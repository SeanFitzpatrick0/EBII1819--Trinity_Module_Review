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
table = soup.find('table')
tableText = table.text.replace('\n\n', '\n')
print(tableText.split('\n'))
'''
for row in tableText.split('\n'):
    print(row) 

    #print('Code: %s, Name: %s, ECTS: %s' % (code, name, ects))
'''

#print('--- Collecting Module data {0:3.1f} seconds ---'.format((time.time() - link_time)))

print('Finished\tTotal Time:{0:3.1f} seconds'.format((time.time() - start_time)))