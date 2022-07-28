a, b, c = 80, 75, 55
print("평균 : ", (a+b+c)/3)

print("짝수" if 13%2 == 0 else "홀수")
print(13%2==0 and "짝수" or "홀수")

t1 = (1,2,3)
t2 = t1 + (4,)
print(t2)

a = {'A':90, 'B':80, 'C':70}
print(a)
print(a.pop('A'))
print(a)
print(a.pop('B'))
print(a)
print(a.pop('C'))

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(type(a), ":", a)
s = set(a)
print(type(s), ":", s)
