#!/bin/bash


READ1=$(ls ~/Desktop/NGS_Teng/Data/Demultiplexed/Read1/*.fastqsanger)

for f in $READ1
do
    # ./bbmap/bbmerge.sh in1=$f  in2=NGS_Feulin/Data/Demultiplexed/Read2/S1_1-12.fastqsanger out=NGS_Feulin/Data/Merged/S1.fastq.gz qin=33
    FILE_NAME=$(basename $f)
    IN2=~/Desktop/NGS_Teng/Data/Demultiplexed/Read2/$FILE_NAME
    OUT=~/Desktop/NGS_Teng/Data/Merged/$FILE_NAME
    ./bbmap/bbmerge.sh in1=$f  in2=$IN2 out=$OUT qin=33
done
