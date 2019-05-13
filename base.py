#!/usr/bin/python
import sys
base=0
with open(sys.argv[1])as lines:
    for line in lines:
        line=line.strip('\n')
        if line[0]=='>':
            continue
        else:
            base=base+len(line)
print('base is',base)
