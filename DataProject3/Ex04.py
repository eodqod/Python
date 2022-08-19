from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "http://www.event-tv.co.kr/core/newsninfo/festivarbooklet"

# 1. 옵션지정
options = Options()
# 2. 크롬드라이버를 로드하여 브라우저 열기
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# 3. 네이버를 접속해보자
driver.get(url)

# 잠시 기다려라!!!
driver.implicitly_wait(500)

# 아이디로 찾아라!!!
content = driver.find_element(by=By.ID, value="content")
# print(content)
# 찾은것 중에서 태그명으로 찾아라
title = content.find_element(By.TAG_NAME, value='h2')
print(title.text)

# 화면 일부분을 저장해 보자!!!
content.screenshot('divimg.png')

# 4. 부라우져 닫기
driver.quit()