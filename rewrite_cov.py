import re
import linecache
import os
import sys

filename1='/rhome/xyhe/bigdata/dataxy/temp_res/ref.yeast'
filename2='/rhome/xyhe/bigdata/dataxy/temp_res/mecat.yeast'

def file_to_matrix(filename1):
    try:
        file=open(filename1,'r')
    except IOError:
        error=[]
        return error
    list=file.readlines()
    lists=[]
    for fields in list:
        fields=fields.strip()
        lists.append(fields)
    file.close()
    return lists
def get_row(filename):
    try:
        file=open(filename,'r')
    except IOError:
        error=[]
        return error
    content=file.readlines()
    row=len(content)
    return row
if __name__=='__main__':
    total_length=0
    total_map_length=0
    length=0
    data1=file_to_matrix(filename1)
    data2=file_to_matrix(filename2)
    rows1=get_row(filename1)
    rows2=get_row(filename2)
    for i in range(rows1):
        data=data1[i].split()
        ref_length=int(data[2])
        total_length+=ref_length
    print('total_length is',total_length)
    matrix=[0]*100000000
    for i in range(rows1):
        for j in range(rows2):
            row_data1=data1[i].split()
            name=row_data1[1]
            row_data2=data2[j].split()
            name2=row_data2[0]
            start=int(row_data2[1])
            end=int(row_data2[2])
            if name==name2:
                for k in range(start,end):
                    matrix[k]=1
        for z in range(100000000):
            if matrix[z]==1:
                length+=1
        total_map_length+=length
        length=0
        for k in range(100000000):
            matrix[k]=0
    print('total_map_length is',total_map_length)



