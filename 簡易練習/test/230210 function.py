import random 
def rand2int():
    rand1 = random.randint(1,10)
    rand2 = random.randint(1,10)
    return rand1, rand2
a,b = rand2int()
print(a)
print(b)
print(rand2int())