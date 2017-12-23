#heatmap热度图，seaborn中常用的图，也是我最喜欢画的一种图
#重要点思维：拿到一批数据一般会求特征之间的相关系数，可以用padas直接求出来相关系数，放到heatmap，可以很清楚的看到两个特征的相关程度，这是一个固定的数据思维
#用途：比如拿到一批离散数据，想看一下在哪个点值比较大，在哪个点值比较低，你想把这样一个值的变化，用颜色来区分出来，这是我们要做的一个变化

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
import seaborn as sns
sns.set()
#颜色可以由浅到深，可以由深到浅，比如股票每天的涨跌
#
#随机生成一个3*3矩阵，点heatmap穿进去数据，调色板叫做col_bar,很明显的看出这堆数中的值大小
uniform_data=np.random.rand(3,3)
heatmap=sns.heatmap(uniform_data)
#可以区间设置，vmin vmax，大于或小于v的全是一个颜色，只有在这区间的才会分颜色
# ax=sns.heatmap(uniform_data,vmin=0.2,vmax=0.5)
#比如拿到的数据是权重参数，又有正负，正是涨，负是跌，定义center=0，以0为中心画这个数据
normal_data = np.random.randn(3, 3)
ax2 = sns.heatmap(normal_data, center=0)

#读取航班数据集flights，seaborn自带的，1949年乘机的人数passengers
#需要横轴表示年份，纵轴月份，点的值是大小
# 把当前的数据转换为可以用的矩阵格式，读取的dataframe的，然后.pivot一下（x，y，值）x和y直接写列名即可，直接把dataframe中的year和month传进来，加一个注释项annot=True，fmt=“d”即是在图上显示数据值，linewidth=.5加上一个格，这个图会比较更清晰，调色板是cmap=“YIGnBu”，颜色，cbar=false是隐藏，但是一般不隐藏不然不知道图例了
#默认颜色太丑，应该设置一下常用的颜色

flights = sns.load_dataset('flights')
# print(flights.head())
flights=flights.pivot('month','year','passengers') #pivot函数重要
print(flights.head())
sns.heatmap(flights) #注意这里是直接传入数据集即可，不需要再单独传入x和y了

sns.heatmap(flights,linewidth=.5,annot=True,fmt='d')

#改变颜色
ax= sns.heatmap(flights,cbar=False,cmap='YlGnBu')
plt.show()
