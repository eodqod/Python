import json, pprint

# 읽기
data = json.load(open('list3.json'))

# 이쁘게 찍기
pprint.pprint(data)
print("*" * 100)

