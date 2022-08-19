import urllib.request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# https://movie.naver.com/ 에 접속하여
# 박스오피스에 있는 열화목록을 출력하는 프로그램을 작성하시오

url = "https://movie.naver.com/"

# 1. 옵션지정
options = Options()

# 2. 크롬드라이버를 로드하여 브라우저 열기
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# 3. 네이버를 접속해보자
driver.get(url)

# 잠시 기다려라!!!
driver.implicitly_wait(500)
# 타이틀 확인
print(driver.title)
print("*" * 80)

boxoffice_tab = driver.find_element(by=By.ID, value='BOXOFFICE_tab')
boxoffice_tab.click()

boxoffice_list = driver.find_elements(by=By.CSS_SELECTOR, value='#flick0 li')
print(len(boxoffice_list), "개")
print("*" * 80)

for i, m in enumerate(boxoffice_list):
      t = m.find_element(by=By.CSS_SELECTOR, value="span.rank em")
      # print(t.get_attribute("innerHTML"))
      # print(t.get_attribute("outerHTML"))
      item = m.find_element(by=By.CSS_SELECTOR, value="div a img")
      print(t.get_attribute("innerHTML"), ":", item.get_attribute('alt'))
      img_link = item.get_attribute('src')[:-10]
      print("이미지 :", img_link )
      bottom = m.find_element(by=By.CSS_SELECTOR, value='span.baseplate')
      print(bottom.text.split("\n")[0], ":", bottom.text.split("\n")[1])

      save_name = str(i+1) + ".jpg"
      urllib.request.urlretrieve(img_link, save_name)
      print(save_name + "!! 저장완료")
      print("-"  *  100)

# 4. 부라우져 닫기
driver.quit()