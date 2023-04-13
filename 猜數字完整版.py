import random


while True:
    play_game = input("\n是否要開始猜數字遊戲？(請輸入 y 或 n)：") # 詢問使用者是否要開始遊戲
    if play_game.lower() == "y":
        # 開始遊戲
        break
    elif play_game.lower() == "n":
        print("\n你不想玩點進來幹嘛?\n")
        continue
    else:
        print("\n蝦雞掰輸入?\n")
        continue

print("\n歡迎來到猜數字遊戲")
if play_game.lower() == "y": # 如果使用者輸入 y，則開始遊戲
    ans = random.randint(1,100) # 從數字列表中隨機選一個數字
    guess = 0
    i = 1
    r = 100
    
    while True: # 使用 while True 來詢問是否重啟遊戲
        while guess != ans: # 使用 while 迴圈來不斷詢問使用者輸入，直到猜對為止
            print(f"這題的答案是: {ans}\n") 
            try:
                guess = int(input(f"\n請猜一個 {i} 到 {r} 之間的數字：")) # 詢問使用者輸入猜測的數字
                 
            except ValueError: # 如果使用者輸入的不是數字，則進行錯誤處理
                print("請輸入數字！\n")
                continue    
            if guess < ans: # 如果猜測的數字小於答案，提示使用者往大的方向猜
                print("\n猜錯了，請往大的方向猜！\n")
                i = guess
            elif guess > ans: # 如果猜測的數字大於答案，提示使用者往小的方向猜
                print("\n猜錯了，請往小的方向猜！\n")
                r = guess
            else: # 如果猜對了，則顯示猜對的訊息
                print("\n恭喜你猜對了！\n")

        play_again = input("遊戲結束，是否要再玩一次？(請輸入 y 或 n)： ") # 詢問使用者是否要重新開始遊戲
        if play_again.lower() == "y": # 如果使用者輸入 y，則重新選擇答案並重新開始遊戲
            ans = random.randint(1,100)
            guess = 0
            continue
        elif play_again.lower() == "n": # 如果使用者輸入 n，則結束程式
            print("\n\n@@@!!!滾囉!!!@@@\n\n")
            break
        else: # 如果使用者輸入的不是 y 或 n，則提示使用者輸入錯誤並讓他再輸入一次

            print("\n你再亂輸入沒差，請輸入 y 或 n！\n")
            continue