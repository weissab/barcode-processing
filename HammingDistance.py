import sys
import csv
from libs.utils import hamming_distance, read_barcodes

# calculates hamming distance between all pairs of sequence provided in a text file and returns list of all hamming distances. 

# Input arguments - index file and number of indexes

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
    #value_hamming_distances = [int(x) for x in value_hamming_distances]
    value_hamming_distances = [i for i in value_hamming_distances if i != 0]
    print(" Min Hamming Distances %s " % (min(value_hamming_distances)))

if __name__ == '__main__':
    main()
