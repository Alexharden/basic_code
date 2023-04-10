n = int(input("請輸入一個數字: "))

sum = 0
for i in range(1, n+1):
    if i % 2 == 1:
        sum += i

print("從1到", n, "之間的所有奇數的總和為：", sum)
