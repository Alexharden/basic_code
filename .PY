class A:
     def add(self, x):
         y = x+2
         print(y)
class B(A):
    def add(self, x):
        super().add(x)
B().add(3)
