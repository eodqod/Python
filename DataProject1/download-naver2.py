import urllib.request
import urllib.parse
API = "https://search.naver.com/search.naver"
# 매개변수를 URL 인코딩합니다. --- (※1)
values = {
    'query' : 'JSP'
}

# dict 자료형을 url의 요청 정보 형태로 가공해준다.
params = urllib.parse.urlencode(values)
# print(params)

# 요청 전용 URL을 생성합니다. --- (※2)
url = API + "?" + params  # 주소뒤에 요청정보를 붙여준다.
# print("url=", url)

# 다운로드합니다. --- (※3)
data = urllib.request.urlopen(url).read()  # 연결하고 데이터를 읽는다.
text = data.decode("utf-8")   # 디코딩
print(text)   # 출력
