num = int(input("請輸入一個正整數: ")) # 讓使用者輸入一個正整數

if num > 1: # 判斷輸入的數字是否大於 1
    for i in range(2, num): # 使用 for 迴圈從 2 到該數字的前一個數字之間檢查
        if (num % i) == 0: # 如果該數字能夠被整除，就不是質數
            print(num, "不是質數")
            break # 跳出迴圈 
    else: 
        print(num, "是質數") 
            
else:
    print(num, "不是質數") # 如果輸入的數字小於等於 1，就不是質數

#用flag來
num = int(input("請輸入一個正整數: "))

if num > 1:
    is_prime = True # 標記是否為質數的變數
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False # 能夠整除，不是質數
            break
    if is_prime:
        print(num, "是質數")
    else:
        print(num, "不是質數")
else:
    print(num, "不是質數")
