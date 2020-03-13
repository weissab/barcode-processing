# List of functions useful in manipulations for read alignmnet algorithms

import matplotlib.pyplot as plt
import collections
import pprint


def read_fastq(filename):
    sequences = []
    qualities = []
    with open(filename) as f:
        while True:
            f.readline()  # skip name line
            seq = f.readline().rstrip()  # read base sequence
            f.readline()  # skip placeholder line
            qual = f.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def read_genome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


def reverse_complement(sequence):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a', 'n': 'n', }
    rev_comp_sequence = ''
    for base in sequence:
        rev_comp_sequence = complement[base] + rev_comp_sequence
    return rev_comp_sequence


def naive(pattern, reference_genome):
    occurrences = []
    for i in range(len(reference_genome) - len(pattern) + 1):  # loop over alignments
        match = True
        for j in range(len(pattern)):  # loop over characters
            if reference_genome[i+j] != pattern[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

    
def phred33toQ(qual):
        return ord(qual) - 33 # function ord takes a characer and converts it to ASC intereger value


def create_histogram(qualities):
    hist = [] * len(qualities)
    for qual in qualities:
        for phred in qual:
            q = phred33toQ(phred)
            hist[q] += 1
        return hist

def plot_histogram (hist): 
    # matplotlib inline
    plt.bar(range(len(hist)), hist) #gives x and y values
    plt.show() 


""" def findGCbyPos(reads):
    gc = [0] * len(reads)
    totals = [0] * len(reads)
    for read in reads:
        for i in range(len(reads)):
            if read[i] == ‘c’ or read [i] == ‘g’:
                gc[i] += 1
            totals[i] += 1
        for i in range(len(gc)):
            if totals[i] > 0:
                gc[i] /= float(totals[i]) #convert totals[i] to a float so it will not truncate integers or anything
        return gc

gc = findGCbyPos(seqs)
plt.plot(range(len(gc)), gc)
plt.show() """

def nucleotide_distribution(reads):
    count = collections.counter()
    for seq in reads:
        count.update(seq)
    return count


def pretty_print(value):
    pp = pprint.PrettyPrinter(indent=2)
    return pp.pprint(value)

def hamming_distance(string1, string2):
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i]:
            distance += 1
    return distance