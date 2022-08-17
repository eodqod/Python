import matplotlib.pyplot as plt

"""
Matplotlib 축 스케일 지정하기
matplotlib.pyplot 모듈의 xscale(), yscale() 함수를 사용해서 그래프의 축 스케일을 다양하게 지정할 수 있습니다.
축은 기본적으로 ‘linear’ 스케일로 표시되지만 ‘log’, ‘symlog’, ‘logit’으로 변경할 수 있습니다.
Keyword: plt.xscale(), plt.yscale(), axis scale, linear, log
"""
import numpy as np

x = np.linspace(-10, 10, 100)  # -10~10까지 100개의 배열을 생성
print(len(x))
y = x ** 3 # x값을 세제곱

# 축의 원점을 기준으로 양, 음의 방향이 대칭적인 로그 스케일로 표시됩니다.
plt.plot(x, y)
plt.xscale('symlog')  # Symmetrical Log Scale(대칭 로그 스케일)

plt.show()
