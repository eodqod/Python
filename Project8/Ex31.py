import matplotlib.pyplot as plt

"""
Matplotlib 여러 곡선 그리기

"""
import numpy as np

x = np.arange(0, 2, 0.2)

# plt.plot(x, x, 'r--')
# plt.plot(x, x**2, 'bo')
# plt.plot(x, x**3, 'g-.')

# 위의 3줄을 1줄로 표현할 수 있다.
plt.plot(x, x, 'r--', x, x**2, 'bo', x, x**3, 'g-.')

plt.show()