#color 颜色通道 从各种网站找颜色三元组，括号是元组 /255定义的也不知道为啥记住
#合适的figsize和排列方式 通常放到一个屏幕中，linewith线的粗细
#在图中添加文字 ax.text(x,y,文字）
#设置线条粗细 Setting Line Width
#设置显示排版屏幕，一般显示在一个屏幕容易作比较
#Color
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']


cb_violet = (238/255, 130/255, 238/255)
cb_lndigo = (75/255, 0/255, 130/255)

fig = plt.figure(figsize=(12,12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1) #这里是sp+1
    ax.plot(women_degrees['Year'],women_degrees[major_cats[sp]],c=cb_violet,label = 'Women',linewidth= 4)#设置线条粗细
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c=cb_lndigo, label='men',linewidth= 4)
    for key,spine in ax.spines.items():#去掉坐标轴
        spine.set_visible(False)
    ax.set_xlim(1968,2011)#添加x，y轴范围
    ax.set_ylim(0,100)
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")#忽略x轴和y轴的刻度（这个和边框不一样）

plt.legend(loc='upper right')
# plt.show()

#设置线条粗细及空间展示屏幕大小
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_violet, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_lndigo, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

plt.legend(loc='upper right')
#plt.show()

#给图表某位置添加文本
for sp in range(0, 6):
    ax = fig.add_subplot(1, 6, sp + 1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_violet, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100 - women_degrees[stem_cats[sp]], c=cb_lndigo, label='Men', linewidth=3)
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
plt.show()
