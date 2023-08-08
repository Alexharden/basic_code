import tkinter as tk
import tkinter.messagebox as msg 

# window = tk.Tk() #創建視窗
# window.title('玩遊戲') #創建標題
# window.geometry('1080x720') #創建視窗大小
# window.resizable(False, False) #使用者可否調整視窗大小
# window.iconphoto(True, tk.PhotoImage(file='image\ico.png'))  #左上角icon圖示

# import tkinter as tk
# import tkinter.messagebox as msg # messagebox要另行匯入，否則會出錯。

# ### calculate函式用來接受按鈕事件，取得商品價格及折扣方式，計算後輸出
# def calculate():
#     # 每次要計算時，都讓按鈕顯示計算哪一個折扣法
#     btnstr.set('計算' + radiostr.get() + '中')
#     # 用try...except...的方式來避免掉輸入的不是數字
#     try:
#         choice = radiostr.get() # radiobutton的選擇項
#         p1 = int(price1.get())
#         p2 = int(price2.get())
#         if p1 <= 0 or p2 <= 0: # 如果輸入<=0的數字也當成例外處理
#             raise Exception()
#         if choice == '一': # 買二件88折
#             p = 0.88 * (p1 + p2)
#         elif choice == '二': # 第二件6折
#             p = p1 + p2 * 0.6
#         else: # 第二件半價
#             p = p1 + p2 * 0.5
#         total.set(str(int(p))) # 顯示總額
#     except:
#         # 例外處理：先全部歸0，再跳提示視窗
#         price1.set('0')
#         price2.set('0')
#         total.set('0')
#         msg.showerror('輸入錯誤!', '請輸入正確的數字!')
#     btnstr.set('算選項' + radiostr.get())


# ### select會在選中了某個折扣的時候被呼叫，此時會再呼叫calculate快速計算比較方便
# def select():
#     btnstr.set('算選項' + radiostr.get())
#     calculate()

# #### 主視窗生成
# win = tk.Tk()
# win.title('從零開始學Python：第二件X折？')
# win.geometry('800x220')
# win.resizable(False, False)
# win.iconphoto(True, tk.PhotoImage(file='image\ico.png'))

# ### Frame fm_cal: 放計算按鈕、"總額"文字label、總額金額顯示label
# fm_cal = tk.Frame(win, bg='skyblue', width=800, height=100)
# # fill表示沒填滿的部分是否填滿，BOTH表示xy方向都填滿，讀者可以試試看去掉的差別
# fm_cal.pack(fill=tk.BOTH) 

# btnstr = tk.StringVar() # 初始化tk的字串變數
# btnstr.set('按我計算')
# btn = tk.Button(fm_cal, bg='#71C973', fg='white', textvariable=btnstr, font=('微軟正黑體', 20), command=calculate, pady=10) # pad是指兩個元件之間空出多少距離
# # side代表排版對齊時跟上個元件從哪個方向開始對齊
# btn.pack(side=tk.LEFT, padx=10, pady=10) # padx/pady分別就是x方向跟y方向

# lbl_text = tk.Label(fm_cal, bg='#F95E62', fg='white', 
#                text='總額：', font=('微軟正黑體', 20), 
#                padx=10, pady=10)
# lbl_text.pack(side=tk.LEFT, padx=108)

# total = tk.StringVar() # 初始化tk的字串變數
# total.set('0')
# lbl_total = tk.Label(fm_cal, bg='#F95E62', fg='white', 
#                text='0', textvariable=total, font=('微軟正黑體', 20), 
#                padx=10, pady=10)             
# lbl_total.pack(side=tk.LEFT, padx=57, pady=10)

# ### Frame fm_lbl: 放標籤及Radiobutton(折數)
# fm_lbl = tk.Frame(win, bg='#FF9955', width=800, height=150)
# fm_lbl.pack(side=tk.TOP, fill=tk.BOTH)

# lbl1 = tk.Label(fm_lbl, bg='#F95E62', fg='white', 
#                text='第一件價格', font=('微軟正黑體', 20), 
#                padx=10, pady=10)
# lbl1.pack(side=tk.LEFT, padx=10, pady=10)
# lbl_plus = tk.Label(fm_lbl, bg='#FF9955', fg='black', 
#                text='及', font=('微軟正黑體', 20), 
#                padx=10, pady=10)
# lbl_plus.pack(side=tk.LEFT, padx=10)
# lbl2 = tk.Label(fm_lbl, bg='#F95E62', fg='white', 
#                text='第二件價格', font=('微軟正黑體', 20), 
#                padx=10, pady=10)               
# lbl2.pack(side=tk.LEFT, padx=10)
# lbl_plus2 = tk.Label(fm_lbl, bg='#FF9955', fg='black', 
#                text='及', font=('微軟正黑體', 20), 
#                padx=10, pady=10)
# lbl_plus2.pack(side=tk.LEFT, padx=10)
# lbl_coupon = tk.Label(fm_lbl, bg='#F95E62', fg='white', 
#                text='折扣', font=('微軟正黑體', 20), 
#                padx=10, pady=10)
# lbl_coupon.pack(side=tk.LEFT, padx=10)

# ### Frame fm_rad: 放Radiobutton(框一組自己對齊)
# fm_rad = tk.Frame(fm_lbl, bg='#FF9955', width=150, height=150, padx=30)
# fm_rad.pack(side=tk.LEFT, fill=tk.BOTH)

# # StringVar的初始化值在第二個參數，第一個要填None
# radiostr = tk.StringVar(None, '一')
# # command會對應到選取時呼叫的函式，同時當選擇到它，value的值會放入variable的變數
# r1 = tk.Radiobutton(fm_rad, bg='#FF9955', text='買兩件88折', variable=radiostr, value='一', command=select)
# r1.pack(anchor=tk.W) # 另一個對齊方式，由上而下，但上下之間是靠左對齊
# r2 = tk.Radiobutton(fm_rad, bg='#FF9955', text='第二件6折', variable=radiostr, value='二', command=select)
# r2.pack(anchor=tk.W)
# r3 = tk.Radiobutton(fm_rad, bg='#FF9955', text='第二件半價', variable=radiostr, value='三', command=select)
# r3.pack(anchor=tk.W)

# ### Frame fm_ent: 放entry(輸入兩件商品分別的價格)
# fm_ent = tk.Frame(win, width=800, height=200)
# fm_ent.pack(side=tk.TOP, fill=tk.BOTH)

# # ent1對應到price1
# price1 = tk.StringVar(None, '0')
# ent1 = tk.Entry(fm_ent, width=20, justify='center', textvariable=price1)
# ent1.pack(side=tk.LEFT, padx=17, pady=7, fill=tk.Y)

# # 為了排版增加的空白label
# lbl_empty = tk.Label(fm_ent, 
#                text='　', font=('微軟正黑體', 20), 
#                padx=20)
# lbl_empty.pack(side=tk.LEFT)

# # ent1對應到price2
# price2 = tk.StringVar(None, '0')
# ent2 = tk.Entry(fm_ent, width=20, justify='center', textvariable=price2)
# ent2.pack(side=tk.LEFT, padx=17, pady=7, fill=tk.Y)

# # 開始整個主程式
# win.mainloop()