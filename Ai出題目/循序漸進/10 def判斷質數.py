# def is_prime(number):
#     # 如果數字小於2，則不是質數，返回False
#     if number < 2:
#         return False
    
#     # 判斷從2到number-1的每個數字是否是number的因數
#     for i in range(2, number):
#         if number % i == 0:
#             return False
    
#     # 如果上述循環沒有返回False，則number是質數，返回True
#     return True
# answer = int(input("請輸入一個數字: "))
# result = is_prime(answer)
# print("該數字是不是質數: ", result)



#更詳細解
def is_prime(number):
    # 如果數字小於2，則不是質數，返回False
    if number < 2:
        return False
    
    # 判斷從2到number-1的每個數字是否是number的因數
    for i in range(2, number):
        if number % i == 0:
            return False
    
    # 如果上述循環沒有返回False，則number是質數，返回True
    return True

# 獲取用戶輸入的數字
number = int(input("請輸入一個數字: "))

# 判斷是否為質數
if is_prime(number):
    print(number, "是質數")
else:
    print(number, "不是質數")
