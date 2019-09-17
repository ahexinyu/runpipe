import sys
file="/rhome/xyhe/bigdata/dataxy/result/blasr_ath"
out=open("/rhome/xyhe/bigdata/dataxy/fliter_MECAT/blasr/ath","w")
with open(file) as lines:
	read_name=""
	refname=""
	read_start=0
	read_end=0
	ref_start=0
	ref_end=0
	for line in lines:
		data=line.split();
		read_name=data[0]
		read_start=int(data[2])
		read_end=int(data[3])
		refname=data[5]
		ref_start=int(data[7])
		ref_end=int(data[8])
		out.write(str(read_name)+' '+str(read_start)+' '+str(read_end)+' '+str(refname)+' '+str(ref_start)+' '+str(ref_end)+'\n')
