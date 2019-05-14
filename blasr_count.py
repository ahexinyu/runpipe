#!/usr/bin/python
import sys
base=0
start=0
end=0
totalbase=0
M_base=0
with open(sys.argv[1])as lines:
    for line in lines:
        data=line.split()
        start=int(data[2])
        end=int(data[3])
        base=end-start
        totalbase=totalbase+base
        M_base=M_base+int(data[11])
print('M_base is',M_base)
print('total_base is',totalbase)
