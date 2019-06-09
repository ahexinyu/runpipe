import re
import linecache
import numpy as np
import os

filename1='/rhome/xyhe/bigdata/dataxy/temp_res/ref.ecoli'
filename2='/rhome/xyhe/bigdata/dataxy/temp_res/ecoli'

def file_to_matrix(filename1):
    file=open(filename1)
    lines=file.readlines()
    rows=len(lines)
    datamat=np.zeros((rows,3))
    row=0
    for line in lines:
        line=line.strip.split('\t')
        datamat[roe,:]=line[:]
        row+=1
    return datamat

if _name_=='_main_':
    total_length=0
    total_map_length=0
    data1=file_to_matrix(filename1)
    data2=file_to_matrix(filename2)
    [rows1,cols1]=data1.shape
    [rows2,cols2]=data2.shape
    for i in range(rows1)
        data=data[i].split()
        ref_length=data[2]
        total_length+=ref_length
    print('total_length is',total_length)
    for i in range(rows1):
        for j in range(rows2):
            matrix=[0]*10000000
            row_data1=data[i].split()
            name=row_data1[2]
            row_data2=data2[j].split()
            name2=row_data2[2]
            if name==name2:
                for k in range(10000000):
                    matrix[k]=1
        for k in range(10000000):
            if matrix[k]==1:
                length+=1
        total_map_length+=length
        length=0
        matrix=[0]*10000000
    print('total_map_length is',total_map_length)





