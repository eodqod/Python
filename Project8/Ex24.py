import matplotlib.pyplot as plt

#  Matplotlib 색상 지정하기
# plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], 'r')
# plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], 'g')
# plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], 'b')

plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], color='limegreen')
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], color='violet')
plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], color='dodgerblue')

plt.plot([2, 4, 6, 8], [4, 6, 10, 15], color='#e35f62', marker='o', linestyle='--')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
