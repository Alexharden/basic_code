# 蛇式命名法，在各單字之間用下底線做分隔，且所有字母均小寫，例如: “hello_world”就是蛇式命名法格式的字串。

# 輸入: 
# 任意字串，字串長度不能超過1000，且字串中只能有大小寫英文字母和數字。用大寫字母區分各個單字
# 舉例 IHaveAPenIHaveAAppleEhhhApplePen
# 輸出:
# i_have_a_pen_i_have_a_apple_ehhh_apple_pen

# 輸入:
# TodayIsAGoodDayToPicnic

# 輸出:
# today_is_a_good_day_to_picnic

# 輸入:
# Bye! ViewSonic

# 輸出:
# {Because include invalid characters, print custom Error Message}





user = input("輸入任意字串(英文或數字): ")
answer = ""
#判斷字串長度有無超過 1000 超過則 重複輸入 直到使用者長度少於1000
while len(user) > 1000:  
    print("字串長度超過1000")
    user = input("請重新輸入任意字串(英文或數字): ")

for i in range(len(user)):
    if user[i].isalnum(): #判斷輸入該Index的字串是否為英文和數字
        if user[i].isupper():#判斷輸入該Index的字串是否為大寫
            answer += "_" + user[i].lower() #是的話將大寫字串轉換成小寫並在字串前面加上_
        else:
            answer+= user[i] #如果不是大寫字串
    else:#輸入的字串非英文和數字
        print("{Because include invalid characters, print custom Error Message}")
        break

if answer: #判斷使用者是不是輸入 空白字串 如果沒有這一行 輸入空白字串會出錯
    if answer[0] == "_": #如果輸入AppleApple結果會是_apple_apple 所以這時候來判斷是index[0]是不是_
        answer = answer[1:] #從第二格開始輸出就等於刪除[0]的_
print(answer)
    