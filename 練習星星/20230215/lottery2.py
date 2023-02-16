import random

lottery_A = []
while(len(lottery_A)<6):
    #random.randint 包含頭尾 
    numA=random.randint(1,38) #1-38取1
    if(numA not in lottery_A): #隨機取的數不在列表內
        lottery_A.append(numA) #執行增加 把數字放入列表
lottery_A = sorted(lottery_A)
# lottery_A =  sorted(lottery_A)
print("第一區樂透號碼",lottery_A)
lottery_B = random.randint(1,8)
print("第二區樂透號碼",lottery_B)
lottery_A.append(lottery_B)
#map(function函數,variable變數)
#list python3 之後都要使用list
lottery_A = list(map(str,lottery_A)) #map對列表中的所有數字
lottery_A = (",".join(lottery_A))
print(lottery_A)

# sorted() > 排序 、 " ".join()將list轉成str 、 map(str , list) 返回一個可跌代的map物件
# print(f'第一個選區號碼為 => {",".join(map(str,sorted(lottery_A)))}') 
# print(f'第二個選區號碼為 => {random.randint(1,8)}')
