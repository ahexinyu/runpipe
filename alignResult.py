import sys
file="/rhome/xyhe/bigdata/dataxy/result/moni_yeast"
out=open("/rhome/xyhe/bigdata/dataxy/fliter_MECAT/blasr/yeast","w")
with open(file) as lines:
    read_name=""
    refname=""
    read_start=0
    read_end=0
    ref_start=0
    ref_end=0
    qlength=0
    ref_length=0
    strr=""
    dev=""
    dec=""
    for line in lines:
        data=line.split();
        strr=data[0].split('/')
        read_name=strr[0]
        read_start=int(data[2])
        read_end=int(data[3])
        refname=data[5]
        ref_start=int(data[7])
        qlength=int(data[1])
        ref_length=int(data[6])
        ref_end=int(data[8])
        dec=data[9]
        if dec=="+":
            dev="F"
        else:
            dev="R"
            read_start, read_end = qlength - read_end, qlength - read_start
        out.write(str(read_name)+' '+str(refname)+' '+str(dev)+' '+str(read_start)+' '+str(read_end)+' '+str(qlength)+' '+str(ref_start)+' '+str(ref_end)+' '+str(ref_length)+'\n')
