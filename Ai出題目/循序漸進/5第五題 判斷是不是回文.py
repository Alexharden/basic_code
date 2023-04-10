def is_palindrome(word):
    return word == word[::-1]

word = input("請輸入一個單詞：")
if is_palindrome(word):
    print(word, "是回文。")
else:
    print(word, "不是回文。")
