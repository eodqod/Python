import matplotlib.pyplot as plt

#  Matplotlib 그래프 영역 채우기
"""
fill_between() - 두 수평 방향의 곡선 사이를 채웁니다.
fill_betweenx() - 두 수직 방향의 곡선 사이를 채웁니다.
fill() - 다각형 영역을 채웁니다.
"""

# 다각형 채우기
x = [1, 2, 3, 4]
y1 = [2, 3, 5, 10]
y2 = [1, 2, 4, 8]

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# 좌표 1개씩 시계방향으로  점을 지정하면 채워준다.
plt.fill([1.9, 1.9, 3.1, 3.1, 2.7], [1.0, 4.0, 6.0, 3.0, 1.5], color='green', alpha=0.5)

plt.show()

