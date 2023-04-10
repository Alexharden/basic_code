# user_str = input("請輸入一串文字: ")
# user_list = list(user_str) #轉成列表
# user_list.reverse() #需要轉換成列表才能使用reverse
# answer = "".join(user_list) #取消列表用join 變成字串
# print(answer)


#slice 反轉字串
user_str = input("請輸入一串文字: ")
answer = user_str[::-1]
print(answer)