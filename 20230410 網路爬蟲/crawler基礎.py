#抓取 網頁原始碼 (HTML)
import urllib.request as req  #用於向網站發送請求
url = "https://www.ptt.cc/bbs/movie/index.html"
#:"" 這裡的網頁F12 NETWORK內的 user-agent 貼上
#建立一個 Request 物件, 附加 Request Headers 的資訊
request = req.Request(url, headers= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response: #上下文管理器 with抓取資料 response在語句結束時自動關閉並釋放資源
    data = response.read().decode("utf-8")
#print(data) #為了讓自己確定程式有成功抓取到網頁資訊

#解析原始碼，取得每篇文章的標題
#網頁右鍵 開啟網頁原始碼
#如果沒安裝過在終端機安裝 輸入 pip install beautifulsoup4
import bs4
root = bs4.BeautifulSoup(data, "html.parser")  #把data網頁原始碼 丟給 BeautifulSoup去解析成html
#print(root.title) #root整份網頁的<title>內的資訊含<title>
#print(root.title.string)##root整份網頁的<title>內的資訊不含<title>


#titles = root.find("div", class_ = "title") #find只抓其中一個從網頁中尋找(標籤"div", 條件 class = "title")
# print(titles) #代表div
# print(titles.a) #代表<a
#print(titles.a.string) #代表文字
# 第一種方法
titles = root.find_all("div", class_ = "title") #尋找所有符合的
#print(titles)
for title in titles:
    if title.a != None: #如果標題包含 a 標籤 (沒有被刪除)，印出來
        print(title.a.string)

#列表解析式
# titles = root.find_all("div", class_="title")
# filtered_titles = []
# for title in titles:
#     if title.a is not None:  #判斷盪前標題是否包含超連結 
#         filtered_titles.append(title.a.string)  # 將超連結中的文本填加到列表中
# ## titles = [title.a.string for title in titles if title.a is not None] 35 -38行
# print('\n'.join(filtered_titles))

# #使用 filter 函數
# titles = root.find_all("div", class_="title")  # 找到所有 class 為 "title" 的 div 元素
# filtered_titles = filter(lambda x: x.a is not None, titles)  # 過濾掉沒有超鏈接的標題 也就是刪除的不要
# for title in filtered_titles:
#     print(title.a.string)  # 輸出每個超鏈接文本

# #使用 CSS選擇器
# # 選取 class 為 "title" 的 div 元素下的 a 元素
# titles = root.select("div.title > a")
# # 創建一個新的列表，從每個 a 元素中提取文字內容，並將這些內容加入到新列表中
# title_texts = []
# for title in titles:
#     title_texts.append(title.string)
# #titles = [title.string for title in titles] 52-54行
# # 使用 join() 方法將標題列表中的每個元素連接成一個字串，以換行符分隔
# print('\n'.join(title_texts))


