import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} [btab format file] [output file]'.format(sys.argv[0]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r') as in_file, open(sys.argv[2], 'w') as out_file:
        for line in in_file:
            sp = line.split('\t')
            query_name = sp[0]
            ref_name = sp[5]
            forward = sp[17] == 'Plus'
            query_begin = int(sp[6]) - 1
            query_end = int(sp[7])
            query_len = int(sp[2])
            ref_begin = int(sp[8]) - 1
            ref_end = int(sp[9])
            ref_len = int(sp[18])

            if forward is False:
                query_begin, query_end = query_end, query_begin

            out_file.write('{}\t{}\t'.format(query_name, ref_name))
            out_file.write('{}\t'.format('F' if forward else 'R'))
            out_file.write('{}\t{}\t{}\t'.format(query_begin, query_end, query_len))
            out_file.write('{}\t{}\t{}'.format(ref_begin, ref_end, ref_len))
            out_file.write('\n')
