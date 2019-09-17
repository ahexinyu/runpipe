import os
import shutil 
txtpath='/rhome/xyhe/bigdata/dataxy/PBSIM-PacBio-Simulator/src/data_yeast'
namelist=[x for x in os.listdir(txtpath)]
fastqfile=[]
count=0
for i in range(len(namelist)):
    if namelist[i].find(".fastq")!=-1:
        fastqfile[count]=namelist[i]    
        count=count+1
print(count)
outfilename='/rhome/xyhe/bigdata/dataxy/PBSIM-PacBio-Simulator/src/yeast.fastq'
outfile=open(outfilename,'a')
for i in range( count ):
    datapath = os.path.join(txtpath, fastqfile[i])
    file=open(datapath,'r')
    shutil.copyfileobj(file,outfile)
    file.close()
outfile.close()
