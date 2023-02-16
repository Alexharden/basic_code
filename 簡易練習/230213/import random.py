#隨機模組
import random

#隨機選取
# data =random.choice([1,5,6,10,20]) #choice 隨機選一筆
# print(data)
# data =random.sample([1,5,6,10,20],4) #sample 隨機選多筆
# print(data)

#隨機調換順序 (洗牌的概念)
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)

#隨機取得亂數
# data=random.random() # 0 ~ 1 之間的亂數
# data=random.uniform(60, 100) #60 ~ 100 之間的亂數
# print(data)

#常態分配亂數
#平均數 100, 標準差 10, 得到資料多數在 90 - 110 之間
# data = random.normalvariate(100, 10)
# print(data)
# #平均數 0, 標準差 10, 得到的資料多數在 -5 ~ 5之間
# data1 = random.normalvariate(0, 5)
# print(data1 )


# 統計模組
import statistics as stat 
# data = stat.mean([1,4,5,8]) #平均數
# data = stat.median([1,2,3,4,5,8,100]) #中位數 排除極端值
data = stat.stdev([1,2,3,4,5,8,10]) #標準差

print(data)
