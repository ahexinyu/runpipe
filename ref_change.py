#!/usr/bin/python
import sys
out=open("/rhome/xyhe/bigdata/dataxy/temp_res/mecat.ath","w")
with open(sys.argv[1])as lines:
    name=""
    length=""
    count=0
    for line in lines:
        data=line.split()
        if data[0]=='@SQ':
            name=data[1].strip('SN:')
            length=data[2].strip('LN:')
            count+=1
            out.write(str(count)+' '+name+' '+length+'\n')
