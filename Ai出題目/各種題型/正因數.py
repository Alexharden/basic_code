n = int(input("請輸入一個整數: "))

print("正因數有：")
for i in range(1, n+1):
    if n % i == 0:
        print(i)
