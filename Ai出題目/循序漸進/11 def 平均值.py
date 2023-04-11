#解法 1
def calculate_average(lst):
    if len(lst) == 0:
        return 0
    else:
        return sum(lst) / len(lst)

# 提示用戶輸入數字
user_input = input("請輸入數字，以空格分隔: ")

# 將用戶輸入的字符串轉換為整數列表
user_list = list(map(int, user_input.split()))

# 調用calculate_average函數計算平均值
average = calculate_average(user_list)

# 輸出結果
print("平均值為:", average)



#解法 2 def內直接 print結果
def calculate_average(lst):
    if len(lst) == 0:
        print("列表為空")
    else:
        average = sum(lst) / len(lst)
        print("平均值為:", average)

# 提示用戶輸入數字
user_input = input("請輸入數字，以空格分隔: ")

# 將用戶輸入的字符串轉換為整數列表
user_list = list(map(int, user_input.split()))

# 調用calculate_average函數計算平均值
calculate_average(user_list)

