user = input("請輸入一個數字: ") #假設我輸入 1234
while len(user) > 1: #長度會4
    total = 0 #先設定一個待會要加總的變數
    for i in user: #user是字串 所以是 1234 第一次i = 1 第二次i =2
        total += int(i) #total = 1 + 2 + 3 + 4
        user = str(total) #將加總的數字轉成字串 重新讓while迴圈判斷 長度是否>1
print(user) 