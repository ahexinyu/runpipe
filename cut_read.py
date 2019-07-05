#!/usr/bin/python
import sys
base=0
read_num=0
flag=0
filename="/rhome/xyhe/bigdata/dataxy/real_read/ecoli.fasta"
out1=open("/rhome/xyhe/bigdata/dataxy/real_read/cut_read","w")
with open(filename)as lines:
    for line in lines:
        if line[0]=='>':
            read_num=read_num+1
            if read_num==34:
                out1.write(">33"+'\n')
                flag=1
            else:
                flag=0
        else:
            if flag==1:
                out1.write(line)
