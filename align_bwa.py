import sys
file="/rhome/xyhe/bigdata/dataxy/result/bwa_ecoli"
out="/rhome/xyhe/bigdata/dataxy/fliter_MECAT/bwa/eco"
with open(file) as lines:
	for line in lines:
		if line[0]=='@':
			continue
		read_name=""
		refname=""
		read_start=0
		read_end=0
		ref_start=0
		ref_end=0
		M=0
		H=0
		D=0
		I=0
		data=line.split()
		read_name=data[0]
        refname=data[2]
        ref_start=int(data[3])
        cigar=data[5]
        flagH=0
        if cigar.find('*')>=0:
            continue
        for ch in cigar:
        	if ch>='A' and ch<='Z':
                if ch=='H' or 'S':
                    H+=num
                    if flagH=1:
                        continue
                    flagH=1
                if ch=='D':
                    D+=num
                if ch=='I':
                    I+=num
                if ch=='M':
                    M+=num
                num=0
            else:
            	num=num*10+int(ch)
        read_start=H
        ref_end=H+M+D
        read_end=H+M=I
        out.write(read_name+' '+read_start+' '+read_end+' '+refname+' '+ref_start+' '+ref_end+'\n')

