#!/usr/bin/python
import sys

base=0
readcount=0
ref_array=dict()
with open(sys.argv[1])as lines:
    for line in lines:
        da=line.split()
        ref_name=da[1]
        ref_length=da[2]
        ref_array[ref_name]=ref_length
with open(sys.argv[2])as lines:
    refname=""
    reflength=0
    ref_station=0
    name=""
    prename=""
    pre_M=0
    total_M=0
    pre_station=0
    pre_total=0
    total_base=0
    flag=0
    for line in lines:
        if line[0]=='@':
            continue
        data=line.split()
        if len(data)<11:
            print(line)
            continue
        cigar=data[5]
        if cigar.find('*')>=0:
            continue
        num=0
        start_location=0
        name=data[0]
        refname=data[2]
        reflength=int(ref_array[refname])
        ref_station=int(data[3])
        temp_M=0
        temp_D=0
        temp_count=0
        flag2=0
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
                if(ref_station+temp_M+temp_D)<=reflength:
                    if(ch>='0' and ch<='9'):
                        num=num*10+int(ch)
                    else:
                        flag2=1
                        continue
                else:
                    continue
        if(flag2==1):
            print(line);
            continue
        if temp_count<500:
            continue
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
                readcount=readcount+1
                name=""
                flag=1
print("readcount is",readcount)
print("M is",total_M);
print("total_base is",total_base)
