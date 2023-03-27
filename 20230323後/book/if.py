# x, y = (input("請輸入兩個數字")).split(",")
# x = int(x)
# y = int(y)
# if x > y:
#     max_ = x
#     print(max_)
# else:
#     max_ = y
#     print(max_)

# x, y = (input("請輸入兩個數字")).split(",")
# max_ = max(x, y)
# print(max_)

# x = 0
# items = eval(input("請輸入一個數字"))
# items = x if items >=10 else items #如果iteams >= 10 x = 0 so items = 0
# print(items)

# print("計算成績")
# score = input("請輸入分數: ")
# sc = int(score)
# if sc >= 90:
#     print("A")
# elif sc >= 80:
#     print("B")
# elif sc >= 70:
#     print("C")
# elif sc >= 60:
#     print("D")
# else:
#     print("F")

#  
#也可以改寫成以下這段 比較正確能減少出錯
print("判別輸入字元類別")
ch = input("請輸入字元: ")
if ch.isdigit():
    print("這是數字")
elif ch.isalpha():
    if ch.islower():
        print("這是小寫字元")
    elif ch.isupper():
        print("這是大寫字元")
else:
    print("這是特殊字元") 

