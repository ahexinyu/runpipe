#!/usr/bin/python
import sys
basecount=0
out=open("/rhome/xyhe/bigdata/dataxy/temp_res/ours_target.ath","w")
with open(sys.argv[1])as lines:
    pre_base=0
    total_base=0
    flag=0
    name=""
    prename=""
    ref_name=""
    ref_satrt=0
    ref_end=0
    preref_name=""
    preref_start=0
    preref_end=0
    for line in lines:
        line = line.strip('\n')
        data=line.split()
        temp_base=0
        temp_total=0
        name=data[0]
        if len(data)<10:
            print("error is",line)
            continue
        if data[5].isdigit()==False or data[4].isdigit()==False:
            print("error  isdigit is",line)
            continue
        temp_total=int(data[5])-int(data[4])
        ref_name=data[1]
        ref_start=int(data[7])
        ref_end=int(data[8])
        if  name==prename:
            if temp_total<pre_base:
                continue
            else:
                pre_base=temp_total
                preref_name=ref_name
                preref_start=ref_start
                preref_end=ref_end
        else:
            if flag==0:
                pre_base=temp_total
                flag=1
                prename=name
                preref_name=ref_name
                preref_start=ref_start
                preref_end=ref_end
                name=""
                continue
            else:
                total_base+=pre_base
                prename=name
                preref_name=ref_name
                preref_start=ref_start
                preref_end=ref_end
                name=""
                pre_base=temp_total
                flag=1
                out.write(str(preref_name)+' '+str(preref_start)+' '+str(preref_end)+'\n')
