#!/usr/bin/python
import sys
base=0
read_num=0
out=open('/rhome/xyhe/bigdata/dataxy/target/2mele.fasta','w')
with open(sys.argv[1])as lines:
    for line in lines:
            line=line.strip('\n')
            if read_num<300:
                if line[0]=='>':
                    read_num=read_num+1
                    out.write(line+'\n')
                else:
                    out.write(line+'\n')

