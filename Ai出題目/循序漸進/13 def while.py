# #使用return
# def sum_to_n(number):
#     sum = 0
#     num = 1
#     while num <= n:
#         sum += num
#         num += 1
#     return sum
    
# n = int(input("請輸入一個正整數："))
# result = sum_to_n(n)
# print("從 1 到", n, "的和為：", result)

#使用return 2
def sum_to_n(number):
    sum = 0
    num = 1
    while num <= n:
        sum += num
        num += 1
    return sum
    
n = int(input("請輸入一個正整數："))
print("從 1 到", n, "的和為：", sum_to_n(n))


# #不使用return
# def sum_to_n(number):
#     sum = 0
#     num = 1
#     while num <= n:
#         sum += num
#         num += 1
#     print(sum)
# n = int(input("請輸入一個正整數："))
# sum_to_n(n)


