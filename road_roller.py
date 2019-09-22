import argparse
import itertools
import sys
from collections import namedtuple
from concurrent.futures.thread import ThreadPoolExecutor
from enum import Enum
from progressbar import ProgressBar

import parser_tools


def target_range_helper(target_range, read_len, forward, align_range):
    target_minus = target_range[1] - target_range[0]
    left = round(align_range[0] / read_len * target_minus + target_range[0])
    right = round(align_range[1] / read_len * target_minus + target_range[0])
    if forward:
        return left, right
    else:
        target_add = target_range[0] + target_range[1]
        return target_add - right, target_add - left


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='ROAD ROLLER DA!! Wryyyyyyyyyyyy!!', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--version', action='version', version='%(prog)s 1.1')
    parser.add_argument('-s', '--src', required=True, type=str, default=argparse.SUPPRESS,
                        help='Alignments file between read and target')
    parser.add_argument('-r', '--ref', required=True, type=str, default=argparse.SUPPRESS,
                        help='Fastq or fasta file of references')
    parser.add_argument('-t', '--target', required=True, type=str, default=argparse.SUPPRESS,
                        help='Fastq or fasta file of targets')
    parser.add_argument('-a', '--align', required=True, type=str, default=argparse.SUPPRESS,
                        help='Alignments file between reads and references')
    parser.add_argument('-d', '--diff', required=True, type=str, default=argparse.SUPPRESS,
                        help='Alignments file between references and targets')
    parser.add_argument('--thread', required=False, type=int, default=16,
                        help='Thread number')
    parser.add_argument('--tp_cov', required=False, type=float, default=0.8,
                        help='Threshold of coverage used by TP')
    parser.add_argument('--fn_cov', required=False, type=float, default=0.8,
                        help='Threshold of coverage used by FN')

    if len(sys.argv) <= 1:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()

    # Arguments
    thread_num = args.thread
    tp_cov = args.tp_cov
    fn_cov = args.fn_cov
    ref_path = args.ref
    target_path = args.target
    src_align_path = args.src
    ref_align_path = args.align
    diff_align_path = args.diff

    print('Loading References..............', end='')
    sys.stdout.flush()
    # Get reference information
    ref_lens = dict()

    for name, size in parser_tools.seq_name_and_len(ref_path):
        ref_lens[name] = size
    print('OK!')

    print('Loading Targets.................', end='')
    sys.stdout.flush()
    # Get target information
    target_lens = dict()

    for name, size in parser_tools.seq_name_and_len(target_path):
        target_lens[name] = size
    print('OK!')

    # Generate map between name and index of target
    target_to_idx = dict()
    idx_to_target = dict()

    for idx, name in zip(itertools.count(), target_lens):
        target_to_idx[name] = idx
        idx_to_target[idx] = name

    print('Loading Reads and Source........', end='')
    sys.stdout.flush()
    # Parse read source file
    ReadTarget = namedtuple('ReadTarget', ['ref', 'forward', 'begin', 'end', 'len'])
    read_targets = dict()

    for align in parser_tools.parse_align(src_align_path):
        read_targets[align.query] = ReadTarget(
            align.ref, align.forward, align.ref_begin, align.ref_end, align.query_len)
    print('OK!')

    print('Loading Read to Reference.......', end='')
    sys.stdout.flush()
    # Get read alignments aligning to reference
    ReadAlign = namedtuple('ReadAlign', ['ref', 'forward', 'query_begin', 'query_end', 'ref_begin', 'ref_end'])
    read_aligns = {key: list() for key in read_targets}

    for align in parser_tools.parse_align(ref_align_path):
        if align.ref_len <= ref_lens[align.ref]:
            read_aligns[align.query].append(
                ReadAlign(align.ref, align.forward, align.query_begin, align.query_end, align.ref_begin, align.ref_end))
    print('OK!')

    print('Loading Reference To Target.....', end='')
    sys.stdout.flush()
    # Pre-treat alignments of reference and target
    BaseAlign = namedtuple('BaseAlign', ['ref', 'forward', 'pos'])
    ref_to_target = dict()
    target_aligns = dict()

    for name in ref_lens:
        ref_to_target[name] = [list() for _ in range(0, ref_lens[name])]

    for name in target_lens:
        target_aligns[name] = [False] * target_lens[name]

    for align in parser_tools.parse_align(diff_align_path):
        ref_align = ref_to_target[align.query]
        move_step = (align.ref_end - align.ref_begin - 1) / (align.query_end - align.query_begin - 1)
        move_step = move_step if align.forward else -move_step
        target_cur = align.ref_begin if align.forward else align.ref_end - 1

        for i in range(align.query_begin, align.query_end):
            ref_align[i].append(BaseAlign(target_to_idx[align.ref], align.forward, round(target_cur)))
            target_cur += move_step

        target_align = target_aligns[align.ref]

        for i in range(align.ref_begin, align.ref_end):
            target_align[i] = True
    print('OK!')

    print()
    print('Counting start with {} thread{}, please wait for a second...'.format(thread_num,
                                                                                's' if thread_num > 1 else ''))
    # Core Algorithm
    true_positive, false_positive, true_negative, false_negative = 0, 0, 0, 0

    class ReadType(Enum):
        TP = 0
        FP = 1
        TN = 2
        FN = 3

    def thread_fun(read_name):
        from_target = read_targets[read_name]
        read_align = read_aligns[read_name]

        if len(read_align) > 0:
            target_idx = target_to_idx[from_target.ref]
            aligned = False

            for aln in read_align:
                hit_count = 0
                check_left, check_right = target_range_helper(
                    (from_target.begin, from_target.end),
                    from_target.len,
                    from_target.forward,
                    (aln.query_begin, aln.query_end)
                )

                check_forward = not (from_target.forward ^ aln.forward)

                ref_aln = ref_to_target[aln.ref]
                for pos in range(aln.ref_begin, aln.ref_end):
                    hit = False
                    for base_align in ref_aln[pos]:
                        # Check whether has right mapping
                        if base_align.forward == check_forward and \
                                base_align.ref == target_idx and \
                                check_left <= base_align.pos < check_right:
                            hit = True

                        if hit:
                            break
                    hit_count += 1 if hit else 0

                aligned = hit_count / (aln.ref_end - aln.ref_begin) >= tp_cov

                if aligned:
                    break

            if aligned:
                return ReadType.TP
            else:
                return ReadType.FP
        else:
            target_aln = target_aligns[from_target.ref]
            hit_count = 0

            for pos in range(from_target.begin, from_target.end):
                hit_count += 1 if target_aln[pos] else 0

            if hit_count / (from_target.end - from_target.begin) >= fn_cov:
                return ReadType.FN
            else:
                return ReadType.TN

    future_list = list()

    with ThreadPoolExecutor(max_workers=thread_num) as executor:
        map_list = executor.map(thread_fun, read_targets)

        progress_cnt = 0
        progress_bar = ProgressBar(maxval=len(read_targets), fd=sys.stderr).start()
        for m in map_list:
            read_type = m
            if read_type == ReadType.TP:
                true_positive += 1
            elif read_type == ReadType.FP:
                false_positive += 1
            elif read_type == ReadType.TN:
                true_negative += 1
            elif read_type == ReadType.FN:
                false_negative += 1
            progress_cnt += 1
            progress_bar.update(progress_cnt)
        progress_bar.finish()

    print('Work Done! Congratulations!')
    print()

    print('True  Positive(TP) = {}'.format(true_positive))
    print('False Positive(FP) = {}'.format(false_positive))
    print('True  Negative(NP) = {}'.format(true_negative))
    print('False Negative(FP) = {}'.format(false_negative))
    print('Total Number       = {}'.format(len(read_targets)))
