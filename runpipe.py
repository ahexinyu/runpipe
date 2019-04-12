import os
import argparse
import ConfigParser

parser = argparse.ArgumentParser(description='runPipe.py')
parser.add_argument('reads1',help="reads file1")
parser.add_argument('reads2',help="reads file2")
parser.add_argument('reference',choices=[1,3],help="reference file Sabin1 or Sabin3 ",type= int)
parser.add_argument('-s',choices=[0,1],help="Specific points,0 or 1",default=0,dest='points',type= int)
parser.add_argument('-d',help="Output directory",dest='output',default="current directory")
args = parser.parse_args()



######read config file########
cp=ConfigParser.ConfigParser()
cp.read('run.conf')
absPath_fastp=cp.get("path","absPath_fastp")
absPath_seqtk=cp.get("path","absPath_seqtk")
ref1=cp.get("reference_file","sabin1")
ref2=cp.get("reference_file","sabin3")

directory=""
reads1=""
reads1=""
ref=""
points=0

reads1=args.reads1
reads2=args.reads2
if args.reference==1:
    ref=ref1
else:
    ref=ref2
print ref
points=args.points
pwd=os.getcwd()
if args.output=="current directory":
    directory=pwd
else:
    directory=args.output


##########fastp################
os.system('module load fastp/0.19.4')
fastp_command=absPath_fastp + 'fastp -i '+ reads1 +' -o 1.fasp -I '+ reads2+' -O 2.fasp --qualified_quality_phred=15 -p'
err =os.system(fastp_command)
if err!=0:
    print('Failed to run fastp')
    exit(-1)

#########seqtk##########
seqtk_command1=absPath_seqtk+'seqtk sample -s seed=11 1.fasp 5000000>1.fq'
err=os.system(seqtk_command1)
if err!=0:
    print('Failed to run seqtk command1')
    exit(-1)
seqtk_command2=absPath_seqtk+'seqtk sample -s seed=11 2.fasp 5000000>1.fq'
err=os.system(seqtk_command2)
if err!=0:
    print('Failed to run seqtk command2')
    exit(-1)


#########bwa############
absPath_bwa='~/bigdata/software/bwa/'










