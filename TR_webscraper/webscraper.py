#Imports===========================================
from bs4 import BeautifulSoup
import requests

#Program===========================================
'''
1st: Gather all the links to the different schools module descriptor pages
From the TCD module directory (https://www.tcd.ie/students/orientation/visiting-exchange/module-directory/) 
'''
#Enter a website to extract the URL's from:
url = 'https://' + 'www.tcd.ie/students/orientation/visiting-exchange/module-directory/' 
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
links = dict()

#Collects links
for link in soup.find_all('a'):
    #print(link.text, link.get('href'))
    links[link.text.strip(r'.php')] = url + link.get('href')

'''
2nd: Go to each link and links and scrape all of the descriptors
on that page. 
'''
