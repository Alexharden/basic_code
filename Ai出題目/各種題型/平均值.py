# 讀取使用者輸入的多個數字
numbers = input("輸入數字: ")

# 將數字以空格分隔後轉成數字列表
number_str_list = numbers.split(",")  # 分隔數字字串，得到數字字串列表 split內為空白就是 空格
number_list = []  # 宣告一個空的數字列表
for num_str in number_str_list:  # 逐一取出數字字串
    num = float(num_str)  # 將數字字串轉成浮點數
    number_list.append(num)  # 將浮點數加入數字列表


# 計算平均值並保留兩位小數
average = sum(number_list) / len(number_list) #數字總和除上字串長度
average = round(average, 2)

# 輸出計算結果
print("計算的結果是:", average)
