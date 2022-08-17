from array import array

import matplotlib.pyplot as plt

"""
Matplotlib 타이틀 설정하기
Keyword: plt.title(), loc, pad, 그래프 제목, 스타일, 위치, 여백
"""
import numpy as np

x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='forestgreen', marker='^', markersize=9)

plt.tick_params(axis='both', direction='in', length=3, pad=6, labelsize=14)

# plt.title('Graph Title 한글')  # 한글 깨짐
title_right = plt.title('Graph Title', loc='right', pad=20)

title_font = {
    'fontfamily':'Malgun Gothic',
    'fontsize': 16,
    'fontweight': 'bold'
}
title_left = plt.title('그래프 타이틀', fontdict=title_font, loc='left', pad=20)

# 타일틀을 변수에 저장해서 필요시 정보를 얻을 수 있다.
print(title_left.get_position())
print(title_left.get_text())

print(title_right.get_position())
print(title_right.get_text())

plt.show()