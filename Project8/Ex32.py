from array import array

import matplotlib.pyplot as plt

"""
Matplotlib 그리드 설정하기
Keyword: plt.grid(), grid style, 그리드, 격자
"""
import numpy as np

x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
# plt.grid(True)  # 그리드 그리기 활성화
# plt.grid(True, axis='x')  # 그리드 그리기 활성화
# plt.grid(True, axis='y')  # 그리드 그리기 활성화
plt.grid(True, axis='y', color='red', alpha=0.5, linestyle='--')
plt.grid(True, axis='x', color='green', alpha=0.5, linestyle='-.')

plt.show()