import selenium
import numpy as np
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
with open("webframes.txt", "r") as f:
    lines = f.readlines()
for i,v in enumerate(lines):
    lines[i] = v.replace("\\n","\n")
    print(f"Converting frame {i}")
site = input("Enter site here:")
driver = webdriver.Chrome()
if(site.startswith("https://")):
    driver.get(site)
else:
    driver.get(f"https://{site}")
paragraphs = driver.find_elements(By.TAG_NAME, 'p')
chars = ''
for i in paragraphs:
    chars += i.text
chars.replace('\n','&nbsp;').replace(' ','&nbsp;')
chars = 2*chars
for line in lines:
    output = ""
    charnum = 0
    for i in line:
        if(i == "1"):
            output += chars[charnum]    
            charnum += 1
        elif(i == "0"):
            output += "&nbsp;"
        elif(i == "\n"):
            output += chars[charnum]
            charnum += 1
            output += "</br>"
            output += chars[charnum]
            charnum += 1
    # print(output)                                                                             
    driver.execute_script("arguments[0].innerHTML = arguments[1]; arguments[0].style.fontFamily = 'Consolas'",paragraphs[4],output)
    time.sleep(1/44)
time.sleep(100)
driver.close()

