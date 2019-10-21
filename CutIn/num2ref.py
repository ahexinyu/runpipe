import os


def num2ref(read_path, align_path, output_path):
    # Inline function #
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

    # Inline function #

    # Start #
    use_fastq = os.path.splitext(read_path)[1][-1] == 'q'

    print('Use fastq? - {}'.format(use_fastq))

    read_names = get_fastq_names(read_path) if use_fastq else get_fasta_names(read_path)

    with open(align_path, 'r', errors='ignore') as in_file, open(output_path, 'w') as out_file:
        line_count = 0
        for line in in_file:
            if line and line[0].isdigit():
                sp = line.split()
                read_num = int(sp[0])
                read_num = read_num if not use_fastq else read_num - 1
                read_name = read_names[read_num] if read_num < len(read_names) else 'UNKNOWN'

                del sp[3]
                out_file.write('{}\t{}\n'.format(read_name, '\t'.join(sp[1:])))
            line_count += 1

