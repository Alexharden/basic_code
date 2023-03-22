#key值一層只有一個
#value值可以重複



score =  [
         [40, 50, 60, 70, 80 ], #key值 0 ,1 ,2 ,3 ,4
         [41, 51, 61, 71, 81 ],
         [42, 52, 62, 72, 82 ]
        ]  

for i in range(1): #  最外層[] 0 1 2 range(數字-1)
    sum=0
    for j in range(4): #內層[] 0 1 2 3 4 
        sum+=score[i][j]
        print(sum)

# score =   [42, 52, 62, 72, 82 ] 