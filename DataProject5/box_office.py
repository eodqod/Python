# 영화 진흥위원회 OPEN API에서 지정 날짜의 박스오피스 순위를
# 출력하는 프로그램을 작성하시오

# 년월일을 입력받는다.
import json

import requests

year = int(input('연도 : '))
month = int(input('월 : '))
date = int(input('일 : '))

# 날짜를 원하는 모양으로 만든다.
# print("{:04d}{:02d}{:02d}".format(year, month, date))
targetDt = "{:04d}{:02d}{:02d}".format(year, month, date)
# print(targetDt)

# url을 만든다.
url = "https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"\
      "?key=f5eef3421c602c6cb7ea224104795888&targetDt=" + targetDt

# 데이터 가져오기
r = requests.get(url)
# print(r)

# json으로 변환
data = json.loads(r.text)  ## python은 dict타입
print(data)

# 출력
print("*" * 80)
print(data['boxOfficeResult']['boxofficeType'])
print(data['boxOfficeResult']['showRange'])
print("*" * 80)

dailyBoxOfficeList = data['boxOfficeResult']['dailyBoxOfficeList']
# print(type(dailyBoxOfficeList))
# print(len(dailyBoxOfficeList), "개")

for boxOffice in dailyBoxOfficeList:
    # print(boxOffice['rank'])
    # print(boxOffice['movieNm'])
    # print(boxOffice['openDt'])
    print("{:02d}위. {}(개봉일 : {})".format(int(boxOffice['rank']), boxOffice['movieNm'], boxOffice['openDt']))

print("*" * 80)
