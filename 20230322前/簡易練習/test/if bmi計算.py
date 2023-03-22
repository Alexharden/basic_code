weight = float(input("你的體重: "))
height = float(input("你的身高: "))
bmi = weight / (height /100) **2
if bmi >=28:
    a = "運動"
else:
    a = "正常"
print(f'你的bmi數值為:\t{bmi},{a}') #\t 加一個縮排 #\n 換行


