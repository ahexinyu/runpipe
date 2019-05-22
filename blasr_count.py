#!/usr/bin/python
import sys
base=0
start=0
end=0
totalbase=0
M_base=0
with open(sys.argv[1])as lines:
    name=""
    prename=""
    pre_len=0
    pre_M=0
    temp_len=0
    flag=0
    for line in lines:
        data=line.split()
        name=data[0]
        start=int(data[2])
        end=int(data[3])
        temp_len=end-start
        if name==prename:
            if temp_len>pre_len:
                pre_M=int(data[11])
                pre_len=temp_len
            else:
                continue
        else:
            if flag==0:
                pre_M=int(data[11])
                pre_len=temp_len
                name=""
                prename=name
                flag=1
            else:
                totalbase=totalbase+pre_len
                M_base=M_base+pre_M
                prename=data[0]
                name=""
                pre_M=int(data[11])
                pre_len=temp_len
                flag=1
print('M_base is',M_base)
print('total_base is',totalbase)
