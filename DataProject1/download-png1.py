'''
웹 사이트의 데이터를 추출하기 위해서 urllib 라이브러리를 사용합니다.
http, ftp 상의 데이터를 쉽게 다운로드 가능하다.
urllib 라이브러리는 url에 관계된 모듈을 모아 놓은 패키지이다.
'''

# 라이브러리 읽어 들이기 --- (※1)
import urllib.request
# URL과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"
# 다운로드 --- (※2)
urllib.request.urlretrieve(url, savename)
print("저장되었습니다...!")
