# 物件導向的最基礎，我們定義class，然後用它宣告我們的物件/實體(instance)
# class 可以定義attribute(成員)、method(方法)，還有一些既定方法像是初始化__init__
# class裡的method，跟function基本上是一樣的，但第一個參數是self，會指向此實體本身

# 定義一個class叫做Person
# 我們習慣把class的名稱定義成UpperCaseCamelCase，字的開頭大寫
# 如果有多個字組成則在每個字的開頭大寫連起來
class Person:
  
  # 定義class attribute，所有實體會共用它
  kind = 'Person'
  
  # 初始化，當宣告實體的時候這個方法會被呼叫
  # 用self.xxx來定義實體的 attribute，每個被宣告的實體會有自己的attribute 
  def __init__(self, name, age):
    self.name = name; 
    self.age = age;
  
  # 定義實體的方法
  def say_hi(self):
    print(
      f'Hi, my name is {self.name}, I am {self.age} years old'
    )
  
# 使用定義好的Class宣導實體(instance)
mike = Person('Mike', 5) # 帶進去的參數Mike與5分辨對應__init__裡的name與age
john = Person('John', 10)

# 呼叫實體的方法
mike.say_hi() # output: Hi, my name is Mike, I am 5 years old
john.say_hi() # output: Hi, my name is John, I am 10 years old

# 印出實體attribute
print(mike.name) # output: Mike
print(john.name) # output: John

# class attribute是共用的，不管是class本身或是instance都能使用
print(mike.kind) # Person
print(Person.kind) # Person


# 宣告新的class叫Student，繼承Person
class Student(Person):

  # 如果需要的話可以定義新的初始化函數，它會覆蓋掉原本Person定義好的
  def __init__(self, name, age, degree):
    
    # 使用super去呼叫parent的初始化函數，Student的parent是Person
    super().__init__(name, age)
    
    # 新的class多一個degree這個attribute
    self.degree = degree
  
  # 定義新的方法
  def tell_my_degree(self):
    print(f'I earned my {self.degree} degree')

# 宣告實體
susan = Student('Susan', 22, 'master')


# 繼承的class所宣告出的實體可以呼叫parent class定義的方法
susan.say_hi() # ouptut: Hi, my name is Susan, I am 22 years old
susan.tell_my_degree() # output: I earned my master degree

print(susan.name) # output: Susan
print(susan.degree) # output: master