#!/usr/bin/python
import sys
out=open("/rhome/xyhe/bigdata/dataxy/temp_res/ref.ecoli","w")
with open(sys.argv[1])as lines:
    count=0
    for line in lines:
        if line[0]=='>':
            data=line.split()
            data[0]=data[0].strip('>')
            name=data[0]
        else:
            count+=1
            length=len(line)
            out.write(str(count)+' '+name+' '+str(length)+'\n')
