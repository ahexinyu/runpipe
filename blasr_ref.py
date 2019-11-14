#!/usr/bin/python
import sys
base=0
start=0
end=0
totalbase=0
M_base=0
out=open("/rhome/xyhe/bigdata/dataxy/change_ref/euba/blasr_start_to_end","w")
with open(sys.argv[1])as lines:
    name=""
    prename=""
    pre_len=0
    dev=""
    pre_M=0
    temp_len=0
    preref_start=0
    preref_end=0
    preref_name=0
    ref_start=0
    ref_end=0
    ref_name=0
    r_len=0
    flag=0
    for line in lines:
        data=line.split()
        name=data[0]
        dev=data[9]
        r_len=int(data[6])
        start=int(data[2])
        end=int(data[3])
        temp_len=end-start
        ref_end=int(data[8])
        ref_start=int(data[7])
        if dev=="-":
            ref_start,ref_end=r_len-ref_start,r_len-ref_end
        ref_name=data[5]
        if name==prename:
            if temp_len>pre_len:
                pre_M=int(data[11])
                preref_end=ref_end
                preref_name=ref_name
                preref_start=ref_start
                pre_len=temp_len
            else:
                continue
        else:
            if flag==0:
                pre_M=int(data[11])
                preref_end=ref_end
                preref_name=ref_name
                preref_start=ref_start
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
                preref_end=ref_end
                preref_name=ref_name
                preref_start=ref_start
                flag=1
                out.write(str(preref_name)+' '+str(preref_start)+' '+str(preref_end)+'\n')
