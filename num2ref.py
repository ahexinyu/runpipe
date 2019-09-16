import sys
import argparse
import os


def get_names_with_start(file_path, special):
    name_list = list()
    with open(file_path, 'r') as in_file:
        for line in in_file:
            if line.startswith(special):
                sp = line[1:].split()
                name_list.append(sp[0] if len(sp) > 0 else 'UNKNOWN')

    return name_list


def get_fastq_names(file_path):
    return get_names_with_start(file_path, '@')


def get_fasta_names(file_path):
    return get_names_with_start(file_path, '>')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transform first line of mecat\'s alignment to name')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-r', '--read', required=True, type=str, help='fastq file of reads')
    parser.add_argument('-a', '--align', required=True, type=str, help='alignments file of mecat')
    parser.add_argument('-o', '--output', required=True, type=str, help='output file')

    if len(sys.argv) <= 1:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()

    use_fastq = os.path.splitext(args.read)[1] == '.fastq'

    print('Use fastq? - {}'.format(use_fastq))

    read_names = get_fastq_names(args.read) if use_fastq else get_fasta_names(args.read)

    with open(args.align, 'r') as in_file, open(args.output, 'w') as out_file:
        line_count = 0
        for line in in_file:
            if line_count % 3 == 0:
                sp = line.split()
                read_num = int(sp[0])
                read_num = read_num if not use_fastq else read_num - 1
                read_name = read_names[read_num] if read_num < len(read_names) else 'UNKNOWN'
                out_file.write('{}\t{}\n'.format(read_name, '\t'.join(sp[1:])))
            line_count += 1

