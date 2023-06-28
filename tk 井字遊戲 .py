import tkinter as tk
from tkinter import messagebox
import random

def get_user_input():
    user_name = entry.get()
    if user_name.strip() == '':
        messagebox.showerror('錯誤', '請輸入有效的名稱')
    else:
        messagebox.showinfo('歡迎', f'歡迎, {user_name}!')
        window.withdraw() #隱藏主視窗
        open_game_window(user_name) #開啟遊戲

def open_game_window(user_name):
    # 創建新窗口
    game_window = tk.Tk() #新建一個視窗
    game_window.title('井字遊戲') #標題
    game_window.geometry('1080x1080') #視窗大小

    # 初始化井字遊戲狀態
    game_state = [[' ']*3 for _ in range(3)]
    current_player = 'X'

    # 檢查遊戲是否結束...
    # 點擊方格的事件處理函式...

    # 電腦自動下棋
    def computer_move():
        nonlocal current_player

        # 獲取空白方格的座標
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if game_state[row][col] == ' ':
                    empty_cells.append((row, col))

        if empty_cells:
            # 隨機選擇一個空白方格下棋
            row, col = random.choice(empty_cells)
            game_state[row][col] = 'O'
            button = buttons[row][col]
            button.config(text='O', state=tk.DISABLED)

            if check_game_over():
                messagebox.showinfo('遊戲結束', '電腦獲勝！')
                reset_game()
            else:
                current_player = 'X'

    # 重置遊戲狀態
    def reset_game():
        nonlocal current_player, game_state
        current_player = 'X'
        game_state = [[' ']*3 for _ in range(3)]
        for row in buttons:
            for button in row:
                button.config(text=' ', state=tk.NORMAL)

    # 檢查遊戲是否結束
    def check_game_over():
        # 檢查行...
        # 檢查列...
        # 檢查對角線...
        # 檢查是否平局...
        return False
    def on_cell_click(row, col):
        nonlocal current_player

        if game_state[row][col] == ' ':
            game_state[row][col] = current_player
            button = buttons[row][col]
            button.config(text=current_player, state=tk.DISABLED)

            if check_game_over():
                messagebox.showinfo('遊戲結束', f'玩家 {current_player} 獲勝！')
                reset_game()
            else:
                current_player = 'O' if current_player == 'X' else 'X'
                computer_move() #電腦下棋
    # 創建方格按鈕
    buttons = []
    for row in range(3):
        game_window.grid_rowconfigure(row, weight=1)
        game_window.grid_columnconfigure(row, weight=1)
        button_row = []
        for col in range(3):
            button = tk.Button(game_window, text=' ', font=('Arial', 70), width=4, height=2,
                               command=lambda r=row, c=col: on_cell_click(r, c))
            button.grid(row=row, column=col, padx=5, pady=5)
            button_row.append(button)
        buttons.append(button_row)

    # 創建重置按鈕
    reset_button = tk.Button(game_window, text='重置遊戲', font=('Arial', 30), command=reset_game)
    reset_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

    # 添加電腦自動對戰的按鈕
    auto_play_button = tk.Button(game_window, text='電腦自動對戰', font=('Arial', 20), command=computer_move)
    auto_play_button.grid(row=4, column=0, columnspan=3, padx=5, pady=10)

    # 運行遊戲窗口主循環
    game_window.mainloop()

# 創建窗口
window = tk.Tk()
window.title('My Application')
window.geometry('1080x1080')

label = tk.Label(window, text='請輸入你的名稱:', font=('Arial', 20))
label.pack(pady=(300, 10))

entry = tk.Entry(window, width=30, font=('Arial', 30))
entry.pack()

button = tk.Button(window, text='確認', command=get_user_input, font=('Arial', 15))
button.pack(pady=10)

# 運行窗口主循環
window.mainloop()

