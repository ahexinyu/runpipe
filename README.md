# runpipe

command:
python runpipe.py reads1 reads2 1 output_file_name -s 1 -d ~/bigdata/results

1 respresent reference file sabin1 ,only 1 or 3
-s respresent Specific points,0 or 1, default 0 .0 respresent no specific points
-d respresent output directory .default current directory.

if you want to run runpipe.py successfully,you need to change 'run.conf' file first.
write the absolute path of each executable software and absolute path of reference file(SABIN1 and SABIN3 ) in this file
