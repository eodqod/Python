import json, pprint

# 읽기
data = json.load(open('people_list.json'))

# 내가 목록을 출력
actor_list = []
for index, people in enumerate(data):
    if people['roleName'] == '배우':
        print(index + 1, ". ", people['name'], "(", people['roleName'], ')', sep='')
        actor_list.append(people)

print(len(actor_list), "명")

with open("actor_list.json", 'w') as outfile:
    json.dump(actor_list, outfile)