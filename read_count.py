#!/usr/bin/python
import sys
read_num=0
length=0
out=open("/rhome/xyhe/bigdata/dataxy/length","w")
with open(sys.argv[1])as lines:
    for line in lines:
        line =line.strip('\n')
        if line[0]=='@':
            read_num=read_num+1
            length=0
        else:
            length+=len(line)
            out.write(str(length)+'\n')
print('read_num is',read_num)

