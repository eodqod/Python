from selenium import webdriver

url = "http://www.naver.com/"
# 드라이버를 로드한다.
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
# 화면을 최대화 한다.
driver.maximize_window()
# 읽는다.
driver.get(url)

# 화면의 크기를 구해보자
size = driver.get_window_size()
print(size)
width = driver.execute_script('return document.body.parentNode.scrollWidth')
height = driver.execute_script('return document.body.parentNode.scrollHeight')
print(width, height)
# 크기 지정
driver.set_window_size(width, height)

# 화면을 캡처해서 저장하기
driver.save_screenshot("Website.png")
# 브라우저 종료하기
driver.quit()

