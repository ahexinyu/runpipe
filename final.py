import os
file1=""#read_origin文件
file2=""#read_ref文件
file3=""
read_name_origin=[]
with open(file1) as lines:
    for line in lines:
        data=line.split()
        read_name_origin.append(data[0])
print（read_name_origin)

#with open(file2) as lines:


