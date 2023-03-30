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

# #刪除串列元素 del 不會返回值 可以指定一個或一個範圍的索引值 或是全部刪除
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

# a = [1, 2, 3]
# print(dir([a])) #列出串列所有內建的方法

# #增加或刪除串列 在串列末端增加元素 這是直接在末尾增加 ->append() 
# cars = ["Honda", "Toyota", "Ford"]
# cars.append("Nissan")
# print(cars)





# #插入串列元素 insert() 可以指定在哪一個索引值中加入
# cars = ["Honda", "Toyota", "Ford"]
# print("目前串列內容等於 = ", cars)
# print("在索引1位置插入Nissan")
# cars.insert(1, "Nissan")
# print("新的索引內容 = ", cars)

# #刪除串列元素 pop() 刪除的是索引值 會返回值
# cars = ["Honda", "Toyota", "Ford", "Nissan"]
# print("目前串列內容 = ", cars)
# poped_car = cars.pop() #()內沒有填索引值刪除末端值
# print("被刪除的串列是 = ", poped_car)
# print("刪除後的串列內容 = ", cars)
# poped_car = cars.pop(1) #刪除索引值1的值
# print("被刪除的串列是 = ", poped_car)
# print("最終剩下的串列內容 = ", cars)

# #刪除指定的元素 remove() 可以刪除的是第一次出現的值 而不是索引值
# cars = ["Honda", "bmw", "Toyota", "Ford", "bmw"]
# print("目前串列的內容為 = ", cars)
# expensive = "bmw" #刪除第一次出現的 () 內可以把bmw 指定存放到變數內
# cars.remove(expensive)
# # cars.remove("bmw") #刪除第一次出現的 可以指定字串
# print(f"所刪除的內容是 : {expensive.upper()} 因為太貴了")
# print("新的字串內容是 = ", cars)

#串列排序
#顛倒排序 reverse()
# cars = ["Honda", "bmw", "Toyota", "Ford", "bmw"]
# print("目前的串列內容 = ", cars)
# #直接列印cars[::-1]顛倒排序 不更改字串內容
# print("列印使用[::-1]顛倒排序\n ", cars[::-1]) #完整意思 [start:end:step] 起始 終點 間隔 結束位置不包含在切片中 所以顛倒排序可以寫 cars[4::-1]
# #更改串列內容
# print("使用reverse()顛倒排序串列元素")
# cars.reverse()
# print("新的串列內容 = ",cars)

#sort() 一定要存放在列表串列[]內由小排到大 英文字建議轉成小寫 永久更改排序
# cars = ["Honda", "BMW", "Toyota", "Ford", "bmw"] #定義一個列表
# new_cars = [] #指定一個空列表存放值
# for car in cars: 
#     new_cars.append(car.lower()) #每執行一次迴圈 car=列表內的不同值 第一次Honda 第二BNW ... ...
# cars = new_cars
# print(cars)
# cars.sort()                   #print(cars.sort()) #無法這樣使用
# print(cars)

# nums = [3, 7, 5, 9, 1] 
# nums.sort()
# print(nums)
#強制在sort內由大排到小 #
# cars = ["honda", "toyota", "bmw", "ford"]
# cars.sort(reverse = True)
# print(cars)

# nums = [1, 2, 3, 4, 6, 8, 9]
# nums.sort(reverse = True)
# print(nums)

# #sorted()排序 從小排到大 原先串列列表內不更動
# cars = ["honda", "toyota", "bmw", "ford"]
# cars_sorted = sorted(cars)
# print("更改過的", cars_sorted)
# print("原先的", cars)
# nums = [9, 8, 7, 6, 5, 4]
# num_sorted = sorted(nums)
# print("更改過的", num_sorted)
# print("原先的", nums)
# #一樣可以由大排到小
# cars = ["honda", "toyota", "bmw", "ford"]
# cars_sorted = sorted(cars, reverse=True)
# print("更改過的", cars_sorted)
# print("原先的", cars)
# nums = [1, 2, 3, 4, 5, 6]
# num_sorted = sorted(nums, reverse=True)
# print("更改過的", num_sorted)
# print("原先的", nums)

#進階操作 index 建議可以搭配in 判斷列表內是否有該元素
# cars = ["toyota", "nissan", "honda"] #0, 1, 2
# search_str = "nissan"
# i = cars.index(search_str) #搜尋  search_str = "nissan" 在cars內的indes是多少 儲存到i
# print(f"所搜尋元素 {search_str} 第一次出現位置索引是 {i}")
# nums = [7, 12, 30, 12, 30, 9, 8]
# search_val = 30
# j = nums.index(search_val)
# print(f"所搜尋元素 {search_val} 第一次出現位置索引是 {j}")

# james = ["Leborn James", 23, 35, 40, 28, 33]
# games = len(james)
# print(games) #這邊我用來判斷 長度 沒有意義 可以刪除
# score_max =max (james[1:games])
# i = james.index(score_max)
# print(f" {james[0]} ,在第 {i} 場砍下最高分 {score_max} ")

# #count () 回傳特地內容出現幾次 搜尋值不在串列內會回傳0
# cars = ["toyota", "honda", "nissan"]
# search_str  = "nissan"
# num1 = cars.count(search_str) #可以直接填字串
# print(f"所搜尋元素 {search_str} 出現 {num1} 次")

# nums = [1, 1, 4, 6, 7, 9, 1, 3, 1, 4, 1]
# search_val = 1
# num2 = nums.count(search_val) #可以直接填數字
# print(f"所搜尋的元素為 {search_val} 出現 {num2} 次")

# #串列含串列
# num = [1, 2, 3, 4, 5, [6, 7, 8]] #0, 1, 2, 3, 4, 5[0,1,2]
# print(num[5][0])
# print(num[5][1])
# print(num[5][2])
# print(num[5])

# James = [["Lebron James", "SF", "12/30/84"], 23, 40, 25,28]
# games = len(James)
# score_Max = max(James[1:games])
# i =James.index(score_Max) 
# name =James[0][0] #名字
# position = James[0][1] #位置
# born = James[0][2] #出生日期
# print("姓名     :", name)
# print("位置     :", position)
# print("出生日期 :", born)
# print(f"在第 {i} 場得最高分 {score_Max}")

# # extend()<- 列表+列表 合併成一個列表
# player1 = ["Harden", "Curry"]
# player2 = ["Green", "字母哥"]
# player1.append(player2)
# print("使用append列印 = ", player1)
# player1 = ["Harden", "Curry"]
# player2 = ["Green", "字母哥"]
# player1.extend(player2)
# print("使用extend列印 = ", player1)



# sc = ["洪錦魁", 80, 95, 88, 0] #0, 1, 2, 3, 4
# sc[4] = sum(sc[1:4]) #這邊1:5也可以 因為5是0 n: n-1
# print(sc[4])
# total_score = sum(sc[1:]) 跟上面相等的加法
# print(total_score)
# print(sc)




sc = [["洪錦魁", 80, 95, 88, 0],
      ["洪冰儒", 98, 97, 96, 0],
      ["洪雨星", 91, 93, 95, 0],
      ["洪冰雨", 92, 94, 90, 0],
      ["洪星雨", 92, 97, 80, 0]
      ]
sc[0][4] = sum(sc[0][1:4]) # 第0層的第四個index[4] = sum(sc[第0層][index1:4-1]) 相加存回index4
sc[1][4] = sum(sc[1][1:4])
print(sc[0])
print(sc[1])