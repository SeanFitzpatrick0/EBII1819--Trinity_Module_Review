#Imports===========================================
import requests
import time
import re
import pandas as pd
from bs4 import BeautifulSoup

#Program===========================================
#===============================================================================
# TIMING
#===============================================================================
start_time = time.time()
print('Start')
print('--- {0:3.1f} seconds ---'.format((time.time() - start_time)))
#===============================================================================
'''
1st: Gather all the links to the different schools module descriptor pages
From the TCD module directory (https://www.tcd.ie/itservices/email/kb/modules.php?fbclid=IwAR2_sfkIQqtSbzphvn2CsbWFpsro577RbGyrm9s1ijz15RZsNSBGtMJp9gE) 
'''
#Enter a website to extract the URL's from:
url = 'https://' + 'www.tcd.ie/itservices/email/kb/modules.php?fbclid=IwAR2_sfkIQqtSbzphvn2CsbWFpsro577RbGyrm9s1ijz15RZsNSBGtMJp9gE' 
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

#==========TEST================
codes = re.findall(r'<td width="193">(.*)<\/td>', data)[0: -1]
names = re.findall(r'<td>(.*)<\/td>', data)

#Remove error in data
del codes[3253]
del names[-1]

df = pd.DataFrame(
    {'code': codes,
     'name': names,
    })
df['lecturer'] = df['code']
df['description'] = df['code']
df['ects'] = 0
print(df)

#Clean data
#remove unwanted char
df['name'] = df['name'].str.replace(r'[^a-zA-Z0-9, ]','').str.strip()

df.to_csv('ModuleData(Codes_Names).csv', index=False)