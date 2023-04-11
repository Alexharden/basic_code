def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result

user_num = int(input("請輸入一個數字: "))
print("數字1到",user_num,"的平方總和為", sum_of_squares(user_num)) # 
