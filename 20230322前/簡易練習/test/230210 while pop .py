buyers = [['James', 1030],   #買家資料
            ['Curry', 893],
            ['Durant', 2050],
            ['Jordan', 990],
            ['David', 2110]]
goldbuyers = [] #Gold 買家串列
vipbuyers = []  #VIP買家資料
while buyers:   #執行迴圈跑完列表資料
    index_buyer = buyers.pop() #傳出列表最後取值 然後刪除
    if index_buyer[1] >= 1000:
        vipbuyers.append(index_buyer) #加入VIP買家列表
    else:
        goldbuyers.append(index_buyer) #加入Gold買家列表
print("VIP 買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)