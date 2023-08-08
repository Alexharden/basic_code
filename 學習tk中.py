import tkinter as tk
from tkinter.constants import * #anchor 設定多種角度
from tkinter.constants import CENTER
window = tk.Tk() #創建視窗
window.title('玩遊戲') #創建標題
window.geometry('1080x720') #創建視窗大小
window.resizable(False, False) #使用者可否調整視窗大小
window.iconphoto(True, tk.PhotoImage(file='image\ico.png')) #左上角icon圖示
#pack grid 在一個視窗中只能使用一種
fm = tk.Frame(bg= "green", width=300, height=100) #可以在畫面排版上塞一塊色塊 bg可以用 #FF0000代替
fm.pack()
is_button = tk.Button(text="確認") #製作按鈕
is_button.pack(side="top", fill = "both") #按鈕位置 #top bottom(下) right left 
#fill 元件填滿 有  y both可使用
# fm = tk.Frame(bg= "green", width=800, height=300)
# fm.grid(row=0,column=1)
# cancel_button = tk.Button(text="取消")
# cancel_button.grid(row=0,column=1)

# test = tk.Button(text="測試")
# test.place(x=190,y=200,anchor=CENTER)

# window.iconbitmap('image\ico.png')
window.mainloop() #正式啟動