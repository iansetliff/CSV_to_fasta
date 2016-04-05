# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 23:22:18 2016

@author: Ian
"""
import csv 

#what you want to save the fasta file as
f_out = open("sample_seqs_fasta.fasta", 'w')

#read in sequences CSV
#in this code, it's assumed first column is PDB ID and second column is sequence of interest
with open('Sample_Seqs.csv', mode='r') as f:
    reader = csv.reader(f, delimiter=',')
    list_items = [[rows[0],rows[1]] for rows in reader if rows]    

f.close()
        
with f_out as outfile:
    for item in list_items:
        outfile.writelines(">"+item[0]+"\n"+item[1]+"\n")

outfile.close()
