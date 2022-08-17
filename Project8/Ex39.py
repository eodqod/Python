from array import array
from itertools import count

import matplotlib.pyplot as plt

"""
Matplotlib 산점도 그리기
산점도 (Scatter plot)는 두 변수의 상관 관계를 직교 좌표계의 평면에 점으로 표현하는 그래프입니다.
matplotlib.pyplot 모듈의 scatter() 함수를 이용하면 산점도를 그릴 수 있습니다.
Keyword: plt.scatter(), scatter plot, 산점도
"""
import numpy as np

plt.plot([1], [1], 'o', markersize=20, c='#FF5733')
plt.scatter([2], [1], s=20**2, c='#33FFCE')

plt.text(0.5, 1.05, 'plot(markersize=20)', fontdict={'size': 14})
plt.text(1.6, 1.05, 'scatter(s=20**2)', fontdict={'size': 14})
plt.axis([0.4, 2.6, 0.8, 1.2])
plt.show()