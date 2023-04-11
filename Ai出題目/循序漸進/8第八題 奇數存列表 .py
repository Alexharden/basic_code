# 定義一個函數，用於獲取列表中的奇數元素
def odd_elements(input_list):
    # 創建一個新的列表，用於存儲奇數元素
    odd_list = []
    
    # 遍歷輸入列表中的所有元素
    for element in input_list:
        # 如果元素是奇數且大於0，添加到奇數元素列表中
        if element % 2 == 1 and element > 0:
            odd_list.append(element)
    
    
    # 返回新的奇數元素列表
    return odd_list

# 獲取用戶輸入的數字字符串，並將其轉換為整數列表
input_list = input("輸入幾個數字吧: ")
input_list = input_list.split()
new_list = []
for x in input_list:
    new_list.append(int(x))

# 呼叫 odd_elements 函數獲取奇數元素列表，並將結果存儲在 result 中
# result = odd_elements(new_list)   #這段可以不用 如果要使用 在結果的時候要使用變數 result

# # 輸出結果
print("奇數結果為",  odd_elements(new_list)) 





# #不同解法 在def內定義使用print 最後直接呼叫

# 定義一個函數，用於獲取列表中的奇數元素
def odd_elements(input_list):
    # 創建一個新的列表，用於存儲奇數元素
    odd_list = []
    
    # 遍歷輸入列表中的所有元素
    for element in input_list:
        # 如果元素是奇數且大於0，添加到奇數元素列表中
        if element % 2 == 1 and element > 0:
            odd_list.append(element)
    print(odd_list)
    
    # 返回新的奇數元素列表
    return odd_list

# 獲取用戶輸入的數字字符串，並將其轉換為整數列表
input_list = input("輸入幾個數字吧: ")
input_list = input_list.split()
new_list = []
for x in input_list:
    new_list.append(int(x))

# 呼叫 odd_elements 函數獲取奇數元素列表，並將結果存儲在 result 中
odd_elements(new_list)