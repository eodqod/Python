from array import array

import matplotlib.pyplot as plt

"""
Matplotlib 눈금 표시하기
Keyword: plt.xticks(), plt.yticks(), plt.tick_params(), tick, 눈금 스타일

tick_params() 함수를 사용하면 눈금의 스타일을 다양하게 설정할 수 있습니다.
axis는 설정이 적용될 축을 지정합니다. {‘x’, ‘y’, ‘both’} 중 선택할 수 있습니다.
direction을 ‘in’, ‘out’으로 설정하면 눈금이 안/밖으로 표시됩니다. {‘in’, ‘out’, ‘inout’} 중 선택할 수 있습니다.
length는 눈금의 길이를 지정합니다.
pad는 눈금과 레이블과의 거리를 지정합니다.
labelsize는 레이블의 크기를 지정합니다.
labelcolor는 레이블의 색상을 지정합니다.
top/bottom/left/right를 True/False로 지정하면 눈금이 표시될 위치를 선택할 수 있습니다.
width는 눈금의 너비를 지정합니다.
color는 눈금의 색상을 지정합니다.
"""
import numpy as np

x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='forestgreen', marker='^', markersize=9)
# plt.xticks([0, 1, 2])
# plt.yticks(np.arange(1, 6))
# plt.xticks([0, 1, 2], ['a','b','c'])
# plt.yticks(np.arange(1, 6),['!','@','#','$','%'])
plt.xticks(np.arange(0, 2, 0.2), labels=['Jan', '', 'Feb', '', 'Mar', '', 'May', '', 'June', ''])
plt.yticks(np.arange(0, 7), ('0', '1GB', '2GB', '3GB', '4GB', '5GB', '6GB'))

plt.tick_params(axis='x', direction='in', length=3, pad=6, labelsize=14, labelcolor='green', top=True)
plt.tick_params(axis='y', direction='inout', length=10, pad=15, labelsize=12, width=2, color='r')


plt.show()