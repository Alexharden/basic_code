# import urllib.request as req
# url = "https://www.ptt.cc/bbs/movie/index.html"
# request = req.Request(url, headers= {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")
# import bs4
# root = bs4.BeautifulSoup(data, "html.parser")
# titles = root.find_all("div", class_ = "title")
# for title in titles:
#     try:
#         print(title.a.string)
#     except AttributeError:
#         print("None")
        
# #這個是只印刪除
# import urllib.request as req
# url = "https://www.ptt.cc/bbs/movie/index.html"
# request = req.Request(url, headers= {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# })
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")
# import bs4
# root = bs4.BeautifulSoup(data, "html.parser")
# titles = root.find_all("div", class_ = "title")
# for title in titles:
#     if title.a is None:
#         print(title.text.strip())


#美觀寫法 包含刪除使用strip()取消前後空格
# # 匯入模組
# import urllib.request as req
# import bs4

# # 設定 URL 以及 request header
# url = "https://www.ptt.cc/bbs/movie/index.html"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# }

# # 建立 Request 物件並發送請求
# request = req.Request(url, headers=headers)
# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")

# # 使用 Beautiful Soup 解析 HTML 網頁
# root = bs4.BeautifulSoup(data, "html.parser")

# # 尋找所有標籤名稱為 div，且 class 為 "title" 的元素
# titles = root.find_all("div", class_="title")

# # 迭代每個 title
# for title in titles:
#     # 如果 title 有超連結標籤 a，則印出 a 標籤的字串
#     if title.a is not None:
#         print(title.a.string)
#     # 如果 title 沒有超連結標籤 a，但文字不是空白，則印出文字內容
#     elif len(title.text.strip()) > 0: #strip是取消兩端的空格
#         print(title.text.strip())


#不美觀寫法
# import urllib.request as req
# import bs4

# url = "https://www.ptt.cc/bbs/movie/index.html"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# }

# request = req.Request(url, headers=headers)

# with req.urlopen(request) as response:
#     data = response.read().decode("utf-8")

# root = bs4.BeautifulSoup(data, "html.parser")

# titles = root.find_all("div", class_="title")
# for title in titles:
#     if title.a is not None:
#         print(title.a.string)
#     elif title.text != "":
#         print(title.text)


