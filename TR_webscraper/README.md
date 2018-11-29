## Web Scraper
This directory contains the websraper use to gather details on TCD modules.
Information on these module is gathered from the MyTCD Student Portal.
This application makes use of a webdriver to navigate to MyTCD and log in. 
You will be brought to the module search page. Here you must manullay select a school to search and the scraper will then take over and collect all details on the modules in that school. The details gathered will be wrote to a csv file in the **module_data** folder with the name you provided.

Make sure you have installed all needed modules.

### Usage
To use the webscraper navigate to **TR_webscraper** and run **web_scraper.py**.
```
cd TR_webscraper
python web_scraper.py
```
You will be nagivated to the Courses & Modules page. From here you must manually click the View Module Descriptive Details link. You will be brought to a search form. From here select a school for the Faculty/School drop down (E.g. Computer Science and Statistics) and click View Modules.

The webscraper will then take over and select all the module details links and then collect all details from these pages.

### Demo
![](webscraper_demo.gif)
