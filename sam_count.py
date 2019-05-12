#!/usr/bin/python
import sys
read_num=0
align_readnum=0
with open(sys.argv[1])as lines:
    name=""
    prename=""
    for line in lines:
        line=line.strip('\n')
        if line[0]=='@':
            continue
        data=line.split()
        name=data[0]
        if name==prename:
            continue
        else:
            align_readnum=align_readnum+1
            prename=name
            name=""
print('align_readnum is',align_readnum)
