# runPipe, by Xinyu He, School of Software Engineering, Beijing Jiaotong University (contact: 17121708@bjtu.edu.cn)

Command:
python runPipe.py  reads1 reads2 config ref [option | option]

Mandatory parameters:
    reads1 and reads2 are the read files and can be either in fasta or fastq format
    config is the config file containing paths to the analysis tools and ref
    ref is the reference file and can be either 1 (for sabin1) or 3 (for sabin3)

Optional parameters:
    -s is an option to analyze specific points and can be either 0 (for no; default) or 1 (for yes) 
    -d is an option to specify the output directory and can be either not specified (default) or specified
