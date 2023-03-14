# employee_file = open("employees.txt", "r")   #同文件夾可以直接寫檔名
 #r(read)讀 w(write)寫,修改 a(pan)將訊息加到最後,無法修改改變任何東西
 #r+ (read+write) 可閱讀和修改
#print(employee_file.readable()) #給布林值True or False
# print(employee_file.read()) #讀取該文件內的資料
# print(employee_file.readline()) #讀取單獨第一行
# # print(employee_file.readline())# 一直用readline就是一直往下寫
# print(employee_file.readlines()[0]) #取代重複一直寫readline []裡面寫index值
#employee_file.close() #關閉文件不能在訪問



# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
#employee_file.close() #關閉文件不能在訪問

#可以選取特定幾行
# employee_file = open("employees.txt", "r")
# lines = employee_file.readlines() #把檔案  儲存在一個列表中
# for i in range(3):
#     print(lines[i])
# employee_file.close() #關閉文件不能在訪問

#讀取特定幾行且不換行
employee_file = open("employees.txt", "r")
lines = employee_file.readlines() #把檔案  儲存在一個列表中

for i in range(3):
    print(lines[i].strip(), end= ", ") #strip取消文檔中的換行符號
employee_file.close() 