import matplotlib.pyplot as plt

"""
Matplotlib 축 스케일 지정하기
matplotlib.pyplot 모듈의 xscale(), yscale() 함수를 사용해서 그래프의 축 스케일을 다양하게 지정할 수 있습니다.
축은 기본적으로 ‘linear’ 스케일로 표시되지만 ‘log’, ‘symlog’, ‘logit’으로 변경할 수 있습니다.
Keyword: plt.xscale(), plt.yscale(), axis scale, linear, log
"""
import numpy as np

x = np.linspace(0, 5, 100)
# 로그 스케일은 지수함수 (Exponential function)와 같이 기하급수적으로 변화하는 데이터를 표현하기에 적합합니다.
y = np.exp(x)

plt.plot(x, y)
plt.yscale('linear')
# plt.yscale('log')

plt.show()
