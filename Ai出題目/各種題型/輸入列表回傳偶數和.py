def sum_of_even(numbers):#定義一個名為 sum_of_even 的函數，這個函數接受一個整數列表 numbers 作為參數。
    sum = 0 #定義一個名為 sum_of_even 的函數，這個函數接受一個整數列表 numbers 作為參數。
    for num in numbers: #使用 for 循環遍歷整數列表中的每個元素。
        if num % 2 == 0: #判斷是否為偶數
            sum += num #是的話相加
    return sum #回傳

user_input = input("請輸入整數列表，數字之間以空格分隔：") #因為下方split預設為空格分隔 所以提示要求空格
input_list = [] 
for i in user_input.split(): #分割字串
    input_list.append(int(i)) #將每一個偶數數字存入空列表內
result = sum_of_even(input_list) #呼叫自訂的def函數 讓列表內的偶數相加並回傳
print(result)
