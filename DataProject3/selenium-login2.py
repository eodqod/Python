# 네이버 로그인 절차가 강화되어 자동입력 방지문자(Captcha)를 입력해야 로그인할 수 있습니다.
# 따라서 파이썬 셸이나 주피터 노트북(5-3절에서 설명)에서 비밀번호 입력까지만 실행하고
# 자동입력 방지문자는 브라우저 창에서 수작업으로 입력 후 나머지 코드를 이어서 실행하시기 바랍니다.

# Step 1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
#지정한 user-agent로 설정합니다.
user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
options.add_argument('user-agent=' + user_agent)

# options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
# options.add_argument('--window-size= x, y') #실행되는 브라우저 크기를 지정할 수 있습니다.
# options.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
# options.add_argument('--start-fullscreen') #브라우저가 풀스크린 모드(F11)로 실행됩니다.
# options.add_argument('--blink-settings=imagesEnabled=false') #브라우저에서 이미지 로딩을 하지 않습니다.
# options.add_argument('--mute-audio') #브라우저에 음소거 옵션을 적용합니다.
# options.add_argument('incognito') #시크릿 모드의 브라우저가 실행됩니다.

USER = "<아이디>"
PASS = "<비밀번호>"

browser = webdriver.Chrome(options=options)

# 로그인 페이지에 접근하기 --- (※2)
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

# 텍스트 박스에 아이디와 비밀번호 입력하기 --- (※3)
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

########################################################
# Step 2
# 브라우저 창에서 자동입력 방지문자를 입력해주세요.


########################################################
# Step 3

# 입력 양식 전송해서 로그인하기 --- (※4)
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")

# 쇼핑 페이지의 데이터 가져오기 --- (※5)
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

# 쇼핑 목록 출력하기 --- (※6)
products = browser.find_elements_by_css_selector(".name")
print(products)
for product in products:
  print("-", product.text)
