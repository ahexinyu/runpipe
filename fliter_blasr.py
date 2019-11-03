#!/usr/bin/python
import sys
base=0
start=0
end=0
totalbase=0
M_base=0
read_num=0
with open(sys.argv[1])as lines:
    name=""
    prename=""
    pre_len=0
    pre_M=0
    temp_len=0
    qlength=0
    flag=0
    dev=""
    for line in lines:
        data=line.split()
        name=data[0]
        start=int(data[2])
        end=int(data[3])
        dev=data[9]
        temp_len=end-start
        qlength=int(data[1])
        if temp_len<500:
            continue
        if dev=="-":
            start,end = qlength-start,qlength-end
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
                read_num=read_num+1
                flag=1
print("read num is",read_num)
print('M_base is',M_base)
print('total_base is',totalbase)
