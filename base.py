#!/usr/bin/python
import sys
base=0
with open(sys.argv[1])as lines:
    for line in lines:
        line=line.strip('\n')
        data=line.split()
        base=base+len(data[1])
print('base is',base)
