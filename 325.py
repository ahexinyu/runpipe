#!/usr/bin/python
import sys

filename="/rhome/xyhe/bigdata/formal/formal/MECAT-master_1/Linux-amd64/bin/ath_1"
with open(filename)as lines:
    for line in lines:
        data=line.split()
        if data[0]=='962':
            print line
