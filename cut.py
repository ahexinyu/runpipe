#!/usr/bin/python
import sys
base=0
filename="/rhome/xyhe/bigdata/dataxy/reference/ref_ecoli.fq"
out1=open("/rhome/xyhe/bigdata/dataxy/reference/cut1","w")
with open(filename)as lines:
    for line in lines:
        if line[0]=='>':
            out1.write(">NC_011750.2"+'\n')
            continue
        else:
            for ch in line:
                c=ch
                base=base+1
                if base>2070000and base<2090000:
                    out1.write(ch)
