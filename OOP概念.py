from abc import ABC, abstractmethod

# 建立一個名為 InterfaceSample 的抽象類別，繼承 ABC 類別
class InterfaceSample(ABC):
    # 定義五個抽象方法，需要在繼承的子類別中實作
    @abstractmethod
    def function1(self):pass
    @abstractmethod
    def function2(self):pass
    @abstractmethod
    def function3(self):pass
    @abstractmethod
    def function4(self):pass
    @abstractmethod
    def function5(self):pass

# 建立一個 IntheritClass 的類別，繼承 InterfaceSample 抽象類別
class IntheritClass(InterfaceSample):
    def __init__(self):
        pass

# 建立一個 IntheritClass 的實體，但是因為 InterfaceSample 為抽象類別，且沒有實作裡面的抽象方法，
# 所以無法實體化 IntheritClass
IntheritClass()
