n = input("輸入一個正整數")
n = int(n) #轉換輸入成數字
for i in range(n):
    if i*i == n:
        print("整數平方根",i)
        break
else:
    print("沒有整數平方根")#迴圈完後一定會印出