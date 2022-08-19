from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "http://www.naver.com/"

# 1. 옵션지정
options = Options()
# 2. 크롬드라이버를 로드하여 브라우저 열기
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# 3. 네이버를 접속해보자
driver.get(url)

# 잠시 기다려라!!!
driver.implicitly_wait(1000)

# 이름으로 찾아라!!!
search_box = driver.find_element(by=By.NAME, value="query")
# print(search_box)
# 찾은 요소에 값 전달
search_box.send_keys("Selenium")

# 찾기 버튼을 찾아서 클릭해보자
# 찾기 버튼을 ID로 찾기
search_btn = driver.find_element(by=By.ID, value='search_btn')
# 버튼 클릭 이벤트 발생
search_btn.click()

value = driver.find_element(by=By.ID, value='nx_query').get_attribute('placeholder')
print(value)

# 4. 부라우져 닫기
driver.quit()