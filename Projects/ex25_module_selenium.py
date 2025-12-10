# 사람이 하던 웹 브라우저의 행동을 파이썬 프로그램이 대신 수행 하도록 자동화 해주는 모듈.selenium

#  외부모듈이니 설치필요 pip install selenium

import time

from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get('https://www.naver.com')

time.sleep(5)

#검색어 입력창에 '스타벅스' 글씨 입력하기. 
search_input= driver.find_element(By.CLASS_NAME, 'search_input')

#input 요소에 키보드 값 입력 기능

search_input.send_keys('스타벅스')

time.sleep(5)

#검색 버튼 클릭을 자동화
search_button = driver.find_element(By.ID, 'search-btn')

#그 버튼 클릭 이벤트 발동
search_button.click()


time.sleep(5)






#driver.quit()