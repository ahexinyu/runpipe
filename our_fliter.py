#!/usr/bin/python
import sys
basecount=0
read_num=0
with open(sys.argv[1])as lines:
    pre_base=0
    total_base=0
    flag=0
    name=""
    prename=""
    for line in lines:
        line = line.strip('\n')
        data=line.split()
        temp_base=0
        temp_total=0
        name=data[0]
        if len(data)<10:
            continue
        if data[5].isdigit()==False or data[4].isdigit()==False:
            continue
        temp_total=int(data[5])-int(data[4])
        if temp_total<500:
            continue
        if  name==prename:
            if temp_total<pre_base:
                continue
            else:
                pre_base=temp_total
        else:
            if flag==0:
                pre_base=temp_total
                flag=1
                prename=name
                name=""
                continue
            else:
                total_base+=pre_base
                prename=name
                name=""
                pre_base=temp_total
                read_num=read_num+1
                flag=1
print('read_num',read_num)
print('total_base is',total_base)
