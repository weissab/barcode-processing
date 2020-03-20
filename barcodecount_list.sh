#!/bin/bash


IN1=$(ls ~/Desktop/NGS_Teng/Data/Merged/*.fastqsanger)
IN2=~/Desktop/NGS_Teng/barcodes.txt

for f in $IN1
do
    ./Naive_withMismatch_Barcode_V2.py $f $IN2 2
done
