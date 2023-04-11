# #解法 1 不使用 max和min 
# def calculate_max_min_diff(lst):
#     if len(lst) == 0:
#         print("列表为空")
#     else:
#         max_num = lst[0]
#         min_num = lst[0]
#         for num in lst:
#             if num > max_num:
#                 max_num = num
#             if num < min_num:
#                 min_num = num
#         result = max_num - min_num
#         print("最大值是:", max_num)
#         print("最小值是:", min_num)
#         print("最大值和最小值之差是:", result)

# user_num = input("輸入數字，以空格分隔: ")
# user_list = list(map(int, user_num.split()))

# calculate_max_min_diff(user_list)



# #解法2 不使用max 和 min
# def calculate_max_min_diff(lst):
#     if len(lst) == 0:
#         print("列表为空")
#     else:
#         max_num = lst[0]
#         min_num = lst[0]
#         for num in lst:
#             if num > max_num:
#                 max_num = num
#             if num < min_num:
#                 min_num = num
#         diff = max_num - min_num
#         return max_num, min_num, diff

# user_num = input("輸入數字，以空格分隔: ")
# user_list = list(map(int, user_num.split()))
# max_num, min_num, result = calculate_max_min_diff(user_list)
# print("最大值是:", max_num)
# print("最小值是:", min_num)
# print("結果是:", result)

# #解法3 如果只要結果 不要最大最小值可以這樣寫
# def calculate_max_min_diff(lst):
#     if len(lst) == 0:
#         print("列表为空")
#     else:
#         max_num = lst[0]
#         min_num = lst[0]
#         for num in lst:
#             if num > max_num:
#                 max_num = num
#             if num < min_num:
#                 min_num = num
#         return  max_num - min_num
        

# user_num = input("輸入數字，以空格分隔: ")
# user_list = list(map(int, user_num.split()))
# result = calculate_max_min_diff(user_list)
# print("結果是:", result) #或者不寫result 直接print(calculate_max_min_diff(user_list)



# #解法4 def 內不使用 max 和 min
# def calculate_max_min_diff(lst):
#     if len(lst) == 0:
#         print("列表为空")
#     else:
#         max_num = lst[0]
#         min_num = lst[0]
#         for num in lst:
#             if num > max_num:
#                 max_num = num
#             if num < min_num:
#                 min_num = num
#         return  max_num - min_num
        

# user_num = input("輸入數字，以空格分隔: ")
# user_list = list(map(int, user_num.split()))
# result = calculate_max_min_diff(user_list)
# print("最大值為: ", max(user_list))
# print("最小值為: ", min(user_list))
# print("結果為: ", result)





# #解法5 使用max min
# def calculate_max_min_diff(lst):
#     if len(lst) == 0:
#         print("列表为空")
#     else:
#         max_num = max(lst)
#         min_num = min(lst)
#         return max_num - min_num
       

# user_num = input("輸入數字，以空格分隔: ")
# user_list = list(map(int, user_num.split()))
# result = calculate_max_min_diff(user_list)
# print("最大值是:", max(user_list))
# print("最小值是:", min(user_list))
# print("結果是:", result)
