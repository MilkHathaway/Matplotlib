# 总结 直方图hist 盒图boxplot（分位图）

import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
# print(norm_reviews[:5])

##一、绘制直方图hist
fandango_distribution = norm_reviews['Fandango_Ratingvalue'].value_counts()#这一个count计数把索引搞没了
fandango_distribution = fandango_distribution.sort_index()

imdb_distribution = norm_reviews['IMDB_norm'].value_counts()
imdb_distribution = imdb_distribution.sort_index()
# print(fandango_distribution)
# print(imdb_distribution)

#fig,ax = plt.subplots()
#ax.hist(norm_reviews['Fandango_Ratingvalue'],range= (4,5),bins=20) #range(4,5)表示只显示4-5的，bins表示总共分多少条（全部数据非range数据）
# plt.show()

## 二、绘制多个直方图
fig = plt.figure(figsize=(5,20))  #这里只能写fig不能加ax，ax在写subplot可以加上
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)
ax1.hist(norm_reviews['RT_user_norm'], 20, range=(0, 5))
ax1.set_title('Distribution of Rotten Tomatoes Ratings')
ax1.set_ylim(0,50)

ax2.hist(norm_reviews['RT_user_norm'], 20, range=(0, 5))
ax2.set_title('Distribution of Rotten Tomatoes Ratings')
ax2.set_ylim(0, 50)

ax3.hist(norm_reviews['Metacritic_user_nom'], 20, range=(0, 5))
ax3.set_title('Distribution of Metacritic Ratings')
ax3.set_ylim(0, 50)

ax4.hist(norm_reviews['IMDB_norm'], 20, range=(0, 5))
ax4.set_title('Distribution of IMDB Ratings')
ax4.set_ylim(0, 50)

# plt.show()

## 三、盒图boxplot
fig,ax = plt.subplots()
ax.boxplot(norm_reviews['RT_user_norm'])
ax.set_xticklabels(['Rotten Tomatoes']) #添加横轴标签名字
ax.set_ylim(0,5) #设置y轴值范围
# plt.show()

# 一个图绘制多个boxplot
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig,ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols,rotation=90)
ax.set_ylim(0,5)
plt.show()
