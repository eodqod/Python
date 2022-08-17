import matplotlib.pyplot as plt

#  Matplotlib 그래프 영역 채우기
"""
fill_between() - 두 수평 방향의 곡선 사이를 채웁니다.
fill_betweenx() - 두 수직 방향의 곡선 사이를 채웁니다.
fill() - 다각형 영역을 채웁니다.
"""
x = [1, 2, 3, 4]
y = [2, 3, 5, 10]

plt.plot(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# 수치는 좌표의 인덱스 값이다. x : 2~3, y: 3~5
plt.fill_between(x[1:3], y[1:3], alpha=0.5)

plt.show()
