scores = [21,11,12,13,45,30,20]
index = 1
for score in scores: 
    if score >= 20:
        print("場次",end=" ")
        print(index,end="  : ")
        print("分數",end=" ")
        print(score,end="   ")
        print()
    index += 1
        
      