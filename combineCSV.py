import sys
import os
import csv

"""
By: Andrea Weiss (with much help from Loic Gasser)
Last edited: 15 April 2020

This program is designed to merge the .csv output files after running the barcode matching .py script on 
The header of each column in the resulting file will correspond to each sample id (corresponding to the name of the original .csv file)

INPUTS: 
direcotry: path to all files to be merged
"""


# parrse input arguments
def parse_args(argv):
    directory = argv[1]
    return directory


def list_csvs(path):
    return [f for f in os.listdir(path) if f.endswith('csv') and not f.endswith('all_results.csv')]


def read_cvs(filename):
    with open(filename) as f:
        csvreader = csv.reader(f)
        results = [r for r in csvreader if len(r)]
    return results


def main():
    directory = parse_args(sys.argv)
    basenames = [os.path.basename(csv_file).split('.fastqsanger.fastqsanger_result.csv')[0] for csv_file in list_csvs(directory)]

    with open('{}/all_results.csv'.format(directory), 'w', newline='') as final:
        writer = csv.DictWriter(final, fieldnames=basenames)
        writer.writeheader()

        final_res = {}
        for csv_file in list_csvs(directory):
            for res in read_cvs('{}/{}'.format(directory, csv_file)):
                basename = os.path.basename(csv_file).split('.fastqsanger.fastqsanger_result.csv')[0]
                if basename not in final_res:
                    final_res[basename] = []
                final_res[basename].append(res[1])

        nb_rows = len(final_res[basename])
        for i in range(nb_rows):
            new_row = {}
            for name in basenames:
                new_row[name] = final_res[name][i]
            writer.writerow(new_row)



if __name__ == '__main__':
    main()