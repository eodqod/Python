#!/usr/bin/env python3
# 라이브러리를 읽어 들입니다. --- (※1)
import sys
import urllib.request as req
import urllib.parse as parse
# 명령줄 매개변수 추출 --- (※2)
# 명령행 인수에 지역코드 값을 받아서 처리한다.
# 명령행 인수에 지역코드 값이 없다면 사용법 출력
if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()  # 프로그램 종료

# 명령행 인수에 지역코드 값을 변수에 저장
regionNumber = sys.argv[1]

# 매개변수를 URL 인코딩합니다. --- (※3)
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = parse.urlencode(values)  # 쿼리 스트링을 완성
url = API + "?" + params
print("url=", url)
# 다운로드합니다. --- (※3)
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)