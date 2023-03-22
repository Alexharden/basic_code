# class ChineseChef: (繼承前)

from Chef import Chef
class ChineseChef(Chef): #繼承後 下方三個程式碼 從Chef.py 中導入過來
    # def make_chicken(self):   繼承前
    #     print("主廚會料理雞肉")
    
    # def make_salad(self): 繼承前
    #     print("主廚會料理沙拉")
    
    # def make_special_food(self): 繼承前
    #     print("主廚會做多汁漢堡")
    def make_special_food(self):
        print("主持會做宮保雞丁") #取代 make_special_food(self)內的資料

    def make_fried_rice(self):
        print("主廚會做炒飯")