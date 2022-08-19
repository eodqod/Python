"""
기상청 1개월 전망
https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20220811.xml

위의 내용을 읽어서
summary
weather_forecast
위 두가지만 출력해 보세요
"""
from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20220811.xml"

response = urlopen(url).read()
print(response)
tree = ET.fromstring(response)
# ET.dump(tree)

# print(tree[0])
# print(tree[0][6])
# print(tree[0][6][5])
# print(tree[0][6][5][1][0])
# print("*" * 80)
# print(tree[0][6][5][1][0].text.strip())
# print(tree[0][6][5][1][0].text.strip().split("○"))
# print(len(tree[0][6][5][1][0].text.strip().split("○")))
print("*" * 80)

for s in tree[0][6][5][1][0].text.strip().split("○"):
    if len(s) > 0:
        print(s)
print("*" * 80)

# print(tree[0][6][5][1][1])
print("*" * 80)
for child in tree[0][6][5][1][1]:
    print(child[0].text)
    print("-" * 100)
    print(child[1].text.strip().replace("<br> ","\n"))
    print("=" * 100)
