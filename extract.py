e#!/usr/bin/python
import sys

filename="/rhome/xyhe/bigdata/formal/formal/MECAT-master_1/Linux-amd64/bin/no"
out=open("/rhome/xyhe/bigdata/dataxy/result/extract_ecoli","w")
with open(filename)as lines:
    for line in lines:
        if line[0]=='T'or line[0]=='A'or line[0]=='G'or line[0]=='C' or line[0]=='-':
            continue
        else:
            out.write(line)
