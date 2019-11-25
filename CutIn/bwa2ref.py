
from Bio import SeqIO


def bwa2ref(align_path, read_path, ref_path, out_path):
    # file="/rhome/xyhe/bigdata/dataxy/result/ath_moni_bwa.sam"#模拟比对结果
    # read_file="/rhome/xyhe/bigdata/dataxy/PBSIM-PacBio-Simulator/src/ath.fastq"#模拟read文件
    # reference_file="/rhome/xyhe/bigdata/dataxy/reference/lyrata.fasta"#参考基因组文件
    ref_len = dict()
    length_r = dict()
    out = open(out_path, "w")
    for seq_record in SeqIO.parse(read_path, "fastq"):
        ref_len[seq_record.id] = len(seq_record)  # 获取read字典
    for seq_record in SeqIO.parse(ref_path, "fasta"):
        length_r[seq_record.id] = len(seq_record)
    with open(align_path) as lines:
        for line in lines:
            if line[0] == '@':
                continue

            num = 0
            M = 0
            H = 0
            D = 0
            I = 0
            data = line.split()
            cigar = data[5]
            if cigar.find('*') >= 0:
                continue
            read_name = data[0]
            ref_name = data[2]
            reference_len = length_r[ref_name]
            read_length = ref_len[read_name]
            ref_start = int(data[3])
            flagH = 0
            if (int(data[1]) >> 4) & 1:
                dez = "R"
            else:
                dez = "F"
            for ch in cigar:
                if 'A' <= ch <= 'Z':
                    if ch == 'H' or ch == 'S':
                        H += num
                        if flagH == 1:
                            continue
                        flagH = 1
                    if ch == 'D':
                        D += num
                    if ch == 'I':
                        I += num
                    if ch == 'M':
                        M += num
                    num = 0
                else:
                    num = num * 10 + int(ch)
            read_start = H
            ref_end = ref_start + M + D
            read_end = H + M + I
            out.write(str(read_name) + ' ' + str(ref_name) + ' ' + str(dez) + ' ' + str(read_start) + ' ' + str(
                read_end) + ' ' + str(read_length) + ' ' + str(ref_start) + ' ' + str(ref_end) + ' ' + str(
                reference_len) + '\n')
