"""
동네예보 > 중기예보 > 전국
http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108

위의 내용을 읽어서
summary
weather_forecast
위 두가지만 출력해 보세요
"""
from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

response = urlopen(url).read()
# print(response)
tree = ET.fromstring(response)
# ET.dump(tree)

# print(tree[0])
# print(tree[0][6])
# print(tree[0][6][5])
# print(tree[0][6][5][0])
# print(tree[0][6][5][1])
# print("*" * 80)
# print(tree[0][6][5][0][2])
# print(tree[0][6][5][0][2].text)
# print(tree[0][6][5][0][2].text.replace("<br />","\n").replace("<br />","\n"))
print("*" * 150)
wf = tree[0][6][5][0][2].text
print(wf.replace(".",". ").replace("○"," ○").replace("<br />","\n").strip())
print("*" * 150)
locations = tree[0][6][5][1].findall("location")
print(len(locations), "개 지역")
for location in locations:
    # print(location.get('wl_ver'))
    # print(location[0].text)
    print(location.find("province").text, " - ", location.find('city').text, sep='')
    print("-" * 50)
    for d in location.findall('data'):
        print(d.find('tmEf').text + "(" + d.find('wf').text + ") : " + d.find('tmn').text + "~" +  d.find('tmx').text)
    print("=" * 50)
