import json, pprint

# 읽기
data = json.load(open('list.json'))

# 이쁘게 찍기
pprint.pprint(data)
print("*" * 100)

# 그냥 찍기
print(data)
print("*" * 100)

# 내가 목록을 출력
for index, book in enumerate(data):
    print(index+1, ". ", book['text'], "(", book['url'], ')', sep='')

