import itertools
import os
import subprocess
import sys
import argparse

import batb2ref
import num2ref

if __name__ == '__main__':
    # Cmd env
    # Modify mummer command
    mummer_bin_dir = ''
    nucmer_cmd='nucmer'
    #nucmer_cmd = os.path.join(mummer_bin_dir, 'nucmer')
    #show_coords_cmd = os.path.join(mummer_bin_dir, 'show-coords')
    show_coords_cmd='show-coords'
    # Modify mecat command
    mecat_old_cmd = '/rhome/xyhe/bigdata/MECAT/Linux-amd64/bin/mecat2ref'
    mecat_new_cmd = '/rhome/xyhe/bigdata/formal/formal/MECAT-master_1/Linux-amd64/bin/mecat2ref'
    #mecat_new_cmd = '/rhome/xyhe/bigdata/2MECAT/mecat2ref'
    mecat_cmd_list = [mecat_old_cmd, mecat_new_cmd]

    # Evaluate command
    road_roller_da = '/bigdata/baolab/huangs/Shared/road_roller_cpp/build/road_roller'

    parser = argparse.ArgumentParser(
        description='种田酱好萌', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--version', action='version', version='%(prog)s 2.01beta')
    parser.add_argument('-w', '--work', required=True, type=str, default=argparse.SUPPRESS,
                        help='Temporary directory for working')
    parser.add_argument('-s', '--src', required=True, type=str, default=argparse.SUPPRESS,
                        help='Read file')
    parser.add_argument('-r', '--ref', required=True, type=str, default=argparse.SUPPRESS,
                        help='Fastq or fasta file of references')
    parser.add_argument('-t', '--target', required=True, type=str, default=argparse.SUPPRESS,
                        help='Fastq or fasta file of targets')
    parser.add_argument('-f', '--from', required=True, type=str, default=argparse.SUPPRESS,
                        help='Alignments file between read and target')
    parser.add_argument('--thread', required=False, type=int, default=16,
                        help='Thread number')
    parser.add_argument('--tp_cov', required=False, type=float, default=0.6,
                        help='Threshold of coverage used by TP')
    parser.add_argument('--fn_cov', required=False, type=float, default=0.6,
                        help='Threshold of coverage used by FN')
    parser.add_argument('--min_diff', required=False, type=int, default=0,
                        help='Minimum length of diff alignments')
    parser.add_argument('--min_aln_cov', required=False, type=int, default=0,
                        help='Minimum coverage of alignments between reads and references')
    parser.add_argument('-g', '--group', required=False, type=bool, default=False,
                        help='Grouped alignments')

    if len(sys.argv) <= 1:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()

    read_path = os.path.abspath(args.src)
    ref_path = os.path.abspath(args.ref)
    target_path = os.path.abspath(args.target)
    read_to_target_path = os.path.abspath(args.__dict__.get('from'))
    thread_num = args.thread

    wrk_dir = os.path.abspath(args.work)
    mummer_dir = os.path.join(wrk_dir, 'nucmer')
    align_dir = os.path.join(wrk_dir, 'align')
    os.makedirs(mummer_dir, exist_ok=True)
    os.makedirs(align_dir, exist_ok=True)

    print('Running NUCMER...')
    subprocess.run([nucmer_cmd, '--maxgap=500', '--minmatch=10', '-p', 'out', target_path, ref_path],
                   stdout=None, stderr=subprocess.STDOUT, cwd=mummer_dir)
    '''subprocess.run([nucmer_cmd, '--maxgap=500', '--mincluster=100', '-p', 'out', target_path, ref_path],
               stdout=None, stderr=subprocess.STDOUT, cwd=mummer_dir)'''
    print('OK')

    print('Runnning SHOW-COORD...')
    with open(os.path.join(mummer_dir, 'out.coords'), 'w') as f:
        subprocess.run([show_coords_cmd, '-B', 'out.delta'],
                       stdout=f, stderr=None, cwd=mummer_dir)
    print('OK')

    print('Running BATB2REF...')
    batb2ref.batb2ref(os.path.join(mummer_dir, 'out.coords'), os.path.join(mummer_dir, 'ref_to_target.ref'))
    print('OK')

    align_path_list = list()

    print('Running MECAT...')

    mecat_dir = os.path.join(align_dir, 'mecat')
    os.makedirs(mecat_dir, exist_ok=True)

    print('\trunning {}'.format(mecat_old_cmd))
    subprocess.run([mecat_old_cmd, '-d', read_path, '-r', ref_path, '-w', os.path.join(mecat_dir, 'wrk'),
                    '-t', str(thread_num), '-o', '1.ref'],
                   stdout=None, stderr=subprocess.STDOUT, cwd=mecat_dir)
    num2ref.num2ref(read_path, os.path.join(mecat_dir, '1.ref'), os.path.join(align_dir, '1.ref'))
    align_path_list.append(os.path.join(align_dir, '1.ref'))
    print('\tok')

    print('\trunning {}'.format(mecat_new_cmd))
    subprocess.run([mecat_new_cmd, '-d', read_path, '-r', ref_path, '-w', os.path.join(mecat_dir, 'wrk'),
                    '-t', str(thread_num), '-o', 'nouse.ref', '-p', '2.ref'],
                   stdout=None, stderr=subprocess.STDOUT, cwd=mecat_dir)
    num2ref.num2ref(read_path, os.path.join(mecat_dir, '2.ref'), os.path.join(align_dir, '2.ref'))
    align_path_list.append(os.path.join(align_dir, '2.ref'))
    print('\tok')

    print('OK')

    print('Spear the Gungnir!')
    cmd_skeleton = [
        road_roller_da, '-s', read_to_target_path, '-r', ref_path, '-t', target_path,
        '-d', os.path.join(mummer_dir, 'ref_to_target.ref'), '--thread', str(thread_num),
        '--tp_cov', str(args.tp_cov), '--fn_cov', str(args.fn_cov), '--min_diff', str(args.min_diff),
        '--min_aln_cov', str(args.min_aln_cov)
    ]

    for align_path in align_path_list:
        cmd_skeleton.append('-a')
        cmd_skeleton.append(align_path)

    if args.group:
        cmd_skeleton.append('-g')

    result = subprocess.run(cmd_skeleton,
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    print('OK')

    print(result.stdout.decode())
