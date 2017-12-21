import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# %matplotlib inline 画图写完代码直接显示在notebook pycharm不支持

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)# linspace函数，在横坐标0-14上取100个点#曲线是用100个点连起来的
    for i in range(1, 7): #画6条线
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip) #i*.5表示0.5i，sin是数学上的sin函数

sinplot() #默认风格，参数组合比较头疼，所以有个风格模板调用seanborn
plt.show()

sns.set()#.set是默认参数
sinplot() #shift+enter 换行快捷键
plt.show()

#五中主题风格 darkgrid whitegrid dark white ticks

sns.set_style('whitegrid')#常用风格
data = np.random.normal(size = (20,6))+np.arange(6)/2
#sns.boxplot(data = data)
plt.show()


sns.set_style('dark')
sinplot()
plt.show()

sns.set_style("white")
sinplot()
plt.show()

sinplot()
sns.despine()#去掉上边和右边的线，对这个画风还可以稍微的改变

f.ax=plt.subplots()
sns.violinplot()
sns.set_style('whitegrid')
sns.violinplot(data)
sns.despine(offset=10,left = True)#默认值是上边和右边去掉，offset参数是你要的画的图离你轴线的距离

##with打开主题，画子图的时候用的比较多，不同子图不同风格
with sns.axes_style('darkgrid'):
    plt.subplot(211)
    sinplot()
plt.subplot(212)
sinplot(-1)

plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2
ax1 = plt.subplot(211) # 在图表2中创建子图1
ax2 = plt.subplot(212) # 在图表2中创建子图2

##布局大小设置,context函数，且里面有很多比如paper等参数
sns.set()

sns.set_context('paper')
plt.figure(figsize=(8,6))
sinplot()

sns.set_context('talk') #talk,里边稍微大一些，供大家选择，区别不大
plt.figure(figsize=(8,6))
sinplot()

sns.set_context("poster") #坐标轴字体变大了
plt.figure(figsize=(8, 6))
sinplot()

sns.set_context("notebook", font_scale=2.5, rc={"lines.linewidth": 2.5})
#为了方便对配置字典进行设置，可以使用rc()。下面的例子同时配置点标识符、线宽和颜色：
#matplotlib.rc("lines", marker="x", linewidth=2, color="red")
sinplot() #指定字体大小，最好用with打开风格
plt.show()


