#senborn绘制回归分析，使用seaborn的内置数据集‘tips’，是pandas的dataframe格式
#直接点head，total_bill 消费金额，tip 消费，sex性别，smoker是否抽烟，day是星期，time是中饭还是午饭，size用餐人数

## 一、导入常用包
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mlp
import matplotlib.pyplot as plt

## 二、导入seanborn内置数据集’tips‘

titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

## 四、重点 多变量回归分析
# 对于星期几，只有1234567这几个类别值，这样的数据如何很好的可视化展示，重要
#对于类别可以用stripplot，并不推荐大家使用，因为堆在一块了某天的，通常数据量比较大。这个是需要我们解决的问题，解决堆积问题

# sns.stripplot(x="day",y="total_bill",data=tips)

#方案1 还是stripplot，但是加上jitter ，jitter=true，即要把我这个点进行偏，随机偏动，更清晰展示
#重叠是很常见的现象，但是重叠营销了我观察数据的量了
# sns.stripplot(x="day",y="total_bill",data=tips,jitter=True)
#plt.show()
#方案2 用 看起来像数一样，用swarmplot函数，类似圣诞树，这个比较好比上个，还可以加上一个属性，加上一个hue指标，通用的参数这是hue等
# sns.swarmplot(x="day",y="total_bill",data=tips,hue="sex")


##横竖着话，x和y调过来即可


##五、盒图，一般情况下数据并不是那么的好，会有离群值（异常值），sns.boxplot，传入x，传入y，传入data
# IQR即统计学概念四分位距离，即第一/四分位与第三/四分位之间的距离
# N=1.5IQR 如果一个值>Q3+N，或者<Q1-N，则为离群点，两个横杠表示最大值，最小值，菱形表示离群点

# sns.boxplot(x='day',y="total_bill",hue='time',data=tips)

##六、琴形图，越胖出现的次数越多，越瘦出现的次数越小，可以指定split属性，即左边一个属性，右边一个属性，split=true，琴形图用的挺多

# sns.violinplot(x='total_bill',y='day',hue='time',data=tips)
# sns.violinplot(x='total_bill',y='day',hue='sex',data=tips,split=True)
# plt.show()

## 七、图合并，alpha=.5代表透明程度，
# sns.violinplot(x='day',y='total_bill',data=tips,inner=None)
# sns.swarmplot(x='day',y='total_bill',data=tips,color = 'w',alpha=.5)

## 八、条形图barplot,可以分组
##数据集是泰坦尼克号数据集，class是头等舱、二等舱、三等舱，y是获救率
# sns.barplot(x='sex',y='survived',hue='class',data=titanic)

##点图，可以更好的描述变化差异，点图pointplot.用的蛮多的，linestyles是线形(折线图）
# sns.pointplot(x='sex',y='survived',hue='class',data=titanic)

##点图，参数化设置
# sns.pointplot(x='class',y='survived',hue='sex',data=titanic,
#               palette={'male':'g',"female":"m"},
#               markers=["^","o"],linestyles=['-','--']) #palette用大括号，其他的用中括号记住

## 宽形数据,画横的图，只需要加个参数orient="h"
# sns.boxplot(data=iris,orient='h')

##九、多层面板分类图（常用的）factorplot，在这里可以画各种图，只要把kind指定好即可,col=各个层的划分

# sns.factorplot(x='day',y="total_bill",hue="smoker",data=tips)

# sns.factorplot(x='day',y='total_bill',hue='smoker',data=tips,kind='bar')
# sns.factorplot(x='day',y='total_bill',hue='smoker',)

sns.factorplot(x='day',y='total_bill',hue="smoker",col="time",data=tips,kind='swarm')

sns.factorplot(x="time", y="total_bill", hue="smoker",
               col="day", data=tips, kind="box", size=4, aspect=1) #size空间大小，慢慢自己把握


plt.show()
