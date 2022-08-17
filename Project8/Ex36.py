from array import array
from itertools import count

import matplotlib.pyplot as plt

"""
Matplotlib 막대 그래프 그리기
막대 그래프 (Bar graph, Bar chart)는 범주가 있는 데이터 값을 직사각형의 막대로 표현하는 그래프입니다.
Matplotlib에서는 matplotlib.pyplot 모듈의 bar() 함수를 이용해서 막대 그래프를 간단하게 표현할 수 있습니다.
Keyword: plt.bar(), bar graph, 막대 그래프
"""
import numpy as np

x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

# plt.bar(x, values)
# plt.bar(x, values, color=['r','g','b'])
# colors = ['y', 'dodgerblue', 'C2']
# plt.bar(x, values, color=colors, width=0.5)  # 폭은 0.0 ~ 1.0

plt.bar(x, values, align='edge', edgecolor='lightgray', linewidth=5, tick_label=years)
# plt.xticks(x, years)

plt.show()