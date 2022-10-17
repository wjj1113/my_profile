from time import time
from webbrowser import BaseBrowser
from selenium import webdriver
import selenium
import csv
import time
from selenium.webdriver.common.by import By
import pandas as pd
import os as o
import jinja2

#브라우저 생성
browser = webdriver.Chrome('chromedriver')

#csv에 있는 List 링크 가져오기
df = pd.read_csv('data.csv', encoding='utf-8')
df.columns = ['이름', '링크']
link_name = df['링크']
val_list = link_name.values.tolist()

#파일 생성
f = open(r"/Users/ain/pythontest/data.csv", 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)

#링크 열기
for i in range(1000):
    link = val_list[i]
    browser.get(link)

    try:
        name = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div[2]').text
        link = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[2]/div[2]/a').text
        print(name, link)
        csvWriter.writerow([name, link])
    except:
        print('데이터가 없습니다')
        csvWriter.writerow('xx')

    time.sleep(2)

#파일 끄기 
f.close()