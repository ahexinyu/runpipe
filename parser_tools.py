from collections import namedtuple

from Bio import SeqIO


def seq_name_and_len(file_path):
    use_fastq = file_path.endswith('q')
    return ((x.id, len(x)) for x in SeqIO.parse(file_path, 'fastq' if use_fastq else 'fasta'))


AlignInf = namedtuple('AlignInf',
                      ['query', 'ref', 'forward', 'query_begin', 'query_end', 'query_len',
                       'ref_begin', 'ref_end', 'ref_len'])


def parse_align(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            sp = line.split('\t')
            yield AlignInf(sp[0], sp[1], sp[2] == 'F', int(sp[3]), int(sp[4]), int(sp[5]),
                           int(sp[6]), int(sp[7]), int(sp[8]))
