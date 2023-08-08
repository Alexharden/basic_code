import os
import time
import shutil 
import send2trash #外部套件 pip install send2trash
#自己決定想吃什麼
# goods = []
# prices = []
# while True:
#     good = input("請輸入你想購買的商品 (如不購買請按q): ")
#     if good.lower() == "q":
#         break
#     price = float(input("請輸入商品價格: "))
#     goods.append(good)
#     prices.append(price)
    
# for index, good in enumerate(goods):
#     print(f'第 {index + 1 } 個商品是 {good} 價格是 {prices[index]:.2f}元')

# total = sum(prices)
# print(f'總價格是 {total:.2f} 元')

#看菜單決定想吃什麼
# menu = {
#     "披薩": 200,
#     "爆米花": 100,
#     "可樂": 40,
#     "檸檬紅茶": 40,
#     "吉拿棒": 80,
# }
# print("菜單")
# print("---------------")
# total = 0     
# cart = []
# for item, price in menu.items():
#     print(f'商品 {item} 價格是: {price}')

# while True:
#     food = input("請輸入你想購買的商品 (如不購買請按q): ")
#     if food =="q":
#         break
#     elif menu.get(food) is None:
#         print("沒有這個商品")
#     else:
#         cart.append(food)
#         total += menu.get(food)
#         # print(food, end=" ")
# print(f"購買了{cart} 總共 {total} 元")

#寫入檔案然後刪除
# test = './file/test.txt'
# text = 'ok'
# folder = './file'
# with open(test,'a') as file:
#     file.write(text)
# time.sleep(10)
# if len(os.listdir(folder)) !=0 :
#     for i in range(len(os.listdir(folder))):
#         os.remove(os.path.join(os.path.abspath(folder)+'//'+os.listdir(folder)[i]))

# #copy copyfile copy2(連檔案權限都可以複製)
# folder = './file'
# source = f'{folder}/test.txt'
# test = './file/test.txt'
# text = 'ok'
# with open(test,'w') as file:
#      file.write(text)
# destination = f'{folder}/test_2.txt'
# shutil.copyfile(source,destination)
# time.sleep(2)
# if len(os.listdir(folder)) !=0 :
#     for i in os.listdir(folder):
#         os.remove(os.path.join(os.path.abspath(folder),i))
#         print("刪除檔案")



#刪除檔案
# path = './file/folder1'
# os.rmdir(path) #如果該資料夾內有檔案無法刪除
# shutil.rmtree(path) #全部永久刪除
# send2trash.send2trash(path) #刪去資源回收桶