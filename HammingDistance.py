import sys
import csv
from libs.utils import hamming_distance, read_barcodes

"""
By: Andrea Weiss
Last edited: April 15 2020

The purpose of this script is to calculate the hamming distance between all pairs of sequence provided in a text file and returns the minumum hamming distance

INPUTS
index_file: file containing all sequences to be analyzed for hamming distance
number of indexes: number of sequenes that will be compared for hamming distance
"""


# parrse input arguments
def parse_args(argv):
    index_file = argv[1]
    num_index = argv[2]
    return index_file, num_index


def hamming_distance_all(indexes, num_index):
    hamming_distance_all = []
    for i in range(num_index):
        for j in range(num_index):
            hamming_distance_next = hamming_distance(indexes[i], indexes[j])
            hamming_distance_all.append(hamming_distance_next)
    return hamming_distance_all


def main():
    index_file, num_index = parse_args(sys.argv)
    indexes = read_barcodes(index_file)
    value_hamming_distances = hamming_distance_all(indexes, int(num_index))
    value_hamming_distances = [i for i in value_hamming_distances if i != 0]
    print(" Min Hamming Distances %s " % (min(value_hamming_distances)))

if __name__ == '__main__':
    main()
