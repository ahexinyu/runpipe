.import os
import argparse
import ConfigParser

parser = argparse.ArgumentParser(description='runPipe.py')
parser.add_argument('reads1',help="reads file1,the read file can be either in fasta or fastq format")
parser.add_argument('reads2',help="reads file2,the read file can be either in fasta or fastq format")
parser.add_argument('conf_file',help="config is the config file containing paths to the analysis tools and ref")
parser.add_argument('reference',choices=[1,3],help="ref is the reference file and can be either 1 (for sabin1) or 3 (for sabin3) ",type= int)
parser.add_argument('-s',choices=[0,1],help="-s is an option to analyze specific points and can be either 0 (for no; default) or 1 (for yes) ",default=0,dest='points',type= int)
parser.add_argument('-d',help=" -d is an option to specify the output directory and can be either not specified (default) or specified",dest='output',default="current directory")
args = parser.parse_args()



######read config file########
cp=ConfigParser.ConfigParser()
path_conf=args.conf_file
cp.read(path_conf)
absPath_fastp=cp.get("path","absPath_fastp")
absPath_seqtk=cp.get("path","absPath_seqtk")
absPath_bwa=cp.get("path","absPath_bwa")
absPath_samtools=cp.get("path","absPath_samtools")
absPath_picard=cp.get("path","absPath_picard")
absPath_lofreq=cp.get("path","absPath_lofreq")
absPath_IGV=cp.get("path","absPath_IGV")
ref1=cp.get("reference_file","sabin1")
ref2=cp.get("reference_file","sabin3")

directory=""
reads1=""
reads2=""
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
fastp_command=absPath_fastp+'fastp -i '+ reads1 +' -o 1.fasp -I '+ reads2+' -O 2.fasp --qualified_quality_phred=15 -p'
err=os.system(fastp_command)
if err!=0:
    print('Failed to run fastp')
    exit(-1)

#########seqtk##########
seqtk_command1=absPath_seqtk+'seqtk sample -s seed=11 1.fasp  5000000>1.fq seqtk sample -s seed=11 2.fasp 5000000>2.fq'
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
bwa_command2=absPath_bwa+'bwa mem -t 3 '+ref+' 1.fq 2.fq> mem.sam'
err=os.system(bwa_command2)
if err!=0:
    print('Failed to run bwa mem')
    exit(-1)
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
picard_command=absPath_picard+'picard MarkDuplicates METRICS_FILE=sorted.metrics I=sorted.bam O=rmseqdup.bam REMOVE_SEQUENCING_DUPLICATES=true'
err=os.system(picard_command)
if err!=0:
    if err!=0:
        print('Failed to run picard')
        exit(-1)


########lofreq #######
lofreq_command1=absPath_lofreq+'lofreq call -f '+ref+' rmseqdup.bam -o ' + directory +'/'+'variants.vcf'
lofreq_command2=absPath_lofreq+'lofreq call -f '+ref+' rmseqdup.bam -o trans.vcf'
file_address=directory+'/variants.vcf'
command_delete='rm -f '+file_address
command_delete2='rm -f trans.vcf'
os.system(command_delete2)
if points==0:
    os.system(command_delete)
    err=os.system(lofreq_command1)
    if err!=0:
        print('Failed to run lofreq')
        exit(-1)
else:
    err=os.system(lofreq_command2)
    if err!=0:
        print('Failed to run lofreq')
        exit(-1)
    out=open(file_address,"w")
    points_sab1=['480','525', '935', '2438', '2795', '2879', '6023']
    points_sab3=['472','2034']
    with open("trans.vcf")as lines:
        for line in lines:
            line = line.strip('\n')
            if line[1]=='#':
                out.write(line+'\n')
                continue
            data=line.split()
            if args.reference==1:
                if data[1] in points_sab1:
                    out.write(line+'\n')
                else:
                    continue
            else:
                if data[1] in points_sab3:
                    out.write(line+'\n')
                else:
                    continue




#########IGV#####
IGV_command='sh'+' '+absPath_IGV+'igv.sh'
err=os.system(IGV_command)
if err!=0:
    print('Failed to open IGV')
    exit(-1)
















