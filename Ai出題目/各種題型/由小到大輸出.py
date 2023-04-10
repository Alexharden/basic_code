# # 提示用戶輸入三個數字
# numbers = input("請輸入三個數字（以空格分隔）：")

# # 創建一個空的列表
# num_list = []

# # 遍歷用戶輸入的每個數字，將其轉換為整數並添加到列表中
# for num in numbers.split():
#     num_list.append(int(num))

# # 將列表中的元素從小到大排序
# num_list.sort()

# # 創建一個空的輸出字串
# output_string = ""

# # 遍歷已排序的列表中的每個數字，將其轉換為字串並添加到輸出字串中
# for num in num_list:
#     output_string += str(num) + " "

# # 刪除輸出字串中的最後一個空格
# output_string = output_string[:-1]

# # 輸出已排序的數字列表
# print(output_string)


# # 要求用戶輸入 5 個整數，以空格分隔 使用for循環排序
# nums_str = input("請輸入 5 個整數：")
# nums_list = nums_str.split()

# # 將輸入的整數列表轉換為整數類型
# nums = []
# for num in nums_list:
#     nums.append(int(num))

# # 將整數列表從小到大排序
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] > nums[j]:
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp

# # 將排序後的整數列表轉換為字串，並以空格分隔整數
# output_str = ""
# for num in nums:
#     output_str += str(num) + " "

# # 移除字串末尾的空格
# output_str = output_str.strip()

# # 輸出排序後的整數列表
# print(output_str)


# numbers = input("請輸入三個數字（以空格分隔）：")
# num_list = list(map(int, numbers.split())) #split 分隔 int轉換成整數 map存到list內
# num_list.sort() #由小到大排序 num_list被改變
# print(num_list)
# print(",".join(map(str, num_list)))  #.join 取消列表[] 以字串分隔 


numbers = input("請輸入三個數字（以空格分隔）：")
num_list = list(map(int, numbers.split())) #split 分隔 int轉換成整數 map存到list內
answer = sorted(num_list) #由小到大排序 但不會改變 原來的num_list
print(answer)

