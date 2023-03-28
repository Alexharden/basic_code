# #ax^2 + bx + c = 0   3x^2 + 5 x + 1 = 0 書本 5-17頁
# a = 3 
# b = 5
# c = 1
# r1 =(-b + (b**2-4*a*c)**0.5)/(2*a)
# r2 =(-b - (b**2-4*a*c)**0.5)/(2*a)
# print(f"{r1 = :6.4f},  {r2 = :6.4f}") #表示輸出的寬度最小為6位 且取代小數第四位 沒有的數字會補0


#ax + by = e cx + dy = f
#2x + 3y = 13 x - 2y = -4
# a = 2
# b = 3
# c = 1
# d = 2
# e = 13
# f = -4
# x = (e*d - b*f) / (a*d - b*c)
# y = (a*f - e*c) / (a*d - b*c)
# print(f"{x = :6.4f},    {y = :6.4f}")


# #火箭速度
# v = eval(input("請輸入火箭速度： "))
# if v < 7.9:
#     print("人造衛星無法進入太空")
# elif v == 7.9:
#     print("人造衛星可以繞著地球作圓形移動")
# elif 7.9< v < 11.2:
#     print("人造衛星可以繞著地球作橢圓形移動")
# elif 11.2 <= v < 16.7: #這寫法和 v>= 11.2 and v <16.7 結果相同
#     print("人造衛星可以繞著太陽移動")
# else:
#     print("人造衛星可以離開太陽系")

#計算閏年 首先不可以被4整除 這個條件成立後必須要符合 不能被100整除 或是可以被400整除才是閏年
print("判斷輸入年份是否為閏年")
year = input("請輸入年分: ")
rem4 = int(year) % 4
rem100 = int(year) % 100
rem400 = int(year) % 400
if rem4 == 0:
    if rem100 != 0 or rem400 ==0:
        print(f"{year} 是閏年")
    else:
        print(f"{year} 不是閏年")
else:
    print(f"{year} 不是閏年")