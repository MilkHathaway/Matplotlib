import pandas as pd
import numpy as np

unrate = pd.read_csv(r"D:\untitled\UNRATE.csv")
unrate['DATE'] = pd.to_datetime(unrate['DATE']) #时间格式转换
#print(unrate)

import matplotlib.pyplot as plt
# plt.plot()  #画
# plt.show()  # 展示

# 存入数据
first_unrate = unrate[0:12] #取前12行的数据
plt.plot(first_unrate['DATE'],first_unrate['VALUE'])
plt.xticks(rotation = 45)
plt.xlabel('MONTH') #添加标题
plt.ylabel('VALUE')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()
