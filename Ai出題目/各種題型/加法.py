# 讀取使用者輸入的數字和運算符號
num1 = float(input("輸入一個數字: "))
num2 = float(input("輸入一個數字: "))
operator = input("輸入一個運算符號 (+,-,*,/): ")

# 根據運算符號計算結果
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("不要亂輸入")
    exit()

# 輸出計算結果，保留兩位小數
print("The result is: {:.2f}".format(result))
