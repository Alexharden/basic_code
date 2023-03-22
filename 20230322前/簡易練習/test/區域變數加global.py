a = []
b = a
c = []
d = c

def f1():
    global c # 如果加上這行，f2 裡的 c 就會被影響 變成全域
    a.append(1)
    c = [1]
    print(a)  # [1]
    print(b)  # [1]   # 被影響
    print(c)  # [1]
    print(d)  # []    # 不受影響

def f2():
    print(a)  # [1]   # 被影響
    print(b)  # [1]   # 被影響
    print(c)  # []    # 不受影響，但如果 f1 加上 global c，此處就會被影響
    print(d)  # []    # 不受影響

f1()
f2()