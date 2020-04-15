#!/bin/bash

"""
By: Andrea Weiss
Last edited: 15 April 2020

This code is designed to run the python script (specifically the barcode matching algorithm) 
through all files in the directory specified in IN1 while matching to target barcode sequences in IN2


INPUTS 
IN1 = path to sequencing reads to serach for matching barcodes
In2 = path to location of reference barcodes to match

Inside of loop specify matching algorithm to use

"""

IN1=$(ls ~/Desktop/NGS_Teng/Data/Merged/*.fastqsanger)
IN2=~/Desktop/NGS_Teng/barcodes.txt

for f in $IN1
do
    ./BarcodeCount_MM_clean.py $f $IN2 2
done
