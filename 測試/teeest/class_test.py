class C8:   #宣告類別 可以做事可以不做事
    number = 1 #類別屬性  
    def __init__(self, numbrt):
        self.n = 3

    def test_object(self): #物件方法
        print("object test")
    
    @classmethod #類別方法
    def test_class(cls):
        print(cls.number)
        cls.test_static()
        print("class test")

    @staticmethod #靜態方法
    def test_static():
        print("static test")

class C7:
    pass