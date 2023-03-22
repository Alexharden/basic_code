# # x = int(input("輸入數字"))
# x = input("輸入數字")
# x = int(x)
# if x > 200:
#     print("大於200")
# elif x > 100:
#     print("大於100")
# else:
#     print("小於等於100")

n1 = int(input("輸入數字一: "))
n2 = int(input("輸入數字二: "))
op = input("請輸入運算符號: +, -, *, /: ")
if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/": 
    print(n1 / n2)
else:
    print("你再亂搞")