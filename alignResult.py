import sys
file="/rhome/xyhe/bigdata/dataxy/result/moni_ath"
out=open("/rhome/xyhe/bigdata/dataxy/fliter_MECAT/blasr/ath","w")
with open(file) as lines:
    read_name=""
    refname=""
    read_start=0
    read_end=0
    ref_start=0
    ref_end=0
    qlength=0
    ref_length=0
    dev=""
    dec=""
    for line in lines:
        data=line.split();
        read_name=data[0]
        read_start=int(data[2])
        read_end=int(data[3])
        refname=data[5]
        ref_start=int(data[7])
        qlength=int(data[1])
        ref_length=int(data[6])
        ref_end=int(data[8])
        dec=data[4]
        if dec=="+":
            dev="F"
        else:
            dev="R"
        out.write(str(read_name)+' '+str(refname)+' '+str(dev)+' '+str(read_start)+' '+str(read_end)+' '+str(qlength)+' 'str(ref_start)+' '+str(ref_end)+' '+str(ref_length)+'\n')
