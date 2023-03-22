# employee_file = open("employees.txt", "a") #寫在該檔案的最後
# employee_file.write("\nKelly - Customer Service") #寫入.txt檔案 #不+\n 會直接寫在新寫入資料後面

# employee_file = open("employees1.txt", "w") #w = 覆蓋全部檔案 檔名打不存在的 會新增
# employee_file.write("\nKelly - Customer Services")


employee_file = open("index.html", "w") #w = 覆蓋全部檔案 
employee_file.write("<p>This is HTML</p>")