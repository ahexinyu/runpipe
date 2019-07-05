#!/usr/bin/python
import sys
base=0
filename="/rhome/xyhe/bigdata/dataxy/reference/ref_ecoli.fq"
out1=open("/rhome/xyhe/bigdata/dataxy/reference/cut2","w")
with open(filename)as lines:
    for line in lines:
        if line[0]=='>':
            out1.write(">NC_011750.2"+'\n')
            continue
        else:
            for ch in line:
                c=ch
                base=base+1
                if base>1700000and base<1801000:
                    out1.write(ch)
