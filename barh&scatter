#总结 先添加横坐标位置，然后再用标签替换横坐标，xticks 和 xticklabels函数用法
#总结 柱形图（纵向）bar，条形图（横向）barh，散点图scatter

import pandas as pd
reviews = pd.read_csv("fandango_scores.csv")
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]
print(norm_reviews[:1])

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = reviews.ix[0,num_cols].values
print(bar_heights)
bar_position = arange(5)+ 0.75
print(bar_position)

fig,ax = plt.subplots()  #图空间,多个要加s
# ax.bar(bar_position,bar_heights,0.8) #0.5表示柱体宽度 #柱形图（纵向叫柱形图）
#添加标签
plt.xlabel("Rating Source")
plt.ylabel('Average Rating')
plt.title("Average User Rating For Avengers: Age of Ultron (2015)")

#添加横坐标
tick_position = range(1,6) #存位置
ax.set_xticks(tick_position) #附加给位置
ax.set_xticklabels(num_cols,rotation = 45) #附加任意标签

# plt.show()


#二、条形图（横着的柱形图）画法
#ax.barh(bar_position,bar_heights,0.5)
plt.show()


#三、散点图
fig,ax = plt.subplots()
ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
#plt.show()

## 多个散点图空间 子图
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1) # fig.add_subplot函数
ax2 = fig.add_subplot(2,1,2)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
ax2.scatter(norm_reviews['RT_user_norm'], norm_reviews['Fandango_Ratingvalue'])
ax2.set_xlabel('Rotten Tomatoes')
ax2.set_ylabel('Fandango')
plt.show()

