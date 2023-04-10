def find_longest_word(sentence): #函式名稱 參數 
    # 將句子分割成單詞並存儲在一個列表中
    words = sentence.split()

    # 使用 max 函數找到最長的單詞
    longest_word = max(words, key=len)

    return longest_word

# 測試函數
sentence = input("請輸入一串英文句子: ")
longest_word = find_longest_word(sentence)
print("在句子中最長的單詞是：", longest_word)
