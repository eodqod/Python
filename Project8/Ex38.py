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

# np.random.seed(100)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
print(x)
print(y)

# plt.scatter(x, y)
area = (30 * np.random.rand(n))**2
colors = np.random.rand(n)

plt.scatter(x, y, s=area, c=colors)
plt.show()
