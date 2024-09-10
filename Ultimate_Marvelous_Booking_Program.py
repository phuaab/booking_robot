#!/usr/bin/env python
# coding: utf-8

# ### Navigation Menu Installation

# In[1]:


#    ！pip install jupyter_contrib_nbextensions


# In[2]:


#pip install jupyter_nbextensions_configurator


# In[3]:


# !jupyter contrib nbextension install --user


# In[4]:


# !jupyter nbextensions_configurator enable --user


# ### Installation for necessary packages

# In[100]:


import unittest


# In[101]:




# In[102]:


# get_ipython().system('pip install webdriver_manager selenium')


# In[138]:

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time


# In[139]:


import time


# In[140]:


import datetime


# In[141]:


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service


url = 'https://fitness-booking.hkust.edu.hk/'
def dosth():
    print ('start')
    print (time.strftime('%Y-%m-%d %H:%M:%S'),time.localtime(time.time()))    

    #hang on logging into account 
    option = webdriver.ChromeOptions()
    option.add_argument(r'--user-data-dir=C:\Users\Peng Hua\AppData\Local\Google\Chrome\User Data\Profile 1')
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(driver_path,options=option)
    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()


    # In[144]:


    #body > div.dialog-off-canvas-main-canvas > div > main > div > div > div.login-wrapper > div.cas > p:nth-child(3) > a
    driver.find_element_by_css_selector(".login-wrapper a").click()


    # ### Input student name and psw

    # In[145]:


    usrname = "####"
    psw = "######"
    #tilesHolder > div.tile-container > div > div.table > div > div.table-cell.text-left.content > div
    driver.find_element_by_css_selector("#tilesHolder > div.tile-container > div > div.table > div > div.table-cell.text-left.content > div").click()
    # driver.find_element_by_id("userNameInput").send_keys(usrname)
    driver.implicitly_wait(10)
    driver.find_element_by_id("i0118").send_keys(psw)
    driver.implicitly_wait(10)
    driver.find_element_by_id("idSIButton9").click()
    driver.implicitly_wait(10)


    # In[146]:


    #body > div.dialog-off-canvas-main-canvas > div > main > div > div > div.facility-list-wrapper > div > ul > li:nth-child(2) > a
    driver.find_element_by_css_selector(".facility-list-wrapper a").click()
    time.sleep(2)
        
        


    # In[147]:


    #popup-buttons > button.agree-button.eu-cookie-compliance-secondary-button
    try:
        driver.find_element_by_css_selector("button.agree-button.eu-cookie-compliance-secondary-button").click()
        time.sleep(3)
        driver.implicitly_wait(10)
    except:
        pass

    # In[148]:


    ### Choosing date of next week

    #calendar > div.fc-view-container > div > table > tbody > tr > td > div > div > div:nth-child(6) > div.fc-content-skeleton > table > thead > tr > td.fc-day-top.fc-sun.fc-future > span
    #<span class="fc-day-number">31</span>
    #calendar > div.fc-view-container > div > table > tbody > tr > td > div > div > div:nth-child(1) > div.fc-content-skeleton > table > thead > tr > td.fc-day-top.fc-mon.fc-today > span

    #driver.find_element_by_css_selector(".fc-view-container div:nth-child(6) span").click()
    aa = driver.find_element_by_class_name("fc-day-number").text 
    print(aa)

    #//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[2]/table/thead/tr/td[4]/span
    # bb = driver.find_element_by_xpath("//span[@class='fc-day-number' and text()='26']").text
    # print(bb)

    cc = driver.find_elements_by_xpath("//span[@class='fc-day-number']")
    i=0
    driver.implicitly_wait(10)

    ### Fix Bug
    try:
        driver.find_element_by_css_selector("button.agree-button.eu-cookie-compliance-secondary-button").click()
        time.sleep(3)
        driver.implicitly_wait(10)
    except:
        pass

    for delement in cc:
        date = delement.text
        print(date)
        i=i+1
        print(i)
        driver.implicitly_wait(10)

    while i == 8:
        try:
            delement.click()
            driver.implicitly_wait(10)
            i = 0
        except:
            pass

        


    #driver.find_element_by_xpath("//span[@class='fc-day-number' and text()='26']").click()


    #driver.find_element_by_class_name("fc-day-top fc-mon fc-other-month fc-today ").send_keys('2021-11-01').click()
    # date = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    # print(date)
    # driver.implicitly_wait(10)


    # ### Free Weight Training Booking 8pm till 8:45pm

    # In[150]:


    #taxonomy-term-398 > div > div.section-break.layout.layout--hkust-onecol.layout--hkust-7525 > div > div > div.layout__region.layout__region--first.col-md-9 > div > div > div > table > tbody > tr:nth-child(14) > td:nth-child(2) > a

    p1 = driver.find_element_by_css_selector("tr:nth-child(14) td:nth-child(2)").text
    while p1 != 'HUA, Peng' and p1 !='Full':
        driver.refresh()
        time.sleep(2)
        try: 
            driver.find_element_by_css_selector("tr:nth-child(14) td:nth-child(2) a").click()
            #tablesaw-7511 > tbody > tr:nth-child(7) > td:nth-child(2) > span > a
            #tablesaw-7511 > tbody > tr:nth-child(15) > td:nth-child(2) > span > div  ****if that is full, then it would be div***
            time.sleep(2)
            driver.find_element_by_css_selector("#edit-submit").click()
            time.sleep(2)
            p1 = driver.find_element_by_css_selector("tr:nth-child(14) td:nth-child(2)").text
        except:
            pass


    # ### Inner Room Booking 9pm till 9:45pm

    # In[152]:

    time.sleep(3)
    p2 = driver.find_element_by_css_selector("tr:nth-child(15) td:nth-child(4)").text
    while p2 != 'HUA, Peng' and p1 !='Full':
        driver.refresh()
        time.sleep(2)    
        try: 
            driver.find_element_by_css_selector("tr:nth-child(15) td:nth-child(4) a").click()
            time.sleep(2)
            driver.find_element_by_css_selector("#edit-submit").click()
            time.sleep(2)
            p2 = driver.find_element_by_css_selector("tr:nth-child(15) td:nth-child(4)").text
        except:
            pass

    # ### Main code

    # In[73]:
    time.sleep(2)
    driver.implicitly_wait(10)
    driver.close()


def main(h,m,s):
    while True:
        now = datetime.datetime.now()   
        print(now)
        if now.hour == h and now.minute == m and now.second == s:
            dosth()
        time.sleep(1)
main(1,9,5)




# In[ ]:




