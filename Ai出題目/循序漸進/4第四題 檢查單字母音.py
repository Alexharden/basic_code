# 定義一個函數 count_vowels，用來計算單詞中的元音字母數量
def count_vowels(word):
    count = 0
    vowels = "aeiou"
    # 遍歷單詞中的每一個字母
    for letter in word:
        # 將字母轉成小寫，並檢查是否是元音字母
        if letter.lower() in vowels:
            count += 1
    # 返回元音字母的數量
    return count

# 讓用戶輸入一個單詞
word = input("請輸入一個單詞：")
# 調用 count_vowels 函數，計算單詞中的元音字母數量
vowel_count = count_vowels(word)
# 將結果輸出到控制台
print("在該單詞中有", vowel_count, "個元音字母。")
