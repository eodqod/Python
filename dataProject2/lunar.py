from bs4 import BeautifulSoup
import urllib.request as req
from urllib import parse
import datetime

today = datetime.datetime.now()
# print(today)
# print(today.year, "년", today.month, "월", today.day, "일")
# print(today.hour, "시", today.minute, "분", today.second, "초")
# print("https://astro.kasi.re.kr/life/pageView/5?search_year={:04d}&search_month={:02d}&search_check=G".format(today.year, today.month))
url="https://astro.kasi.re.kr/life/pageView/5?search_year={:04d}&search_month={:02d}&search_check=G".format(today.year, today.month)
# print(url)
# urlopen()으로 데이터 가져오기
res = req.urlopen(url)
# BeautifulSoup으로 분석하기
soup = BeautifulSoup(res, "html.parser")

#print(soup.find("title").string.rstrip().lstrip())

table  = soup.select("div table")
# print(len(table), "개")
trs = table[0].select("tbody tr")
# print(len(trs), "개")
for tr in trs:
    td = tr.select("td")
    # print(len(td), "개")
    print(td[0].string, "[" + td[1].string + "]", "[" + td[2].string + "]")

print("*" * 100)

for tr in soup.select("div table tbody tr"):
    td = tr.select("td")
    print(td[0].string, "[" + td[1].string + "]", "[" + td[2].string + "]")
