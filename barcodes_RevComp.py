#!/c/Users/Andrea/Anaconda3/python

import sys
import csv
from libs.utils import read_barcodes, reverse_complement

"""
By: Andrea Weiss
Last edited: 15 April 2020

Calculate the reverse complement of a list of sequences 

INPUTS:
barcode_file: file of all sequnces to take reverse complement of


"""

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