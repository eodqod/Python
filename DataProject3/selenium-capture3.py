from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://www.naver.com/"
# 드라이버를 로드한다.
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
# 화면을 최대화 한다.
driver.maximize_window()
# 읽는다.
driver.get(url)

# 화면을 캡처해서 저장하기
e = driver.find_element(By.CLASS_NAME('logo_naver'))
print(str(e))

# 브라우저 종료하기
driver.quit()

