import random 
#這一行是匯入 Python 內建的 random 模組，可以使用其中的 sample 函數，
#用來產生一個指定範圍內的隨機數字。

play_again = "是"  # 初始化玩家是否繼續遊戲的選項為 是

while play_again == "是": 
#進入一個 while 迴圈，只要 play_again 變數的值為 "y"，就會一直執行這個迴圈。

    # 1. 產生隨機答案
    system_answer = random.sample(range(10), 4)
    #random.sample 函數從 0 到 9 的範圍中產生 4 個不重複的數字
    print(system_answer)

    # 2. 取得使用者輸入
    max_guess = 3  # 最大猜測次數
    guess_count = 0  # 已經猜的次數
    guess_chances = 1 #存放剩下幾次機會
    while guess_count < max_guess: 
        user_answer = input("\n輸入四個不重複的數字：")
        if len(user_answer) != 4: #檢查數字長度是不是四
            print("這是四個數字?")
            continue  #避免輸入不正確的數字 導致次數+1
        if len(set(user_answer)) != 4: #檢查數字有沒有重複
            print("亂輸入什麼洨")
            continue #避免輸入不正確的數字 導致次數+1

        # 3. 檢查使用者答案
        a = 0
        b = 0
        for i in range(4): # i=index 0 1 2 3
            if int(user_answer[i]) == system_answer[i]: #輸入數字是str 用int轉成數字
            #檢查輸入數字是不是跟隨機生成的數字在相同位置有相同數字
                a += 1
            elif int(user_answer[i]) in system_answer: #輸入數字是str 用int轉成數字
            #檢查輸入的數字有沒有在隨機生成的數字內有相同但位置不同的的答案
                b += 1
        if a == 4:
            print(f"答對了！ 正確答案是{system_answer} ")
            break  # 猜中了，跳出迴圈
        print(f"你還有 {max_guess - guess_chances} 次機會") #顯示幾次機會
        guess_chances += 1
        guess_count += 1
        if guess_count == max_guess:
            print(f"猜測次數已達上限，正確答案是{system_answer}")
            break  # 超過最大猜測次數，跳出迴圈
        if user_answer != system_answer and guess_count != max_guess:
            print(f"猜錯了！ 您猜了{a}A {b}B")
    
    play_again = input("\n您想再玩一次嗎？(是/否): ")

print("\n遊戲結束，歡迎下次再來玩！\n")
#好幾個版本 終於有一個版本看的懂
#再做修改 並且附上備註