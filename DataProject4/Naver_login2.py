
# 네이버 로그인 주소
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://nid.naver.com/nidlogin.login"

# 1. 옵션지정
options = Options()
options.add_argument("--start-maximized")  # 전체화면으로 실행
options.add_argument("--disable-popup-blocking")  # 팝업창 무시
options.add_argument("--disable-default-apps")  # 기본앱 사용하지 않겠다.

# 2. 크롬드라이버를 로드하여 부라우저를 컨트롤할 준비
driver = webdriver.Chrome(service=Service(executable_path="./chromedriver.exe"), options=options)
# 화면을 최대화 해보자
# driver.maximize_window()

# 지정 주소에 접속
driver.get(url)

# 접속이 되었는지 확인부터 해보자!!!
# print(driver.title)  # title태그의 값을 가져온다. 
# print(driver.page_source)  # 페이지 전체 소스를 가져온다.

# 폼을 찾아 폼의 id와 password부분에 원하는 값을 넣어주고 로그인 버튼을 클릭하면 된다.
# 아이디를 찾아  아이디를 입력한다.
# id = driver.find_element(by=By.ID, value="id")
# id.send_keys("자신의 네이버아이디")

# 자바스크립트를 이용하여 id창에 아이디를 입력해보자
driver.execute_script("document.getElementById(\"id\").value=\"자신의 네이버 아이디\";")


#암호부분을 찾아 암호를 입력한다.
# pw = driver.find_element(by=By.ID, value="pw")
# pw.send_keys("자신의 네이버비번")
driver.execute_script("document.getElementById(\"pw\").value=\"자신의 네이버 비밀번호\";")

# 로그인 버튼을 찾아 클릭한다.
login_btn =  driver.find_element(by=By.ID, value="log.login")
login_btn.click()