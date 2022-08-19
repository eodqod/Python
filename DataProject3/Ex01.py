from selenium import webdriver
from selenium.webdriver.chrome.options import Options
url = "http://www.naver.com/"

# 1. 옵션지정
options = Options()
# 2. 크롬드라이버를 로드하여 브라우저 열기
driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

# 3. 네이버를 접속해보자
driver.get(url)



# 4. 부라우져 닫기
driver.quit()