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
f = open(r"/Users/ain/pythontest/data.csv", 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)

#메뉴 클릭 및 back, 이메일 주소 가져오기

for i in range(3):
    time.sleep(2)

    for number in range(1, 2) :
        element = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[' + str(number) + ']/div')
        element.click()

        #정보 가져오기
        try:
            name = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div[2]').text
            link = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[2]/div[2]/a').text
            print(name, link)
            csvWriter.writerow([name, link])
        except:
            print('데이터가 없습니다')
        
        time.sleep(2)

        browser.execute_script("window.history.go(-1)")
        time.sleep(2)
    
    #다음 페이지 클릭
    nextpage = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div/button[7]')
    nextpage.click()

    
#파일 끄기 
f.close()