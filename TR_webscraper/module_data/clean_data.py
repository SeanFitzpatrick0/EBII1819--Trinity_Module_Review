import pandas as pd
from os import listdir
from os.path import isfile, join
files = [f for f in listdir('./') if isfile(join('./', f))]

if 'clean_data.py' in files: 
    files.remove('clean_data.py')

if 'fileNames.txt' in files: 
    files.remove('fileNames.txt')

for f in files:
    #read data
    df = pd.read_csv(f, ',')
    headers = list(df.columns.values)

    #remove commas
    df[headers] = df[headers].replace({',': ''}, regex=True)

    #write data back
    df.to_csv(f, sep=',',index=False)
