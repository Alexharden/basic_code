# def first_unique_char(s):
#     # 統計每個字符出現的次數
#     counts = {}
#     for c in s:
#         if c in counts:
#             counts[c] += 1
#         else:
#             counts[c] = 1

#     # 找到第一個出現次數為 1 的字符
#     for c in s:
#         if counts[c] == 1:
#             return c

#     # 如果沒有符合條件的字符，返回一個空格
#     return ' '

# user = input("請輸入: ")
# print("第一個出現不重複的字母為: ", first_unique_char(user))




# #第二種寫法
# def first_unique_char(s):
#     for c in s:
#         if s.count(c) == 1:
#             return c
#     return ' '
# user = input("請輸入: ")
# print("第一個出現不重複的字母為: ", first_unique_char(user))


#更好的寫法 區分大小寫
def first_unique_char(s):
    s = s.lower()
    for c in s:
        if s.count(c) == 1:
            return c
    return ' '
user = input("請輸入: ")
print("第一個出現不重複的字母為: ", first_unique_char(user))
