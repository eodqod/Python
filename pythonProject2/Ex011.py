# 딕셔너리 자료형 : 자바의 맵과 비슷
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(type(dic), ":", dic)

print(dic['name'])
print(dic['phone'])
print(dic['birth'])

dic['gender'] = '남자'  # 추가
print(type(dic), ":", dic)

del dic['birth']
print(dic)

print(list(dic.keys()))     # 키를 리스트로
print(list(dic.values()))   # 값을 리스트로

for key in dic.keys():      # 키 반복
    print(key)

for key, value in dic.items() :      # 키, 값 반복
    print(key, " : ", value)

print(dic.get('birth'))                 # none
print(dic.get('birth', '2022-11-01'))   # 없을 경우 기본값 지정