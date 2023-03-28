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
# print("判別輸入字元類別")
# ch = input("請輸入字元: ")
# if ch.isdigit():
#     print("這是數字")
# elif ch.isalpha():
#     if ch.islower():
#         print("這是小寫字元")
#     elif ch.isupper():
#         print("這是大寫字元")
# else:
#     print("這是特殊字元") 

# x = None
# print(x)
# print(type(x))

# flag = True #下方列印出來同寫False True和其他值則為不同
# if not flag:
#     print("尚未定義flag")

# if flag:
#     print("有定義")
# else:
#     print("尚未定義的flag")

#if身高體重bmi
# height = eval(input("請輸入身高(公分): "))
# weight = eval(input("請輸入體重(公斤): "))
# bmi = weight / (height/100) ** 2   #將身高改成公尺
# if bmi >=28:
#     print("過於肥胖")
# else:
#     print("體重不肥")
#另一種
# height = eval(input("請輸入身高(公分): "))
# weight = eval(input("請輸入體重(公斤): "))
# bmi = weight / (height/100) ** 2   #將身高改成公尺
# if  18.5 <= bmi < 24:
#     print(f"{bmi = :5.2f}體重正常 ") #5.2f 表示輸出的寬度最小為5位 且取代小數第二位
# else:
#     print(f"{bmi = :5.2f}體重不正常 ")

#猜心中的數字
# ans = 0
# print("猜數字遊戲，請心中想一個0 - 7之間的數字，然後回答問題")

# truefalse = "請輸入y或y代表有， 其他則代表無： "
# q1 = "有沒有看到心中的數字 : \n" +\
#       "1, 3, 5, 7 \n"
# num = input(q1 + truefalse) #檢查二進位的第一位是否含有1 
# print(num)
# if num == "y" or num =="Y":
#     ans += 1

# truefalse = "請輸入y或y代表有， 其他則代表無： "
# q2 = "有沒有看到心中的數字 : \n" +\
#       "2, 3, 6, 7 \n"
# num = input(q2 + truefalse) #檢查二進位的第二位是否含有1  
# print(num)
# if num == "y" or num =="Y":
#     ans += 2

# truefalse = "請輸入y或y代表有， 其他則代表無： "
# q3 = "有沒有看到心中的數字 : \n" +\
#       "4, 5, 6, 7 \n"
# num = input(q3 + truefalse) #檢查二進位的第三位是否含有1
# print(num)
# if num == "y" or num =="Y":
#     ans += 4
# print("你心中所想的數字是: ", ans)
#補充10進位 4 = 二進位的100  10進位的 2 = 二進位的 010 10進位的1 = 二進位的 001

#12生肖 (西元日曆和農曆年年初年尾有差異)
year = eval(input("請輸入你的西元生日年 : "))
year -= 1900
zodiac = year % 12
if zodiac == 0:
    print("你的生肖是 : 鼠")
elif zodiac == 1:
    print("你的生肖是 : 牛")
elif zodiac == 2:
    print("你的生肖是 : 虎")
elif zodiac == 3:
    print("你的生肖是 : 兔")
elif zodiac == 4:
    print("你的生肖是 : 龍")
elif zodiac == 5:
    print("你的生肖是 : 蛇")
elif zodiac == 6:
    print("你的生肖是 : 馬")
elif zodiac == 7:
    print("你的生肖是 : 羊")
elif zodiac == 8:
    print("你的生肖是 : 猴")
elif zodiac == 9:
    print("你的生肖是 : 雞")
elif zodiac == 10:
    print("你的生肖是 : 狗")
else:
    print("你的生肖是 : 豬")


