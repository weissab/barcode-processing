#!/c/Users/Andrea/Anaconda3/python


import sys
from libs.utils import read_genome


# import file from website with ipython
# !wget --no-check http:// ... 

# Input arguments - filename, pattern to match and number of mismatches allowed


def parse_args(argv):
    filename = argv[1]
    pattern = argv[2]
    mismatch = int(argv[3]) # number of max mismatches allowed
    return filename, pattern, mismatch


def naive(p, t, mismatch):
    occurrences = [] 
    alignmnets_tried = 0
    character_comparison_total = 0
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        k = 0
        character_comparison = 0
        alignmnets_tried += 1
        for j in range(len(p)):  # loop over characters
            character_comparison += 1
            if t[i+j] != p[j]:  # compare characters
                k += 1
                if k > mismatch:
                    match = False
                    break
        character_comparison_total = character_comparison_total + character_comparison
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences, character_comparison_total, alignmnets_tried


def main():
    filename, pattern, mismatch = parse_args(sys.argv)
    reference_genome = read_genome(filename)
    result, character_comparison_total, alignmnets_tried = naive(pattern, reference_genome, mismatch)
    print(" The pattern matches the genome %d times at locations %s " % (len(result), result))
    print(" alignments tried: %d, character comparisons: %d" % (alignmnets_tried, character_comparison_total))
    #print(" The pattern matches the genome %d times " % len(result))


if __name__ == '__main__':
    main()