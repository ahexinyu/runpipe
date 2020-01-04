import sys
import os


def get_fasta_name(file_path):
    fasta_name = ''
    with open(file_path) as fasta_input:
        first_line = fasta_input.readline()
        if first_line.startswith('>'):
            sp = first_line[1:].split()
            if len(sp) > 0:
                fasta_name = sp[0]

    return fasta_name


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} [directory with maf and ref] [output file]'.format(sys.argv[0]),file=sys.stderr)
        exit(1)

    if not os.path.isdir(sys.argv[1]):
        print('{} is not a directory'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    src_dir = sys.argv[1]
    out_file = sys.argv[2]

    with open(out_file, 'w') as output:
        maf_files = (f for f in os.listdir(src_dir)
                     if os.path.isfile(os.path.join(src_dir, f)) and os.path.splitext(f)[1] == '.maf')

        for maf_file in maf_files:
            file_root = os.path.splitext(maf_file)[0]
            ref_name = get_fasta_name(os.path.join(src_dir, '{}{}'.format(file_root, '.ref')))

            with open(os.path.join(src_dir, maf_file)) as maf_input:
                # (name, forward, start, end, srcSize)
                ref_buf = list()
                for line in maf_input:
                    if line.startswith('s'):
                        sp = line.split()
                        ref_buf.append((ref_name if len(ref_buf) == 0 else sp[1], sp[4] == '+', int(sp[2]),
                                        int(sp[2]) + int(sp[3]), int(sp[5])))
                    elif line == '\n':
                        if len(ref_buf) >= 2:
                            output.write('{}\t{}\t'.format(ref_buf[1][0], ref_buf[0][0]))
                            output.write('{}\t'.format('F' if ref_buf[1][1] else 'R'))
                            output.write('{}\t{}\t{}\t'.format(ref_buf[1][2], ref_buf[1][3], ref_buf[1][4]))
                            output.write('{}\t{}\t{}'.format(ref_buf[0][2], ref_buf[0][3], ref_buf[0][4]))
                            output.write('\n')
                        ref_buf.clear()
