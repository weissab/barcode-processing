import sys
import csv
from libs.utils import hamming_distance

# import file from website with ipython
# !wget --no-check http:// ... 

# Input arguments - index file and number of indexes

# parrse input arguments
def parse_args(argv):
    string1 = argv[1]
    string2 = argv[2]
    return string1, string2

def runhamming (string1, string2):
    distance = hamming_distance(string1, string2)
    return distance


def main():
    string1, string2 = parse_args(sys.argv)
    distance = runhamming(string1, string2)
    print(distance)


if __name__ == '__main__':
    main()