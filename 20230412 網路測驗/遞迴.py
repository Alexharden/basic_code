import sys # import我們會在後面進行介紹print(sys.getrecursionlimit())

def cal(end):
    if end != 1:
        return end + cal(end - 1)
    else:
        return 1
    

print(cal(999))
print(sys.getrecursionlimit())