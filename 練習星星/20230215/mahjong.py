mahjong_list = input("輸入17張牌：")
# mahjong_list = "5 6 7 9 10 11 19 20 20 20 20 21 27 27 31 31 31"
print(f"mahjong_list input是=> {mahjong_list}")
print(f"mahjong_list input type是=> {type(mahjong_list)}")
mahjong_list = mahjong_list.split(" ")
print(f"mahjong_list是=> {mahjong_list}")
print(f"mahjong_list type是=> {type(mahjong_list)}")
mahjong_list.sort()
# print(int(mahjong_list))
mahjong_list = list(map(int, mahjong_list))
print(f"mahjong_list=> {mahjong_list}")
print(f"mahjong_list type是=> {type(mahjong_list)}")

# Shunzi = [x for x in range(0, 34) if x not in [7,8,16,17,25,26,27,28,29,30,31,32,33]]
# for i in set(mahjong_list):
#     origin_mahjong = mahjong_list.copy()    
#     if mahjong_list.count(i) >= 2:
#         # print("一對眼")
#         # print(i)
#         mahjong_list[mahjong_list.index(i)] = -1
#         mahjong_list[mahjong_list.index(i)] = -1
#         for j in range(len(mahjong_list)):
#             if mahjong_list.count(mahjong_list[j]) == 3 and mahjong_list[j] != -1:
#                 # print("刻子")
#                 mahjong_list[j],mahjong_list[j+1],mahjong_list[j+2] = -1,-1,-1
#             if mahjong_list[j]+1 in mahjong_list and mahjong_list[j]+2 in mahjong_list and mahjong_list[j] in Shunzi:
#                 # print(mahjong_list[mahjong_list.index(mahjong_list[j]+2)])
#                 # print(mahjong_list[mahjong_list.index(mahjong_list[j]+1)])
#                 # print(mahjong_list[j])
#                 mahjong_list[mahjong_list.index(mahjong_list[j]+2)] = -1
#                 mahjong_list[mahjong_list.index(mahjong_list[j]+1)] = -1
#                 mahjong_list[j] = -1
#                 # print("順子")
#     if mahjong_list.count(-1) == 17:
#         print("胡了")
#         break
#     else:
#         mahjong_list = origin_mahjong