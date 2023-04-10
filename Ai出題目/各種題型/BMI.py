height = float(input("你的身高是: "))
weight = float(input("你的體重是: "))
height = (height / 100) ** 2
BMI = (weight/height)
print(f"你的BMI是 {BMI}")
if BMI < 18.5:
    print("過輕")
elif 18.5 <= BMI < 24:
    print("正常") 
elif 24 <= BMI < 27:
    print("過重") 
elif 27 <= BMI < 30:
    print("輕度肥胖") 
elif 30<= BMI < 35:
    print("中度肥胖") 
elif BMI >= 35:
    print("重度肥胖")
