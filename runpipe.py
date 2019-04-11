import os
import argparse


parser = argparse.ArgumentParser(description='runPipe.py')
parser.add_argument('reads1',help="reads file1")
parser.add_argument('reads2',help="reads file2")
parser.add_argument('ref1',help="reference file1")
parser.add_argument('ref2',help="reference file2")
parser.add_argument('-s',choices=[0,1],help="Specific points,0 or 1",default=0,dest='points',type= int)
parser.add_argument('-d',help="Output directory",dest='output',default="current directory")
args = parser.parse_args()

directory=""
reads1=""
reads1=""
ref1=""
ref2=""
points=0

reads1=args.reads1
reads2=args.reads2
ref1=args.ref1
ref2=args.ref2
points=args.points
pwd=os.getcwd()
if args.output=="current directory":
    directory=pwd
else:
    directory=args.output


##########fastp################

absPath_fastp='~/bigdata/software/fastp/'
fastp_command=absPath_fastp + 'fastp -i '+ reads1 +' -o 1.fasp -I '+ reads2+' -O 2.fasp --qualified_quality_phred=15 -p'
err =os.system(fastp_command)
if err!=0:
    print('Failed to run fastp')
    exit(-1)

#########seqtk##########








