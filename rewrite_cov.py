import re
import linecache
import numpy as np
import os
import sys

filename1='/rhome/xyhe/bigdata/dataxy/temp_res/ref.ecoli'
filename2='/rhome/xyhe/bigdata/dataxy/temp_res/ecoli'

def file_to_matrix(filename1):
    try:
        file=open(filename1,'r')
    except IOError:
        error=[]
        return error
    content=file.readlines()
    rows=len(content)
    datamat=np.zeros((rows,3))
    datamat=datamat.astype('str')
    row=0
    for i in range(rows):
        content[i]=content[i].strip().split('\t')
        datamat[row,:]=content[i][:]
        row+=1
    file.close()
    return datamat

if __name__=='__main__':
    total_length=0
    total_map_length=0
    data1=file_to_matrix(filename1)
    data2=file_to_matrix(filename2)
    [rows1,cols1]=data1.shape
    [rows2,cols2]=data2.shape
    for i in range(rows1):
        data=data[i].split()
        ref_length=int(data[2])
        total_length+=ref_length
    print('total_length is',total_length)
    for i in range(rows1):
        for j in range(rows2):
            matrix=[0]*10000000
            row_data1=data[i].split()
            name=int(row_data1[2])
            row_data2=data2[j].split()
            name2=int(row_data2[2])
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




