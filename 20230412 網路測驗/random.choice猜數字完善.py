from random import choice

romove_numbers = input("請輸入你這次猜數字不要的數字 用空格分開: ").split()
avoid_lt = []
for i in romove_numbers:
    avoid_lt.append(int(i))
#ans_lt = [i for i in range(1, 101) if i not in avoid_lt] # 使用列表生成式來產生不包含避開的數字的數字列表
ans_lt = []
for i in range(1, 101):
    if i not in avoid_lt:
        ans_lt.append(i)
        
play_game = input("是否要開始猜數字遊戲？(請輸入 y 或 n)：") # 詢問使用者是否要開始遊戲

if play_game.lower() == "y": # 如果使用者輸入 y，則開始遊戲
    ans = choice(ans_lt) # 從數字列表中隨機選一個數字
    guess = 0
    i = 1
    r = 100
    print(f"這題的答案是: {ans}")  
    while True: # 使用 while True 來詢問是否重啟遊戲
        while guess != ans: # 使用 while 迴圈來不斷詢問使用者輸入，直到猜對為止
            try:
                guess = int(input(f"請猜一個 {i} 到 {r} 之間的數字：")) # 詢問使用者輸入猜測的數字
            except ValueError: # 如果使用者輸入的不是數字，則進行錯誤處理
                print("請輸入數字！")
                continue    
            if guess < ans: # 如果猜測的數字小於答案，提示使用者往大的方向猜
                print("猜錯了，請往大的方向猜！")
                i = guess
            elif guess > ans: # 如果猜測的數字大於答案，提示使用者往小的方向猜
                print("猜錯了，請往小的方向猜！")
                r = guess
            else: # 如果猜對了，則顯示猜對的訊息
                print("恭喜你猜對了！")

        play_again = input("遊戲結束，是否要再玩一次？(請輸入 y 或 n)： ") # 詢問使用者是否要重新開始遊戲
        if play_again.lower() == "y": # 如果使用者輸入 y，則重新選擇答案並重新開始遊戲
            ans = choice(ans_lt)
            guess = 0
            continue
        elif play_again.lower() == "n": # 如果使用者輸入 n，則結束程式
            print("滾囉")
            break
        else: # 如果使用者輸入的不是 y 或 n，則提示使用者輸入錯誤並讓他再輸入一次

            print("你再亂輸入沒差，請輸入 y 或 n！")
            continue
elif play_game == "n":
    print("你不想玩點進來幹嘛?")
    exit()
else:
    print("蝦雞掰輸入?")
    exit