#物件(Objecct)是類別(Class)的實力(Instancce)
#car 4個輪子
#car.bow()

#
# class Car:
        #物件的變數
#     def __init__(self,make,modle,year,color):
#         #初始化 self代表物件自己本身
#         self.make = make
#         self.model = modle
#         self.year = year
#         self.color = color

#     def driver(self):
#         print(self.model +'正在行駛')
#     def stop(self):
#         print(self.model +'正在煞車')

# car1 = Car('Toyota','Altis',2021,'藍色')
# car2 = Car('Ford','Kuga',2020,'黑色')
# print(car1.make)
# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car2.make)
# print(car2.model)
# print(car2.year)
# print(car2.color)
# car1.driver()
# car2.stop()


# class Car:
#     wheels = 4
#     #物件的變數
#     def __init__(self,make,modle,year,color):
#         #初始化 self代表物件自己本身
#         self.make = make
#         self.model = modle
#         self.year = year
# car1 = Car('福特', 'Focus', 2023, '白色')
# print(car1.wheels)

# car2 = Car('三陽', '勁戰', 2020, '黑色')
# car2.wheels =2
# print(car2.wheels)




#繼承
#動物
# class Animal:
#     aLive = True
#     def eat(self):
#         print('開吃')
#     def sleep(self):
#         print('那我要睡啦')
# #兔子
# class Rabbit(Animal):
#     def jump(self):
#         print('兔子開跳')
        
# animal = Animal()
# rabbit = Rabbit()
# animal.eat()
# animal.sleep()
# rabbit.eat()
# rabbit.jump()
# #魚
# class Fish(Animal):
#     def swim(self):
#         print('小魚開游')
# fish = Fish()
# fish.eat()
# fish.swim()
# class Hawk(Animal):
#     def fly(self):
#         print('老鷹高飛')
# hawk = Hawk()
# hawk.sleep()
# hawk.fly()


#python 方法重寫
# class Animal:
#     def eat(self):
#         print('動物在吃東西')
# class Rabbit(Animal):
#     def eat(self):
#         print('兔子在吃紅蘿蔔')
# class Mammal(Animal):
#     def hi(self):
#         print('開哺')
#     pass
# animal = Animal()
# animal.eat()
# rabbit = Rabbit()
# rabbit.eat()

# class Dog(Mammal):
#     def eat(self):
#         print('狗開啃')
# class Cat(Mammal):
#     def eat(self):
#         print('貓開咬')
# dog = Dog()
# cat = Cat()
# dog.eat()
# cat.eat()



# #python 方法鍊
# class Car:
#     def turn_on(self):
#         print('啟動引擎')
#         #回傳物件本身
#         return self
#     def drive(self):
#         print('開車囉')
#         return self
#     def stop(self):
#         print('停止')
#         return self
#     def turn_off(self):
#         print('熄火')
#         return self
# car = Car()
# car.turn_on().drive().stop().turn_off()


#supper 函式
# class Rectengle: #矩形
#     def __init__(self, length, width):
#         self.length =length
#         self.width = width
#         print('矩形成功執行')
# class Square(Rectengle): #正方形
#     def __init__(self, length, width):
#         super().__init__(length, width)
#         print('正方形')
# class Cube(Rectengle): #立方體
#     def __init__(self, length, width,height):
#         super().__init__(length, width)
#         self.height = height
#         print(f'立方體來囉{length},{width},{height}')

# square = Square(500,500)
# cube = Cube(100,100,100)

#物件當成引數
class Car:
    color = None

def change_color(car,color):
    car.color = color
car1 = Car()
car2 = Car()
car3 = Car()
print(car1.color)
print(car2.color)
print(car3.color)

change_color(car1, '白色')
change_color(car2, '黑色')
change_color(car3, '藍色')

print(car1.color)
print(car2.color)
print(car3.color)