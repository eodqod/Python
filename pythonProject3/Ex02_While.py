# While 반복문

"""
조건이 참인동안 반복실행 한다.
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
"""

# 종료 문자를 입력 받을 때까지 계속 반복 하고 싶다.

menu="""
1. 입력
2. 수정
3. 삭제
4. 조회
5. 종료

원하는 번호를 선택하세요 """

select = 0
while select != 5:
    print(menu, end="")
    select = int(input())
