#!/usr/bin/python
import sys

filename="/rhome/xyhe/bigdata/formal/formal/MECAT-master_1/Linux-amd64/bin/nono5"
out=open("/rhome/xyhe/bigdata/formal/formal/MECAT-master_1/Linux-amd64/bin/ecol.5","w")
with open(filename)as lines:
    for line in lines:
        if line[0]=='T'or line[0]=='A'or line[0]=='G'or line[0]=='C' or line[0]=='-':
            continue
        else:
            data=line.split();
            if len(data)!=10:
                print(line)
                continue
            out.write(line)
