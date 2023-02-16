n = int(input("請輸入一個大於1的數字:  "))
if n == 2:  #2是質數 先單獨拉出
    print(n,end="")
    print("是質數!")
else:
    for i in range(2,n): #判斷是不是還有能整除的
        if n % i == 0: #i從2開始跑 i每次+1 
            print(n,end="")
            print("不是質數!" )
            break
    else: #無法被整除有餘數的
        print(n,end="")
        print("是質數!" )
