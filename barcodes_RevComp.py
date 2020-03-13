#!/c/Users/Andrea/Anaconda3/python

import sys
import csv
from libs.utils import read_barcodes, reverse_complement

# import file from website with ipython
# !wget --no-check http:// ... 

# Input arguments - filename, pattern to match and number of mismatches allowed

# parrse input arguments
def parse_args(argv):
    barcode_file = argv[1]
    return barcode_file


# Loops through read file once and compares each barcode instead of vise versa
# Should be a little bit faster than V1
# !!!This only works if all barcodes have the same length!!!
def take_comp(barcodes):
    barcodes_RevComp = {}
    #barcode_len = len(barcodes[0])
    # Initialize it so that the order is kept
    for barcode in barcodes:
        barcodes_RevComp.setdefault(barcode, 0)
        barcodes_RevComp[barcode] = reverse_complement(barcode)
    return barcodes_RevComp


def main():
    barcode_file = parse_args(sys.argv)
    barcodes = read_barcodes(barcode_file)
    barcodes_RevComp = take_comp(barcodes)
    print(" Table of barcodes %s " % (barcodes_RevComp))


if __name__ == '__main__':
    main()