#!/usr/bin/python
import sys

filename="/rhome/xyhe/bigdata/dataxy/PBSIM-PacBio-Simulator/src/data/human"
out=open("/rhome/xyhe/bigdata/dataxy/PBSIM-PacBio-Simulator/src/data/human2","w")
with open(filename)as lines:
    for line in lines:
        data=line.split()
        out.write(str(data[0])+' '+str(data[1])+' '+str(data[2])+' '+str(data[3])+' '+str(data[4])+' '+str(data[6])+' '+str(data[7])+' '+str(data[8])+' '+str(data[9])+'\nope')
