msg1 = "人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!"
msg2 = "輸入 q可以結束對話"
msg = msg1 + "\n" + msg2 + "\n" + "= "
input_msg= ""
while input_msg != "q":
    input_msg = input(msg)
    print(input_msg)