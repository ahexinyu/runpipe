#!/usr/bin/python
import sys
read_num=0
out=open('/rhome/xyhe/bigdata/dataxy/target/mele','w')
with open(sys.argv[1])as lines:
    for line in lines:
        line =line.strip('\n')
        if read_num<400:
            if line[0]=='>':
                read_num=read_num+1
                out.write(line)
            else:
                out.write(line)

