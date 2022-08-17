import matplotlib.pyplot as plt

# 마커지정하기
# b : blue
# r : red
# o : circle
plt.plot([1, 3, 6, 8], [2, 3, 5, 10], 'ro')  # 빨간색 동그라미
plt.plot([2, 3, 4, 5], [3, 4, 7, 9], 'b^-')  # 파란색 + 삼각형마커 + 실선
plt.plot([2, 4, 6, 8], [4, 6, 10, 20], 'gs--')  # 초록색 + 사각형마커 + 점선

plt.plot([4, 5, 6], marker="H")
plt.plot([3, 4, 5], marker="d")
plt.plot([2, 3, 4], marker="x")
plt.plot([1, 2, 3], marker=11)
plt.plot([0, 1, 2], marker='$Z$')


plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()
