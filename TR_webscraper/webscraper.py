#Imports===========================================
from bs4 import BeautifulSoup
import requests

#Program===========================================
'''
First attempt to get simple information(Codes and Names) from IT services email list
(https://www.tcd.ie/itservices/email/kb/modules.php)
'''
#Enter a website to extract the URL's from: 
r  = requests.get('http://www.tcd.ie/itservices/email/kb/modules.php')
data = r.text
soup = BeautifulSoup(data, 'html.parser')

for row in soup.find_all('tr'):
    print(row.text.strip())

