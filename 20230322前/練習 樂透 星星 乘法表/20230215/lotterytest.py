import random
numbers = []
for i in range(1,39): 
    numbers.append(i)#把1-38的數字放入空列表
numbers = random.sample(numbers,6)  #隨機取列表中的六個數字
numbers = sorted(numbers) #排序
print("第一區號碼: ",numbers)
numbers2 = random.randint(1,8) #隨機從1-8裡面挑一個數字
print(f"第二區號碼: ",numbers2)
numbers.append(numbers2) #將第二組數字放入第一組數字最後
#map(function函數,variable變數)
#使用map轉換資料型態 list python3 之後都要使用list
numbers = (list(map(str,numbers))) #將數字個別轉成字串
numbers = ",".join(numbers) #把數字從列表中拉出用,分開沒有[]
print("你的樂透號碼是:",numbers)