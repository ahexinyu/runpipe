#!/usr/bin/python
import sys
base=0
filename="/rhome/xyhe/bigdata/dataxy/real_read/cut_read"
out2=open("/rhome/xyhe/bigdata/dataxy/real_read/cut_read2","w")
with open(filename)as lines:
    for line in lines:
        if line[0]==">":
            out2.write(">1"+'\n')
        else:
            for ch in line:
                if base<5000:
                    out2.write(ch)
                    base=base+1
                if base==5000:
                    out2.write('\n')
                    out2.write(">2"+'\n')
                    out2.write(ch)
                    base=base+1
                if base<9000 and base>5000:
                    out2.write(ch)
                    base=base+1
                if base==9000:
                    out2.write('\n')
                    out2.write(">3"+'\n')
                    out2.write(ch)
                    base=base+1
                if base>9000:
                    out2.write(ch)
                    base=base+1
print(base)





