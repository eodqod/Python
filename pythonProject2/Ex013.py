# 논리 자료형
a = True
b = False

print(a, b, type(a))

c = 1 == 1
print(type(c), ":", c)

a = [1,2,3]
b = a  # 얕은 복사 : 주소가 복사된다.
print(id(a), ":", a)
print(id(b), ":", b)
a[1] = 99
print(id(a), ":", a)
print(id(b), ":", b)  # 둘다 변경 : 참조형 변수다
print("-"*80)

c = a[:]  # 깊은 복사 : 값이 복사된다.
print(id(a), ":", a)
print(id(c), ":", c)
a[1] = 88
print(id(a), ":", a)
print(id(c), ":", c)  # 1개만 변경 : 깊은 복사다
print("-"*80)

d = a.copy()
print(id(a), ":", a)
print(id(d), ":", d)
a[1] = 77
print(id(a), ":", a)
print(id(d), ":", d)  # 1개만 변경 : 깊은 복사다
print("-"*80)

a, b = ('python', 'life')
print(id(a), ":", a)
print(id(b), ":", b)

[a, b] = ['python', 'life']
print(id(a), ":", a)
print(id(b), ":", b)

(a, b) = ['python', 'life']
print(id(a), ":", a)
print(id(b), ":", b)

a = b = 100
print(id(a), ":", a)
print(id(b), ":", b)

b = 200
a, b = b, a
print(id(a), ":", a)
print(id(b), ":", b)
