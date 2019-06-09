//
//  main.c
//  compute
//
//  Created by 何欣雨 on 2019/5/28.
//  Copyright © 2019年 tony. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "Header.h"
#include <string.h>
static reference_ *point;
static ref2 *ref_data;
static int count=0;
static int count2=0;
int open_SAMfile(const char *reference_file,const char *file) {
    FILE *fp;char *fq;char *str;int start=0,end=0;int flag;
    FILE *fp2;int flag2;int length2;
    float *coverage;
    int *database;
    fp2=fopen(file,"r");int num;
    char *name;int name_length;int name_length2;
    fp=fopen(reference_file,"r");
    fq=(char *)malloc(100000000);
    setvbuf(fp, fq, _IOFBF, 100000000);
    point=(reference_ *)malloc(10000000*sizeof(reference_));
    str=(char *)malloc(10000000);
    while((flag=fscanf(fp,"%s\t%d\t%d\n",str,&start,&end))!=EOF){
        point[count].name=str;
        name_length=strlen(str);
        point[count].start=start;
        point[count].end=end;
        point[count].flag=0;
        str=str+name_length+1;
        count++;
    }
    printf("count is %d\n",count);
    name=(char*)malloc(10000000);
    ref_data=(ref2 *)malloc(10000000*sizeof(ref2));
    while((flag2=fscanf(fp2, "%d\t%s\t%d\n",&num,name,&length2))!=EOF){
        ref_data[count2].name=name;
        ref_data[count2].num=num;
        name_length2=strlen(name);
        ref_data[count2].length=length2;
        name=name+name_length2+1;
        count2++;
    }
    int i,j;
    for( i=0;i<count;i++){
        for( j=0;j<count2;j++){
            if(strcmp(point[i].name,ref_data[j].name)==0){
                point[i].length=ref_data[j].length;
            }
        }
    }
    database=(int *)malloc(100000000*sizeof(int));
    for (i=0;i<100000000;i++){
        database[i]=0;
    }
 
    int k;float real_length=0.0;float total_len=0.0;
    for( i=0;i<count2;i++){
        for(j=0;j<count;j++){
            if(strcmp(point[j].name,ref_data[i].name)==0){
                for(k=point[j].start;k<point[j].end;k++){
                    database[k]=1;
                }
            }
        }
        for(k=0;k<100000000;k++){
            if(database[k]==1){
                real_length++;
            }
        }
        for(k=0;k<100000000;k++){
            database[k]=0;
        }
    }
    for(i=0;i<count2;i++){
        total_len=total_len+ref_data[i].length;
    }
    float qqq;
    qqq=real_length/total_len;
    printf("%f\n",qqq);
    printf("%f\n",real_length);
    printf("%f\n",total_len);
    free(fq);
    fclose(fp2);
    fclose(fp);
    return 0;
}

int main(int argc, const char * argv[]) {
    char path[200]="/rhome/xyhe/bigdata/dataxy/temp_res/bwa.ath";//三个参数的
    char path2[200]="/rhome/xyhe/bigdata/dataxy/temp_res/ref.ath";
    open_SAMfile(path,path2);
    return 0;
}
