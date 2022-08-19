import json, pprint

# 읽기
data = json.load(open('actor_list.json'))

for index, people in enumerate(data):
    if people['roleName'] == '배우' and len(str(people['filmoNames']).split("|"))>3:
        print(index + 1, ". ", people['name'], "(", people['filmoNames'], ')', sep='')
