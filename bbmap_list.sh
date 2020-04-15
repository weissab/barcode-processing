#!/bin/bash
"""
By: Andrea Weiss
Last edited: 15 April 2020

This script runs through all files in a specified directory and runs bbmerge (from bbmap suit software) on each file

INPUTS
READ1: path to location of reads 1


NOTE: read1 and read2 must have the same name and be stored in the same location in folders labeled Read1 and Read2, respectively, or they will not be merged
"""

READ1=$(ls ~/Desktop/NGS_Teng/Data/Demultiplexed/Read1/*.fastqsanger)

for f in $READ1
do
    # ./bbmap/bbmerge.sh in1=$f  in2=NGS_Feulin/Data/Demultiplexed/Read2/S1_1-12.fastqsanger out=NGS_Feulin/Data/Merged/S1.fastq.gz qin=33
    FILE_NAME=$(basename $f)
    IN2=~/Desktop/NGS_Teng/Data/Demultiplexed/Read2/$FILE_NAME
    OUT=~/Desktop/NGS_Teng/Data/Merged/$FILE_NAME
    ./bbmap/bbmerge.sh in1=$f  in2=$IN2 out=$OUT qin=33
done
