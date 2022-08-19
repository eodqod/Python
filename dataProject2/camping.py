import urllib.request

from bs4 import BeautifulSoup
import urllib.request as req
from urllib import parse
import datetime

url="https://www.campingtalk.me/booking/camp/2654"
# print(url)
# urlopen()으로 데이터 가져오기
res = req.urlopen(url)
# BeautifulSoup으로 분석하기
soup = BeautifulSoup(res, "html.parser")

images = soup.select("img")
# print(len(images), '개')
i=1
for img in images:
    try:
        # print(img.attrs['src'])
        url = img.attrs['src']
        file_name = "{:03d}.png".format(i)
        i += 1
        urllib.request.urlretrieve(url, file_name)
        print(file_name, '저장완료!!!')
    except:
        pass

