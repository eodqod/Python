from bs4 import BeautifulSoup 
import urllib.request as req
from urllib import parse

# 뒤의 인코딩 부분은 "저자:윤동주"라는 의미입니다.
# 따로 입력하지 말고 위키 문헌 홈페이지에 들어간 뒤에 주소를 복사해서 사용하세요.

name = "윤동주"
name = "김소월"

url = "https://ko.wikisource.org/wiki/" + parse.quote("저자:"+name)
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
print("{} 작가의 저작물".format(name))
print("-" * 100)
toc = soup.select("h3 > span.mw-headline")
ul = soup.select("h3+ul")
for i in range(len(toc)):
    print("[" + toc[i].string + "]")
    li = ul[i].select("li")
    for item in li:
        print("   -", item.select_one("a").text)
print("-" * 100)
