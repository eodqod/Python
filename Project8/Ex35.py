from array import array

import matplotlib.pyplot as plt

"""
Matplotlib 수평선/수직선 표시하기
axhline(): 축을 따라 수평선을 표시합니다.
axvline(): 축을 따라 수직선을 표시합니다.
hlines(): 지정한 점을 따라 수평선을 표시합니다.
vlines(): 지정한 점을 따라 수직선을 표시합니다.
"""
import numpy as np

x = np.arange(0, 4, 0.5)

plt.plot(x, x + 1, 'bo')
plt.plot(x, x**2 - 4, 'g--')
plt.plot(x, -2*x + 3, 'r:')

plt.axhline(4.0, 0.1, 0.9, color='lightgray', linestyle='--', linewidth=2)
plt.hlines(-0.62, 1.0, 2.5, color='gray', linestyle='solid', linewidth=3)
"""
axvline() 함수의 첫번째 인자는 x 값으로서 수직선의 위치가 됩니다.
두, 세번째 인자는 ymin, ymax 값으로서 0에서 1 사이의 값을 입력합니다. 0은 아래쪽 끝, 1은 위쪽 끝을 의미합니다.
vlines() 함수에 x, ymin, ymax를 순서대로 입력하면, 점 (x, ymin)에서 점 (x, ymax)를 따라 수평선을 표시합니다.
"""
plt.axvline(1.0, 0.2, 0.8, color='lightgray', linestyle='--', linewidth=2)
plt.vlines(1.8, -3.0, 2.0, color='gray', linestyle='solid', linewidth=3)

plt.show()