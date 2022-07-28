# 점수를 입력받아 A~F까지 학점을 판단하는 프로그램을 만드시오
# elif 명령을 사용해라

score = int(input('점수를 입력하세요'))

if 100 >= score >= 90:
    print('당신의 학점은 A입니다.')
elif score >= 80:
    print('당신의 학점은 B입니다.')
elif score >= 80:
    print('당신의 학점은 C입니다.')
elif score >= 70:
    print('당신의 학점은 D입니다.')
elif score >= 60:
    print('당신의 학점은 E입니다.')
else:
    print('당신의 학점은 F입니다.')