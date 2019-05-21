#!/usr/bin/python
import sys
base=0
with open(sys.argv[1])as lines:
    name=""
    prename=""
    pre_M=0
    total_M=0
    pre_station=0
    pre_total=0
    total_base=0
    flag=0
    for line in lines:
        line=line.strip('\n')
        if line[0]=='@':
            continue
        data=line.split()
        num=0
        start_location=0
        name=data[0]
        cigar=data[5]
        temp_M=0
        temp_D=0
        start_location=0
        temp_count=0
        if cigar.find('*')>=0:
                continue
        for ch in cigar:
            if ch>='A' and ch<='Z':
                if ch=='H':
                    start_location=num
                if ch=='D':
                    temp_D+=num
                if ch=='M'or ch=='I':
                    temp_count+=num
                if ch=='M':
                    temp_M+=num
                num=0
            else:
                num=num*10+int(ch)
        if prename==name:
            if temp_count<pre_total:
                continue
            else:
                pre_M=temp_M
                pre_total=temp_count
        else:
            if flag==0:
                pre_M=temp_M
                pre_total=temp_count
                flag=1
                prename=name
                pre_station=start_location
                name=""
                continue
            else:
                total_M+=pre_M
                total_base+=pre_total
                pre_M=temp_M
                pre_total=temp_count
                prename=name
                pre_station=start_location
                name=""
                flag=1
print("M is",total_M);
print("total_base is",total_base)
