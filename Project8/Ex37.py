from array import array
from itertools import count

import matplotlib.pyplot as plt

"""
Matplotlib 수평 막대 그래프 그리기
Keyword: plt.barh(), horizontal bar graph, 수평 막대 그래프
"""
import numpy as np

x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

# plt.bar(x, values)
# plt.bar(x, values, color=['r','g','b'])
# colors = ['y', 'dodgerblue', 'C2']
# plt.bar(x, values, color=colors, width=0.5)  # 폭은 0.0 ~ 1.0

plt.barh(x, values,  edgecolor='lightgray', linewidth=5, tick_label=years)
# plt.xticks(x, years)

plt.show()