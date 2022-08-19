# 전체 영화인 목록 중에서 배우만 찾아서 json으로 변환하여 저장하는 프로그램 작성
import json
import xml.etree.ElementTree as ET
import requests

url = "http://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.xml?key=f5eef3421c602c6cb7ea224104795888"
itemPerPage = "&itemPerPage=100"
curPage = "&curPage="

# 데이터 가져오기
r = requests.get(url)
# print(r)

tree = ET.fromstring(r.text)
# print(tree)
ET.dump(tree)

total_count = tree.find("totCnt").text
print("전체 인원 : " + total_count + "명")
total_page = (int(total_count)-1)//100 + 1
print("전체 페이지수 : " + str(total_page) + "페이지")
people_list = []
for i in range(1, total_page+1):
    address = url + itemPerPage + curPage + str(i)
    print(address)
    r = requests.get(address)
    tree = ET.fromstring(r.text)
    peopleList = tree.find("peopleList")
    pList = peopleList.findall("people")
    for p in pList:
        people = {}
        try:
            people['id'] = p.find("peopleCd").text
            people['name'] = p.find("peopleNm").text
            people['roleName'] = p.find("repRoleNm").text
            people['filmoNames'] = p.find("filmoNames").text
            print(people)
        except Exception:
            pass
        people_list.append(people)
        print("-" * 50)

with open("people_list.json", 'w') as outfile:
    json.dump(people_list, outfile)

