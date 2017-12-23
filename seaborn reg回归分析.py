import seaborn as sns
import matplotlib as mlp
import matplotlib.pyplot as plt

## 二、导入seanborn内置数据集’tips‘
tips = sns.load_dataset('tips')
# print(tips.head())

## 三、regplot()和Implot()都可以绘制回归关系，推荐用regplot()支持的参数更多，implot有限制，虽然功能多规范多
#首先调取函数，必须指定的参数有，x轴=列名，y轴=列名，data=dataframe传进去这三个必须
# sns.regplot(x='total_bill',y='tip',data=tips)


#当原始数据集（分类数据）不太支持回归模型，而已加个jitter小范围浮动，左右上下随机浮动，使得数据有那么一丁点
# sns.regplot(data=tips,x="size",y="tip")
sns.regplot(data=tips,x="size",y="tip",x_jitter=.05)
plt.show()
