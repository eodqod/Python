import matplotlib.pyplot as plt

#  Matplotlib 그래프 영역 채우기
"""
fill_between() - 두 수평 방향의 곡선 사이를 채웁니다.
fill_betweenx() - 두 수직 방향의 곡선 사이를 채웁니다.
fill() - 다각형 영역을 채웁니다.
"""
x = [1, 2, 3, 4]
y1 = [2, 3, 5, 10]
y2 = [1, 2, 4, 8]

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill_between(x[1:3], y1[1:3], y2[1:3], color='lightgray', alpha=0.5)
plt.fill_between(x[2:4], y1[2:4], y2[2:4], color='red', alpha=0.5)
plt.fill_between(x[0:2], y1[0:2], y2[0:2], color='blue', alpha=0.5)

plt.show()

