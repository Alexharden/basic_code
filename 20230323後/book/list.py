# james = [1, 3, 5, 7, 9] 
# print("索引值使用", [0])
# print("索引值使用", [1])
# print("索引值使用", [2])

# harden = [
#     [1, 3, 5],
#     [2, 4, 6],
#     [7, 8, 9]
# ]
# print("多重串列索引值使用", harden[0][2])#變數名稱與中括號中間無空格
# print("多重串列索引值使用", harden[1][0])
# print("多重串列索引值使用", harden[2][1])

# #串列切片
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(x[:3]) #012 不含3的索引值
# print(x[:-3]) #從後面數-1-2-3 
# print(x[3:]) #從3開始含3的索引值
# print(x[-3:])#從-3開始含-3

# score = [18, 20, 26, 21, 30] 
# print("1-3場的得分", score[0:3]) #從0開始不包含3 0, 1, 2
# print("2-4場的得分", score[1:4]) #從1(索引值)開始不包含4 1, 2, 3
# print("1、3、5場的得分", score[0:6:2])# 0起始位置 6結束位置(不包含6)不過這一題只有5個數字所以全包含 2是每隔兩個元素抓一次 所以是index值0,2,4

# warriors = ["Curry", "Green", "Thompson", "Bell", "Iquodala"]
# first3 = warriors[:3] #也就是前三名 index 0,1,2
# print("前三名球員", first3)
# n_to_Last = warriors[1:] #從index值1開始包含1
# print("球員索引1到最後", n_to_Last)
# Last3 = warriors[-3:]
# print("後三名球員", Last3)

# mixs = [9, 5.1, "Deepmind"]
# print("最後一個元素", mixs[-1])

# a = [1, 3, 5, 7, 9]
# print(a[-1], a[-2], a[-3], a[-4], a[-5])

# #max(最大值) min(最小值)
# james = [23, 19, 22, 31, 18]
# print("最高得分 = ", max(james))
# print("最低得分 = ", min(james))
# print("總得分 = ", sum(james))

# #含字串符號的 字串切片
# james = ["Leborn James", 23, 19, 22, 31, 18]
# print("最高得分 = ", max(james[1:6]))
# print("最低得分 = ", min(james[1:6]))
# print("總得分 = ", sum(james[1:6]))

# #len 計算列表內的長度
# james = [23, 19, 22, 31, 18]
# games = len(james)
# print(f"經過{games} 場比賽最高得分 = {max(james)}")
# print(f"經過{games} 場比賽最低得分 = {min(james)}")
# print(f"經過{games} 場比賽的總得分 = {sum(james)}")

# #更改列表的元素
# a = [1, 3, 5, 7, 8] #index 0,1,2,3,4
# print("舊的列表", a)
# a[4] = 9
# print("新的列表", a)  

# cars = ["Toyota", "Nissan", "Mazda"]
# print("舊汽車銷售品牌", cars)
# cars[2] = "Honda"
# print("新汽車銷售品牌", cars)

# #字串相加、整數相加 
# cars1 = ["Toyota", "Nissan", "Mazda"]
# cars2 = ["Audi", "BMW"]
# cars3 = cars1 + cars2
# print(cars3)
# numbers1 = [0, 1, 2, 3]
# nunbers2 = [4, 5, 6]
# numbers3 = numbers1 + nunbers2
# print(numbers3)

#列表*數字  串列無法加數字 numslist = nums +5 這樣會報錯
# cars = ["Toyota", "Nissan", "Mazda"]
# nums = [1, 3, 5]
# carslist = cars * 5
# print(carslist)
# numslist = nums * 5
# print(numslist)

# #串列元素加法
# James = ["Lebron James", 23 ,19, 24, 26, 25] #0,1,2,3,4,5
# Love = ["Kevin Love", 20, 15, 18, 30, 21]
# games3 = James[4] + Love[4]
# LKgame = James[0] + "和" + Love[0] + "第四場總得分 = "
# print(LKgame, games3)

# #刪除串列元素
# warriors = ["Curry", "Durant", "Iquodala", "Green", "Thompson"]
# print("勇士隊最強陣容", warriors)
# del warriors[1] #刪除串列內該索引值的值
# print("勇士隊沒有大腿的陣容", warriors)

# num1 = [1, 3, 5]
# del num1[0] 
# print("刪除index0後 ", num1)
# num2 = [1, 2, 3, 4, 5, 6, 7]
# del num2[0:2] #刪除0,1
# print("刪除index0,1後 ", num2)
# num3 = [1, 2, 3, 4, 5, 6]
# del num3[0:6:2] #0刪除 空1格 刪除
# print("刪除從0開始到index5結束每兩位抓一次", num3)

# #if 指令加上列表
# cars = ["Toyota", "Nissan", "Honda"]
# print(f"cars串列長度是 = {len(cars)}")
# if len(cars) != 0:
#     del cars[0]
#     print("刪除cars串列元素成功")
#     print(f"cas串列長度是 = {len(cars)}")
# else:
#     print("cars串列內沒有元素資料")
# nums = []
# print(f"nums串列長度是 = {len(nums)}")
# if len(nums):
#     del nums[0]
#     print("刪除nums串列元素成功")
# else:
#     print("nums串列內沒有元素資料")

# #補充多重指令與串列 打包  *無法放在開頭
# a, b, *c = 1, 2, 3, 4, 5 
# print(a, b, c) ##abc都各要一個元素 a = 1 b =2 剩下來的全部都給c
# a, *b, c = 1, 2, 3, 4, 5
# print(a, b, c) ##abc都各要一個元素 a = 1 c =5 剩下來的全部都給b

# #更改字串大小寫 lower() upper() title() swapcase()
# cars = ["bmw", "benz", "audi"]
# carF = "我開的第一部車是" + cars[1].title() ##在後面用點() title單字開頭大寫
# carN = "我現在開的車子是" + cars[0].upper() ##在後面用點() upper所有字變成大寫
# print(f"{carF}, \n{carN}")

# x = "i love you"
# x = x.title() ##在後面用點() title單字開頭大寫
# print(x)

# y = "OH MY GOD"
# y = y.title() ##在後面用點() title單字開頭大寫 可以這樣把全大寫的字保留只有開頭大寫其他轉成小寫
# print(y)

# z = "ABC" 
# z = z.lower() ##變成小姐
# print(z)

# c = "Apple"
# c = c.swapcase() ##把大小寫反過來
# print(c)

#刪除空白字元 rstrip() lstrip() strip()
# StrN = " DeepStone "
# StrL = StrN.lstrip() ##刪除字串左邊多餘空白
# StrR = StrN.rstrip() ##刪除字串右邊多餘空白
# StrB = StrN.lstrip() ##先刪除字串左邊多餘空白
# StrB = StrN.rstrip() ##再刪除字串右邊多餘空白
# StrO = StrN.strip() ##一次刪除頭尾多餘空白 
# print(f"/{StrL}/")
# print(f"/{StrR}/")
# print(f"/{StrB}/")
# print(f"/{StrO}/")

# string = input("請輸入名字 : ")
# print(f"/{string}/")
# string = input("請輸入名字 : ")
# print(f"/{string.strip()}/")
#也可以這樣
# string = input("請輸入名稱 : ").strip()
# print(string)
# string = input("請輸入名稱 : ").strip().title()
# print(string)

# #格式化字串位置 center() ljust() rjust() zfill()
# title = "Ming-Chi Institute of TechnoLogy"
# print(f"/{title.center(100)}/") ##置中 總長度
# dt = "Department of ME"
# print(f"/{dt.ljust(50)}") ##靠左 總長度
# site = "JK Hung"
# print(f"{site.rjust(50)}")
# print(f"{title.zfill(50)}") ##長度總共要50 (width) 元字串向右靠 左邊不夠的的補0

# #islower() isupper() isdigit() isalpha() 
# s = "abc"
# print(s.isupper())##判斷是否全部都大寫
# print(s.islower())##判斷是否全部都小寫
# print(s.isdigit())##判斷是否全部都數字
# print(s.isalpha())##判斷是否全部都是英文字
# n = "123"
# print(n.isdigit())##判斷是否全部都數字
# print(n.isalpha())##判斷是否全部都是英文字

# # #dir()列出所有系統內建物見的方法(method)
# string = "abc" ##先隨便設定一個變數內有字串數字
# print(dir(string))
# help(string.islower) ##詳細解析函數的用法
# num = 5
# # dir(num)
# # help(num.bit_length)
# y = num.bit_length() #10進位轉成2進位
# print(y)
# num = 31 #10進位轉成2進位 11111 有5個
# y = num.bit_length()
# print(y)

a = [1, 2, 3]
print(dir([a])) #列出串列所有內建的方法
