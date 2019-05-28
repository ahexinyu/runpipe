#!/usr/bin/python
import sys
out=open("/rhome/xyhe/bigdata/dataxy/temp_res/ref.yeast","w")
with open(sys.argv[1])as lines:
    count=0
    flag=0
    prename=""
    for line in lines:
        if line[0]=='>':
            data=line.split()
            data[0]=data[0].strip('>')
            if flag==0:
                count+=1
                flag=1
                prename=data[0]
            else:
                out.write(str(count)+' '+prename+' '+str(length)+'\n')
            prename=data[0]
            length=0
            count+=1
        else:
            length+=len(line)
        out.write(str(count)+' '+prename+' '+str(length)+'\n')
