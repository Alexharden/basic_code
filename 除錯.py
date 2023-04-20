# try:
#     a = 1
#     b = '1'
#     print(a+b)
# except Exception as e:  #如果單純使用 except Exception as e，也能將所有的錯誤資訊全部印出。
#     print(e)



# try:
#     a = int(input('輸入 0～9：'))
#     if a>10:
#         raise
#     print(a)
# except :
#     print('有錯誤喔～')
# else:
#     print('沒有錯！繼續執行！')       # 完全沒錯才會執行這行
# finally:
#     print('管他有沒有錯，繼續啦！')    # 不論有沒有錯都會執行這行 



# try:
#     a = int(input('輸入 0～9：'))
#     if a>10:
#         raise ValueError('數字不在範圍內')
#     print(a)
# except ValueError as msg:    # 如果輸入範圍外的數字，執行這邊的程式
#     print(msg)
# except :                     # 如果輸入的不是數字，執行這邊的程式
#     print('有錯誤喔～')
# print('繼續執行')