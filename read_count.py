#!/usr/bin/python
import sys
read_num=0
length=0
avg=0.00
with open(sys.argv[1])as lines:
    for line in lines:
        line =line.strip('\n')
        if line[0]=='@':
            read_num=read_num+1
        else:
            length+=len(line)
print(avg)
print('read_num is',read_num)

