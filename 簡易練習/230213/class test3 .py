# class Point:
#     def __init__(self,x,y): #初始化函式
#         self.x = x     #建立實體屬性
#         self.y = y
#     def show(self):    #建立實體方法 self一定要寫
#         print(self.x, self.y)
# p= Point(1,5) #建立實體物件
# p.show() #呼叫實體方法

#Point 實體物件的設計: 平面座標上的點
# class Point:
#     def __init__ (self, x, y):
#         self.x = x
#         self.y = y
#     #定義實體方法
#     def show(self):
#         print(self.x, self.y)
#     def distance(self, targetX, targetY): #目標座標跟實體座標之間的距離
#         return (((self.x- targetX)** 2)+((self.y - targetY)** 2))** 0.5 #((x1-x2)^2)+((y1-y2)^2)在開根號
# p=Point(3,4)
# p.show() #呼叫實體方法 / 函式
# result= p.distance(0,0) #計算座標 3,4 和座標 0,0 之間的距離
# print(result)

# #File 實體物件的設計: 
# class File:
#     def __init__(self, name): #初始化函式
#         self.name = name 
#         self.file = None #尚未開啟的檔案:初期是 None
#     def open(self): #定義實體方法
#        self.file= open(self.name, mode = "r" , encoding= "utf-8") #python內建檔案開啟功能 得到一個檔案物件  放在實體屬性file 裡面
#     def read(self): #利用得到的檔案物件,做讀取
#         return self.file.read()
# #讀取第一個檔案
# f1=File("data1.txt")
# f1.open()
# data=f1.read()
# print(data)
# #讀取第二個檔案
# f2=File("data2.txt")
# f2.open()
# data2 = f2.read()
# print(data2)