from time import time
from webbrowser import BaseBrowser
from selenium import webdriver
import selenium
import csv
import time
from selenium.webdriver.common.by import By

#브라우저 생성
browser = webdriver.Chrome('chromedriver')

#웹사이트 열기
browser.get('https://event-us.kr/search/channel')
browser.implicitly_wait(10)

#파일 생성
f = open(r"/Users/ain/pythontest/data.xlsx", 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)

#메뉴 클릭 및 back, 이메일 주소 가져오기
# 현재 데이터를 클릭해서 넘기면 다시 돌아올 때, 1페이지로 돌아오기 때문에, 전체의 url을 다 가져와서 해당 url에서 크롤링해오기

for i in range(999):
    time.sleep(2)

    for number in range(1, 9) :
        #정보 가져오기
        try:
            name = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[' + str(number) + ']/div/div[1]/a/div[2]/div[1]').text
            link = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[' + str(number) + ']/div/div[1]/a').get_attribute('href')
            print(name, link)
            csvWriter.writerow([name, link])
        except:
            print('데이터가 없습니다')

        time.sleep(2)
    
    #다음 페이지 클릭
    nextpage = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div/button[7]')
    nextpage.click()

    
#파일 끄기 
f.close()