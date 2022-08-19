import urllib.request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# sir 메인 화면
url = "https://sir.kr/"

# 1. 옵션지정
options = Options()
options.add_argument("--start-maximized")  # 전체화면으로 실행
options.add_argument("--disable-popup-blocking") # 팝업창 무시
options.add_argument("--disable-default-apps")  # 기본앱 사용하지 않겠다.

# 2. 크롬드라이버를 로드하여 브라우저 열기
driver = webdriver.Chrome(service=Service(executable_path="./chromedriver.exe"), options=options)

# 3. sir를 접속해보자
driver.get(url)

# print(driver.title)  # title 태그 내용
# print(driver.page_source)  # 페이지 전체 소스

id_input = driver.find_element(by=By.ID, value="ol_id")
id_input.send_keys("ithuman")
# driver.execute_script("document.getElementById(\"id\").value=\"사용자아이디\";")

pw_input = driver.find_element(by=By.ID, value="ol_pw")
pw_input.send_keys("woaldjqtek2")
# driver.execute_script("document.getElementById(\"pw\").value=\"사용자비번\";")

btn = driver.find_element(by=By.ID, value="ol_submit")
btn.click()

member = driver.find_element(by=By.ID, value="tnb")
print(member.text)
print("*" * 80)
print(member.get_attribute("outerHTML"))

# 4. 부라우져 닫기
# driver.quit()


