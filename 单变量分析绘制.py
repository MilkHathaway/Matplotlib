# 只需要传入数据即可，kde是核密度现在不用管，bins=20（切成几份）
# 显示轮廓，fit当前的某个统计指标，实际上可以传入很多参数
# 参数介绍
# 均值，协方差，通过numpy这个库生成数据，单变量只需要分析一个维即可
# 想看特征和特征之间内部的关系，可以用散点图最好来描述
# 把数据转换为dataframe
# sns.joinplot散点图（数据量比较少情况下），维度和数据都传入进来，可以即画出散点图又可以画出直方图,还会计算出相关系数，非常方便
#
# hex图，数据量多的情况下，分块，颜色越深，表示点出现的次数越多，六边形，还是joinplot，但是kind=hex，并且给了个with的white风格，共有5个风格，但是white最好

import numpy as np
import pandas as pd
from scipy import stats,integrate #stats统计简写，integrate积分
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_color_codes()
np.random.seed(sum(map(ord,'distributions')))

##例1
# x=np.random.normal(size=100)
# sns.distplot(x,bins =20,kde = False,fit=stats.gamma()) #distplot一般用于查看单变量的分布，kde是核密度函数，以后会讲

##例2 曲线拟合gamma分布
# x = np.random.gamma(6,size=200)
# sns.distplot(x,kde=False,fit=stats.gamma) #重要fit拟合曲线重要

#例3 根据均值和协方差生成数据
mean, cov = [0,1],[(1,.5),(.5,1)]
data = np.random.multivariate_normal(mean,cov,200)#multivariate_normal多变量正态分布
df= pd.DataFrame(data,columns=['x','y'])
# print(df)

##例4 观察两个变量之间的分布关系最好用散点图jointplot,优势是既有散点图又有直方图，还有相关系数
# sns.jointplot(x='x',y='y',data=df)#x变量，y变量，传入数据

##分块散点图hex参数，颜色深的表示出现的次数多
x,y=np.random.multivariate_normal(mean,cov,1000).T
with sns.axes_style('white'):
    sns.jointplot(x=x,y=y,kind='hex',color='k')

iris = sns.load_dataset('iris')
#sns.pairplot(iris)

##指定分类变量的散点图
sns.pairplot(iris,hue='species')#hue参数是指定分类变量

##使用调色板palette='husl'
sns.pairplot(iris,hue='species',palette='husl')#palette='husl'是使用调色板的意思

##使用不同的形状markers=["o", "s", "D"]
sns.pairplot(iris,hue='species',palette='husl',markers=["o", "s", "D"])

##改变对角图，diag_kind='kde'
sns.pairplot(iris,diag_kind='kde',hue='species',palette='husl',markers=["o", "s", "D"])

##使用回归reg
sns.pairplot(iris,kind='reg',palette='husl')

##改变点的形状使用参数，使用edgecolor
g7 = sns.pairplot(iris, diag_kind="kde", markers="+",
                  plot_kws=dict(s=50, edgecolor="b", linewidth=1),
                  diag_kws=dict(shade=True))
plt.show()
