# score = [35, 46, 57, 91, 29]
# result = []

# for number in score:
#     reversed_score = str(number)[::-1]
#     result.append(reversed_score)

# a = result

# print(a)

# def count_chars(text):
#     char_counts = {} #空字典儲存數字和字母
#     for char in text:
#         if char.isalnum(): #只記字母和數字
#             char_is_lower = char.lower() #將所有字母轉換為 小寫
#             char_counts[char_is_lower] = char_counts.get(char_is_lower, 0) + 1 #
    
#     # sorted_char_counts = dict(sorted(char_counts.items())) #sorted排序 items 元組列表  dict存回字典
#     sorted_char_counts = sorted(char_counts.items())
#     return sorted_char_counts 

# text = "Hello welcome to Cathay 60th year anniversary"
# char_counts = count_chars(text)
# # print(char_counts)
# for char, result in char_counts:
#     print(char, result)


player_num = int(input("輸入本場遊戲人數: "))
total_list = [""]
for i in range(1, player_num + 1):
    total_list.append(i)
print(total_list)

# while len(total_list) <= 1:
count = 1
index = 0

while len(total_list) > 1:
    if count == 3 :
        total_list.remove(total_list[index])
        count = 1
    else:
        index += 1
        count += 1

    if index >= len(total_list):
        index = 0
print(total_list)


