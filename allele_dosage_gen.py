# -*- coding: utf-8 -*-
### Created on Wed Mar 22 10:58:48 2017

### @author: Deborah S-L 

import pandas as pd
import sys, getopt

### 
#folder = "D:\Uk Biobank\Genomics\Gen_Files\\"

## get argument passed from command line
argv=sys.argv[1:]
inputfile = ''
outputfile = ''
try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
  print('allele_dosage_gen.py -i <inputfile.gen> -o <.csv OR .txt OR .tsv>')
  sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('allele_dosage_gen.py -i <inputfile.gen> -o <.csv OR .txt OR .tsv>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputformat = arg

print(inputfile)
#print(inputfile.split('_SNPs_'))
[a,b] = inputfile.split('_SNPs_')
[RSID,x] = b.split('.')

outputfile = 'allele_dosage_'+RSID+outputformat
## import .gen file
#df = pd.read_csv(folder+'Gen_Files\subset_SNPs_rs10963811.gen', sep=' ', header=None)
df = pd.read_csv(inputfile,sep=' ', header=None)
info = df[df.columns[0:6]]
data = df[df.columns[6::]]

def number_ind(data):
    N = float(len(data.columns))/float(3)
    flag = N.is_integer()
    if flag:
        return int(N)
    else:
       raise TypeError('columns number mal-formatted')
        
N_ind = number_ind(data)
N = len(data.columns)

def extract_item(sub,k):
    return sub[sub.columns[k]][0]

## for each subject, measure allele dosage 
tmp = range(0,N,3)
cols = ['Allele_A','Allele_B']
df_new = pd.DataFrame(columns=cols)
for j in range(0,len(tmp)):
    i = range(tmp[j],tmp[j]+3)
    sub  = data[data.columns[i]]
    res = []
    tmpA = extract_item(sub,0)*2+extract_item(sub,1)
    tmpB = extract_item(sub,2)*2+extract_item(sub,1)
    df_new.loc[j]=[tmpA, tmpB]
    
df_new.to_csv(outputfile,sep=',')
    
        
