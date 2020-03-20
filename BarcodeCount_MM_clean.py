#!/c/Users/Andrea/Anaconda3/python

import sys, os
import csv
from libs.utils import read_genome, read_barcodes

# import file from website with ipython
# !wget --no-check http:// ... 


# Input arguments - filename, pattern to match and number of mismatches allowed

# parrse input arguments
def parse_args(argv):
    filename = argv[1]
    barcode_file = argv[2]
    mismatch = int(argv[3]) # number of max mismatches allowed
    return filename, barcode_file, mismatch


# Loops through read file once and compares each barcode instead of vise versa
# Should be a little bit faster than V1
# !!!This only works if all barcodes have the same length!!!
def count_barcodes_v2(barcodes, sequ_read, max_mismatch):
    barcodes_count = {}
    barcode_len = len(barcodes[0])
    sequ_read_len = len(sequ_read)
    # Initialize it so that the order is kept
    for barcode in barcodes:
        barcodes_count.setdefault(barcode, 0)
    for i in range(sequ_read_len - barcode_len + 1):
        for barcode in barcodes:
            misatch_count = 0
            for j in range(barcode_len):
                if sequ_read[i + j] != barcode[j]:
                    misatch_count += 1
                if misatch_count > max_mismatch:
                    break
            if misatch_count <= max_mismatch:
                barcodes_count[barcode] += 1
    return barcodes_count


def write_to_csv(filename, results):
    with open(filename,'w') as f:
        w = csv.writer(f)
        w.writerows(results.items())


def main():
    filename, barcode_file, mismatch = parse_args(sys.argv)
    reference_file = read_genome(filename)
    barcodes = read_barcodes(barcode_file)
    barcode_count = count_barcodes_v2(barcodes, reference_file, mismatch)
    write_to_csv("%s_result.csv" % filename, barcode_count)
    print(" Table of barcodes %s " % (barcode_count))


if __name__ == '__main__':
    main()