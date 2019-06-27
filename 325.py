#!/usr/bin/python
import sys

filename="/rhome/xyhe/bigdata/dataxy/result/extract_ath"
with open(filename)as lines:
    for line in lines:
        data=line.split()
        if data[0]=='962':
            print line
