# 오늘의 과제
# 영화진흥공사 XML파일을 읽어서 박스오피스 결과를 출력하는 프로그램을 만드시오
import xml.etree.ElementTree as ET
import requests

url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888"

year = int(input('연도 : '))
month = int(input('월 : '))
date = int(input('일 : '))
# year = 2022
# month = 8
# date = 1
# 날짜를 원하는 모양으로 만든다.
# print("{:04d}{:02d}{:02d}".format(year, month, date))
targetDt = "{:04d}{:02d}{:02d}".format(year, month, date)
# print(targetDt)

url += "&targetDt=" + targetDt

# 데이터 가져오기
r = requests.get(url)
# print(r)

tree = ET.fromstring(r.text)
# print(tree)
# ET.dump(tree)

print("*" * 50)
print(tree.find("boxofficeType").text , "(",tree.find("showRange").text,")", sep="")
print("*" * 50)
# print(tree.find("weeklyBoxOfficeList"))
weeklyBoxOfficeList = tree.find("dailyBoxOfficeList")
weeklyBoxOffice = weeklyBoxOfficeList.findall("dailyBoxOffice")
# print(len(weeklyBoxOffice))
for m in weeklyBoxOffice:
    print(m.find("rank").text, ". ", sep="", end="")
    print(m.find("movieNm").text, "(", sep="", end="")
    print(m.find("openDt").text, ")", sep="", end="")
    print()
print("=" * 100)