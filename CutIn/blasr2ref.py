def blasr2ref(align_path, out_path):
    # file="/rhome/xyhe/bigdata/dataxy/result/moni_yeast"#模拟比对文件
    out = open(out_path, "w")  # 生成文件
    with open(align_path) as lines:
        for line in lines:
            data = line.split()
            strr = data[0].split('/')
            read_name = strr[0]
            read_start = int(data[2])
            read_end = int(data[3])
            refname = data[5]
            ref_start = int(data[7])
            qlength = int(data[1])
            ref_length = int(data[6])
            ref_end = int(data[8])
            dec = data[9]
            if dec == "+":
                dev = "F"
            else:
                dev = "R"
                read_start, read_end = qlength - read_end, qlength - read_start
            out.write(str(read_name) + ' ' + str(refname) + ' ' + str(dev) + ' ' + str(read_start) + ' ' + str(
                read_end) + ' ' + str(qlength) + ' ' + str(ref_start) + ' ' + str(ref_end) + ' ' + str(
                ref_length) + '\n')
