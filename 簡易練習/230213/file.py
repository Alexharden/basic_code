#儲存檔案
# file = open("data.txt", mode="w" ,encoding="utf-8") #開啟 #編碼
# file.write("早安 she ") # 操作
# file.close() #關閉
# with open("data.txt", mode="w", encoding="utf-8") as file: #最佳實務寫法 不用close 自動關閉
#     file.write("5\n3")

#讀取檔案
#把檔案中的數字資料,一行一行讀取出來,並計算加總
# sum = 0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     for line in file: #一行一行讀取
#         sum += int(line) #轉成整數數字 加總
#     # data=file.read()  #讀取文件內所有檔案
# print(sum)

#使用 JSON 格式讀取、 複寫檔案
# import json
# with open("config.json", mode="r") as file:
#     data = json.load(file)
# print(data) #data 是一個字典資料
# print("name", data["name"])
# print("version", data["version"])


import json
#從檔案中讀取JSON資料, 放入變數 data裡面
with open("config.json", mode="r") as file:
    data = json.load(file)
print(data) #data 是一個字典資料
data["name"]="New Name" #修改變數中的資料
#把最新的資料複寫到檔案中
with open("config.json", mode="w") as file:
    json.dump(data,file)
