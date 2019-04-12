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
absPath_bwa=cp.get("path","absPath_bwa")
absPath_samtools=cp.get("path","absPath_samtools")
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
command_load='module load fastp'
err=os.system(command_load)
if err!=0:
    print('Failed to load fastp')
    exit(-1)
fastp_command=absPath_fastp+'fastp -i '+ reads1 +' -o 1.fasp -I '+ reads2+' -O 2.fasp --qualified_quality_phred=15 -p'
err =os.system(fastp_command)
if err!=0:
    print('Failed to run fastp')
    exit(-1)

#########seqtk##########
seqtk_command1=absPath_seqtk+'seqtk sample -s seed=11 1.fasp 500>1.fq seqtk sample -s seed=11 2.fasp 500>2.fq'
err=os.system(seqtk_command1)
if err!=0:
    print('Failed to run seqtk command')
    exit(-1)


#########bwa############
bwa_command1=absPath_bwa+'bwa index '+ ref
err=os.system(bwa_command1)
if err!=0:
    print('Failed to run bwa index')
    exit(-1)
bwa_command2=absPath_bwa+'bwa mem -t 3 '+ref+' 1.fq 2.fq > mem.sam'
err=os.system(bwa_command2)
if err!=0:
    print('Failed to run bwa mem')
    exit(-1)
command_load='module load samtools'
os.system(command_load)
bwa_command3=absPath_samtools+'samtools sort mem.sam>sorted.sam'
err=os.system(bwa_command3)
if err!=0:
    print('Failed to run samtools sort')
    exit(-1)
bwa_command4=absPath_samtools+'samtools view -h sorted.sam > sorted.bam'
err=os.system(bwa_command4)
if err!=0:
    print('Failed to run samtools view')
    exit(-1)
          
          

########picard#######









