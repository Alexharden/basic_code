import random
feet_in_mile = 5280  #1英里 = 英尺
methers_in_kilometer = 1000 # 米 = 公里
beatles = ["John Lennon", "Paul McCartney", "Ringo Star"]

def get_file_ext(filename): #給文件名稱 擴展文件名稱
    return filename[filename.index(".") +1:]

def roll_dice(num): #模擬擲骰子 給數字 他就擲1~那個數字
    return random.randint(1, num)