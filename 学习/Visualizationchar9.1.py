import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#       9.1 Visualization
d1 = np.arange(10)
plt.plot(d1)  # plot函数中传入x，y轴数据 和其他参数

fig = plt.figure()  # 创建一个新的figure，画出的图像都在figure中
ax1 = fig.add_subplot(2, 2, 1)  # 在fig对象中最多创建2*2张图，现在创建第1张
ax2 = fig.add_subplot(2, 2, 2)  # add_subplot返回的对象是AxesSubplot对象
ax3 = fig.add_subplot(223)  # 简单写法
plt.plot(np.random.randn(50).cumsum(), 'k--')  # 'k--'是黑色虚线，直接执行plot会在最后创建的subplot上绘制
ax1.hist(np.random.randn(50), bins=20, color='orange', alpha=0.5)  # 20等分的bins
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30), marker='d')

fig2, axes = plt.subplots(2, 2, sharex=True, sharey=True)  # 使不同subplot使用同一xy轴
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=1, hspace=1)  # 改变subplot间距

# 随机漫步图加标签
fig3 = plt.figure();
ax = fig3.add_subplot(1, 1, 1)
plt.plot(np.random.randn(500).cumsum())
ax.set_xticks([0, 125, 250, 375, 500])  # 设置x轴的刻度
ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],  # 设置用标签代替刻度
                   rotation=30, fontsize='small')  # 标签倾斜30度，字号为small
ax.set_title('Roaming')  # 设置图名
settings = {'xlabel': 'Stage', 'ylabel': 'process'}
ax.set(**settings)  # 也可用字典一次传入多个选项
ax.legend(loc='best')  # 添加图例
ax.text(100, 1, 'no100', fontsize=10)  # family是字体

plt.savefig('path.png', dpf=441, bbox_inches='tight')  # bbox_inches：裁掉空白区域

# 可以通过rc设置全局
plt.rc('figure', figsize=(3, 3))
font_options = {'weight': 'bold',
                'size': 'small'}
plt.rc('font', **font_options)  # 将模板统一使用
