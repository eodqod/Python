from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.naver.com"
# urlopen()으로 데이터 가져오기 --- (※1)
res = req.urlopen(url)
# BeautifulSoup으로 분석하기 --- (※2)
soup = BeautifulSoup(res, "html.parser")
# 원하는 데이터 추출하기 --- (※3)
# find_all() 메서드로 추출하기 --- (※2)
links = soup.find_all("a")
# 링크 목록 출력하기 --- (※3)
for a in links:
    href = a.attrs['href']
    text = a.string
    if not href.startswith("#"):
        print(text, ">", href)