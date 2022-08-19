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
# driver.implicitly_wait(500)

# CSS 선택자로 찾아라!!!
# map = driver.find_element(by=By.CSS_SELECTOR, value="div.s_map")
# print(map)
# map.screenshot('map.png')
map_l = driver.find_element(by=By.CSS_SELECTOR, value="p.map_l")
map_r = driver.find_element(by=By.CSS_SELECTOR, value="p.map_r")
map_l.screenshot("map_l.png")
map_r.screenshot("map_r.png")


# 4. 부라우져 닫기
driver.quit()