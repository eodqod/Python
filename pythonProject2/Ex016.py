# 년도를 입력받아 윤/평년을 판단하는 프로그램을 만드시오
y = int(input('년도를 입력하세요'))

if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
    print('윤년')
else:
    print('평년')