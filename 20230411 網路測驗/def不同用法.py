#寫一個函數 add_numbers(a, b)，該函數接收兩個整數並返回它們的和。
def add_numbers(a, b):  # 定義一個函數 add_numbers，接收兩個參數 a 和 b
    return a + b       # 執行 a + b 運算，返回結果

num1 = 10              # 定義變數 num1，賦值為 10
num2 = 20              # 定義變數 num2，賦值為 20
result = add_numbers(num1, num2)  # 調用 add_numbers 函數，將 num1 和 num2 傳遞進去，並將結果存儲在變數 result 中
print("The sum of", num1, "and", num2, "is", result)  # 使用 print 函數顯示結果






#寫一個函數 count_characters(sentence)，該函數接收一個句子並返回其中的字符數量（不包括空格）。
# 定義一個計算字元數量的函數
def count_characters(sentence):
    count = 0
    # 遍歷句子中的每個字元，若不是空格則計數器加 1
    for char in sentence:
        if char != " ":
            count += 1
    # 返回計數器的值
    return count

# 測試函數
text = "The quick brown fox jumps over the lazy dog"
char_count = count_characters(text)
print("There are", char_count, "characters in the sentence.")
#程式說明：
# 定義一個名為 count_characters 的函數，它接收一個參數 sentence，代表待計算字元數量的句子。
# 初始化計數器 count 為 0。
# 遍歷句子中的每個字元，若該字元不是空格，則將計數器加 1。
# 最後返回計數器的值。
# 測試函數，將一個句子作為參數傳入 count_characters 函數，並將返回值儲存在變數 char_count 中。
# 使用 print 函數輸出字元數量的結果。





#寫一個函數 find_average(numbers)，該函數接收一個數字列表並返回它們的平均值。

# 定義一個函數 find_average，接收一個數字列表作為參數
def find_average(numbers):
    # 初始化變數 sum 和 count
    sum = 0
    count = 0
    # 遍歷數字列表，將每個數字加總到 sum 中，計數器 count 加 1
    for num in numbers:
        sum += num
        count += 1
    # 返回平均值，即總和除以計數器
    return sum / count

# 定義一個數字列表
num_list = [1, 2, 3, 4, 5]
# 調用函數 find_average，計算平均值
average = find_average(num_list)
# 輸出結果
print("The average of", num_list, "is", average)
