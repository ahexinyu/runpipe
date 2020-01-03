#!/usr/bin/python
import sys
out_file='/rhome/xyhe/bigdata/dataxy/target/mele.fasta'
in_file='/rhome/xyhe/bigdata/dataxy/target/melanogaster.fasta'
length=300
def rmShort(in_file, out_file, length):
    cunt = defaultdict(str)
    with open(in_file) as f_in, open(out_file, 'w') as f_out:
        for line in f_in:
            if line.startswith('>'):
                try:  # 在读取后一条序列的时候处理前一条序列，所以刚刚读取第一行的时候会报错
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
        for seq_id, seq in cunt.items():  # 对于最后一行，无法读取其后一行时处理它，故拿出来专门处理
            if len(seq) > length:
                f_out.write(seq_id)
                f_out.write(seq)

