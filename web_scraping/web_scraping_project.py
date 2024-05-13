# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time


from selenium import webdriver

# Specify the path to the Chrome driver executable
chrome_driver_path = "C:/Users/LENOVO/.spyder-py3/chromedriver-win64/chromedriver.exe"

# Initialize Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("webdriver.chrome.driver=" + chrome_driver_path)

# Initialize the Chrome driver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get('https://www.naukri.com/')
input_search=driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[1]/div/div/div[1]/div[1]/div/input')
input_search.send_keys('Web Scraping')
Button=driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[6]').click()


# len(posting)

df = pd.DataFrame(columns=['link', 'name', 'com_name', 'experience', 'salary', 'location'])

while True:
    soup=BeautifulSoup(driver.page_source,'lxml')
    posting=soup.find_all('div',class_= 'cust-job-tuple layout-wrapper lay-2 sjw__tuple')
    for post in posting:
        link = post.find('a', class_='title').get('href')
        name = post.find('a', class_='title').text
        com_name = post.find('a', class_='comp-name').text
        experience_elem = post.find('span', class_='expwdth')
        experience = experience_elem.text if experience_elem else ''
        
        salary_elem = post.find('span', class_='ni-job-tuple-icon ni-job-tuple-icon-srp-rupee sal')
        salary = salary_elem.text if salary_elem else ''
        
        location_elem = post.find('span', class_='locWdth')
        location = location_elem.text if location_elem else ''
     
        
        df = pd.concat([df, pd.DataFrame({'link': [link], 'name': [name], 'com_name': [com_name], 
                                          'experience': [experience], 'salary': [salary], 'location': [location]})], 
                       ignore_index=True)

    try:
        next_button=driver.find_element(By.CSS_SELECTOR,'#lastCompMark > a:nth-child(4)')
        next_button.click()
        time.sleep(2)

    except:
        pass
    
# Save DataFrame to CSV
df.to_csv('job_data.csv', index=False)     











    