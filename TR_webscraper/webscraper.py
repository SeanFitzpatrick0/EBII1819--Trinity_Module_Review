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
From the TCD module directory (https://www.tcd.ie/itservices/email/kb/modules.php?fbclid=IwAR3l0ULSE7tBORsoS29efSkzoeAx1ZdrrQNrZN4Cp1ykq0190kYnpwivYig) 
'''
#Enter a website to extract the URL's from:
url = 'https://' + 'www.tcd.ie/itservices/email/kb/modules.php?fbclid=IwAR3l0ULSE7tBORsoS29efSkzoeAx1ZdrrQNrZN4Cp1ykq0190kYnpwivYig' 
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
links = dict()

#Collects links
##for link in soup.find_all('a'):
    #print(link.text, link.get('href'))
    #links[link.text.strip(r'(^ )(.php)')] = url + link.get('href')

#link_time = time.time()
##print('--- Collecting Links {0:3.1f} seconds ---'.format((time.time() - start_time)))

#Remove exceptions
#del links['Parent Directory']
#del links['ModuleEnrolmentTemplate']
#del links['Single Semester Students (for Biochemistery, Immunology & Molecular Medicine']

'''
2nd: Go to each link and links and scrape all of the descriptors
on that page. 
'''

for key, value in links.items():
    ###r = requests.get(value)
    ##if(r is None):
        #print('ERRROR: request failed')
        #break
    #data = r.text
    #Not in correct format
    #if('For information on modules and courses please see' in data):
        #print('Error %s modules are not in the correct format.' % (key))
    #else:
    soup = BeautifulSoup(data, 'html.parser')
    for table in soup.find_all('table'):
        if('ECTS credits' in table.text):
            #Get code & name
            moduleData = table.find_all('tr')[1].find_all('td')
            item = moduleData[0].text
            item = re.search(r'\((.*)\)', item).group(1)
            item = re.sub(r'[\(\)]', ' ', item)
            item = re.sub(r'  ', ' ', item).strip()

            code = item.split(' ')[-1]
            name = re.sub(code, '', item).strip()
                
            #Get ECTS
            ects = re.search(r'\d{1,2}', moduleData[1].text).group(0)
                
            print('Code: %s, Name: %s, ECTS: %s' % (code, name, ects))


print('--- Collecting Module data {0:3.1f} seconds ---'.format((time.time() - link_time)))

print('Finished\tTotal Time:{0:3.1f} seconds'.format((time.time() - start_time)))