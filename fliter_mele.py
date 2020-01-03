#!/usr/bin/python
import sys
out_file='/rhome/xyhe/bigdata/dataxy/target/mele.fasta'
in_file='/rhome/xyhe/bigdata/dataxy/target/melanogaster.fasta'
def rmShort(in_file, out_file, length):
    cunt = defaultdict(str)
    with open(in_file) as f_in, open(out_file, 'w') as f_out:
        for line in f_in:
            if line.startswith('>'):
                try:
                    seq = cunt.pop(id_)
                    if len(seq) > length:
                        f_out.write(id_)
                        f_out.write(seq)
                except:
                    pass
                finally:
                    id_ = line
            else:
                cunt[id_] += line
        for seq_id, seq in cunt.items():
            if len(seq) > length:
                f_out.write(seq_id)
                f_out.write(seq)
if __name__ == '__main__':
    rmShort(in_file,out_file,300)

