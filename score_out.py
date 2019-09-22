import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} [bad mecat reference file] [output file]'.format(sys.argv[0]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r') as in_file, open(sys.argv[2], 'w') as out_file:
        for line in in_file:
            sp = line.split('\t')

            del sp[3]
            out_file.write('{}'.format('\t'.join(sp)))

