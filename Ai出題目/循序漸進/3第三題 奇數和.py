num = int(input("請輸入一個數字: "))
sum = 0
for i in range(1, num+1):
    if i % 2 == 1:
        sum += i
print(sum)