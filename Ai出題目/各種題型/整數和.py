n = int(input("請輸入一個正整數："))
if n <= 0:
    print("輸入錯誤，請輸入正整數。")
else:
    sum = 0
    for i in range(1, n+1):
        sum += i
    print("從1到", n, "之間的所有整數的總和為：", sum)
