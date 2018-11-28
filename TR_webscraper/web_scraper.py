import re
import time
import string
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

''' 1. Go to My TCD login   '''
driver = webdriver.Chrome()
driver.get("https://my.tcd.ie/urd/sits.urd/run/siw_lgn")
assert 'Log in to the portal' in driver.title

''' 2. Sign into profile    '''
usernameFeild = driver.find_element_by_id('MUA_CODE.DUMMY.MENSYS')
passwordFeild = driver.find_element_by_id('PASSWORD.DUMMY.MENSYS')
loginButton = driver.find_element_by_name('BP101.DUMMY_B.MENSYS.1')
login = input('Test User Enter: <userName> <password>\t')
uName, passW = login.split(' ')
usernameFeild.send_keys(uName)
passwordFeild.send_keys(passW)
fileName = input('Enter name of Output file:')
loginButton.click()
assert 'e:Vision Portal' in driver.title

''' 3. Go to Module Search page '''
moduleSearchEle = driver.find_element_by_id('smPMANCAM_01')
moduleSearchLink = moduleSearchEle.get_attribute('href')
driver.get(moduleSearchLink)
assert 'sitsportalpagetitle' in driver.page_source

''' 4. Need to manually select a school '''
#wait till on modules page
element = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'sv-form-pagination'))
)

''' 5. Select all the deatils links of modules '''
numberOfPages = driver.find_element_by_class_name('sv-form-pagination-rec-count').text
numberOfPages = int(numberOfPages.split('of ')[-1])

detailLinks = []

for i in range (numberOfPages - 1):
    pageLinks = driver.find_elements_by_partial_link_text('Detail')
    pageLinks = [link.get_attribute('href') for link in pageLinks]
    
    detailLinks += pageLinks

    nextPageLink = driver.find_element_by_partial_link_text('Next').get_attribute('href')
    driver.get(nextPageLink)

''' 6. visit module link and scrape data '''
df = pd.DataFrame(columns=['code', 'name', 'lecturer', 'description', 'ects'])

for link in detailLinks:
    try:
        #go to page 
        driver.get(link) 
        #get the data
        data = driver.find_elements_by_class_name('data1')
        code = data[0].text.strip()
        name = data[1].text.strip().title()
        lecturer = data[6].text
        removePattern = re.compile('(|^)(dr\.|dr|pr\.|pr|prof.|prof|Assistant|Associate|Lecturer|Professor|mr.|mr|Lecturing|staff|and|Lecturer\(s\)|Lecturers|tutorials|Module|Coordinators|owner|Co-ordinator|Teaching|-|/|:)( |$)',re.IGNORECASE)
        repeat = True
        oldval = lecturer
        while(repeat):
            lecturer = (re.sub(removePattern,'', lecturer)).strip()

            if lecturer == oldval:
                repeat = False
            oldval = lecturer
        lecturer = ' '.join(lecturer.strip().split()[0:2])

        whitespace_except_space = string.whitespace.replace(' ', '')
        description = 'Learning Outcomes:\n%s\nModule Learning Aims:\n%s\nModule Content:\n%s\n' % (
            data[7].text.strip(whitespace_except_space), data[8].text.strip(whitespace_except_space), data[9].text.strip(whitespace_except_space))
        description = re.sub(r'  ', ' ', description) 
        description = re.sub('\n\n', '\n', description) 
        ects = int(data[3].text.strip())

        df = df.append({'code':code, 'name':name, 'lecturer':lecturer, 'description':description, 'ects':ects}, ignore_index=True)
    except:
        print('ERROR: error while getting module details')
        continue
    
driver.close()    

print('Writing data to file:')
df.to_csv('./module_data/' + fileName, index=False)
print('Output written to ./module_data/' + fileName)
print(df)








