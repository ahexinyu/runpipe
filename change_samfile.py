#!/usr/bin/python
import sys
base=0
out=open("/rhome/xyhe/bigdata/dataxy/temp_res/target_ath2","w")
with open(sys.argv[1])as lines:
    name=""
    prename=""
    refname=""
    prerefname=""
    pre_M=0
    pre_D=0
    total_M=0
    pre_station=0
    pre_total=0
    total_base=0
    flag=0
    end=0
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
        temp_count=0
        start_location=int(data[3])
        refname=data[2]
        if cigar.find('*')!=-1:
            continue
        for ch in cigar:
            if ch>='A' and ch<='Z':
                if ch=='I'or ch=='M':
                    temp_count+=num
                if  ch=='D':
                    temp_D+=num
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
                pre_D=temp_D
                prelocation=start_location
                prerefname=refname
                pre_total=temp_count
        else:
            if flag==0:
                pre_M=temp_M
                pre_D=temp_D
                pre_total=temp_count
                flag=1
                prename=name
                prerefname=data[2]
                name=""
                continue
            else:
                total_M+=pre_M
                total_base+=pre_total
                pre_M=temp_M
                pre_total=temp_count
                prename=name
                prerefname=refname
                pre_station=start_location
                end=start_location+temp_M+temp_D
                name=""
                flag=1
                out.write(prerefname+' '+str(pre_station)+' '+str(end)+'\n')
