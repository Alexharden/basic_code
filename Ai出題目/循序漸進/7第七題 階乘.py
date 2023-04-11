# #解法1
# n = int(input("輸入一個數字來計算階乘: "))
# if n < 0 or n > 12:
#     print("n的範圍應在0到12之間")
# else:
#     factorial = 1
#     for i in range(1, n+1):
#         factorial *= i
#     print("n的階乘為：", factorial)



#解法2 遞迴
#概念 如果我輸入5 他會重複執行這個動作
# factorial(0) = 1
# factorial(1) = 1 * factorial(0) = 1
# factorial(2) = 2 * factorial(1) = 2
# factorial(3) = 3 * factorial(2) = 6
# factorial(4) = 4 * factorial(3) = 24
# factorial(5) = 5 * factorial(4) = 120

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("請輸入一個整數n："))

if n < 0 or n > 12:
    print("n的範圍應在0到12之間")
else:
    print("n的階乘為：", factorial(n))
