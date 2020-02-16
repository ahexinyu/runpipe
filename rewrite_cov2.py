import numpy as np

if __name__ == '__main__':
    ref_file = '/rhome/xyhe/bigdata/dataxy/moni/jurei/jurei.info'
    align_file = '/rhome/xyhe/bigdata/dataxy/moni/jurei/blasr_start_to_end'

    ref_arr = dict()

    total_len = 0

    with open(ref_file) as f:
        for line in f:
            sp = line.split(' ')

            ref_name = sp[1]
            ref_len = int(sp[2])

            total_len += ref_len

            ref_arr[ref_name] = np.zeros(ref_len, dtype=bool)

    error_count = 0

    with open(align_file) as f:
        for line in f:
            sp = line.split(' ')

            ref_name = sp[0]
            begin = int(sp[1])
            end = int(sp[2])

            # end = min(end, len(ref_arr[ref_name]))

            if end > len(ref_arr[ref_name]):
                error_count += 1
            else:
                ref_arr[ref_name][begin - 1:end] = True
                # print('{} {}'.format(begin-1,end))

    count = np.array([np.add.reduce(x) for x in ref_arr.values()]).sum()

    print('num of error = {}'.format(error_count))

    print('count = {}'.format(count))

    print('sum = {}'.format(total_len))

    print('coverage = {}'.format(count / total_len))
