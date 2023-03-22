#網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response: #response 資料讀取下來
#     data = response.read().decode("utf-8") #取得台灣大學網站的原始碼(HTML、 CSS、JS)
# print(data)

#串接、擷取公開資料
import urllib.request as request
import json
src="https://quality.data.gov.tw/dq_download_json.php?nid=151346&md5_url=ccd92bef86fcfca9e7876468726622c0"
with request.urlopen(src) as response: #response 資料讀取下來
    data = json.load(response) #利用 json 模組處理 json 資料格式
# print(data) 確認讀取到資料
clist = data["result"]["results"]  #這一行開始配這個網址是錯的
with open("data.txt","w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"] + "\n")
#沒寫完