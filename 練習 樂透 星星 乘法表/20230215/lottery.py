import random
numbersOne = []
for i in range (1,39):
        numbersOne.append(i) #將1-39全部丟進列表
#random.sample隨機取得列表中的數字 sorted排序
areaOne = sorted(random.sample(numbersOne, 6))
count = 0
while count < len(areaOne):
    #把數字轉成字串為了最後用join函式把list的字串拉出來
    areaOne[count] = str(areaOne[count])
    count += 1
print("第一區號碼為:",areaOne) #題目為兩個選號區
#random.randint隨機從範圍內取一個整數
areaTwo = random.randint(1, 8) #(1,8)就是1-8
areaTwo = str(areaTwo) #把數字轉成字串為了最後的join函式

print("第二區號碼為:", areaTwo)#題目為兩個選號區

areaOne.append(areaTwo) #將第二區的號碼加入第一區
Result = "," .join(areaOne) #把列表字串拉出，組成字串用,隔開
print(Result)


