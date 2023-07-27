import tkinter as tk
from tkinter import messagebox
import random
class windows_welocom:
    def has_special_characters(self, user_name): #判斷是否有特殊符號
        # 定義特殊符號
        special_characters = set("!@#$%^&*()_-+={}[]|\:;'<>?,./\"")
        
        # 檢查是否含有特殊符號
        return any(char in special_characters for char in user_name)

    def get_user_input(self): #檢查判斷使用者輸入的名稱
        user_name = entry.get()
        self.error = self.has_special_characters(user_name)
        if user_name.strip() == '' or self.error:
            messagebox.showerror('錯誤', '請輸入有效的名稱')
        else:
            messagebox.showinfo('歡迎', f'歡迎, {user_name}!')
            window.withdraw() #隱藏主視窗
            open_game_instance = open_game()
            open_game_instance.open_game_window(user_name)
            # open_game_window(user_name) #開啟遊戲
    def confirm_bottom(self): #點及確認按鈕
        self.get_user_input()
    def validate_input(self, user_name): #限制使用者輸入長度限制
        # 限制輸入長度
        return len(user_name) <= 5
    
class open_game:
    def open_game_window(self, user_name):
        game_window = tk.Toplevel()  # Use Toplevel to create a new window
        game_window.title('井字遊戲')
        game_window.geometry('1080x1080')

        # Initialize game state and current player
        game_state = [[' ']*3 for _ in range(3)]
        current_player = 'X'

        def computer_move():
            nonlocal current_player, game_state
            # Computer's move logic here
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

        def reset_game():
            nonlocal current_player, game_state
            current_player = 'X'
            game_state = [[' ']*3 for _ in range(3)]
            # Reset buttons and game state
            for row in buttons:
                for button in row:
                    button.config(text=' ', state=tk.NORMAL)

        def check_game_over():
            nonlocal game_state #使函式可以修改外部定義的變數
            # Check game over logic here
        
            # 檢查行
            for row in range(3):
                if game_state[row][0] == game_state[row][1] == game_state[row][2] != ' ': #檢查行是否有相同符號且不是空白的格子
                    return True

            # 檢查列
            for col in range(3):
                if game_state[0][col] == game_state[1][col] == game_state[2][col] != ' ': #檢查列是否有相同符號且不是空白的格子
                    return True

            # 檢查對角線
            if game_state[0][0] == game_state[1][1] == game_state[2][2] != ' ': #檢查對角線是否有相同符號且不是空白的格子
                return True
            if game_state[0][2] == game_state[1][1] == game_state[2][0] != ' ':
                return True

            # 檢查是否平局
            if all(game_state[row][col] != ' ' for row in range(3) for col in range(3)):
                return "平局"

            return False

        def on_cell_click(row, col):
            nonlocal current_player, game_state
            # Handle cell click event
            
            if game_state[row][col] == ' ': #點擊空白格子
                game_state[row][col] = current_player #輸入玩家的符號
                button = buttons[row][col] #將格子顯示為玩的符號
                button.config(text=current_player, state=tk.DISABLED) #把格子鎖定變成禁用的狀態
                try:
                    result = check_game_over()

                    if result == '平局':  # 檢查是否平局
                        messagebox.showinfo('遊戲結束', '此局平手')
                        reset_game()
                    elif result:
                        messagebox.showinfo('遊戲結束', f'玩家 {user_name} 獲勝！')
                        reset_game()
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'
                        computer_move() #電腦下棋
                except Exception as e:
                    print("發生異常囉", e)

        # Create grid of buttons
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

        # Create reset button
        reset_button = tk.Button(game_window, text='重置遊戲', font=('Arial', 30), command=reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

        # Add computer play button
        # auto_play_button = tk.Button(game_window, text='電腦自動對戰', font=('Arial', 20), command=computer_move)
        # auto_play_button.grid(row=4, column=0, columnspan=3, padx=5, pady=10)

game_start = windows_welocom()
# 創建窗口
window = tk.Tk()
window.title('My Application')
window.geometry('1080x1080')

label = tk.Label(window, text='請輸入你的名稱:', font=('Arial', 20))
label.pack(pady=(300, 10))

entry = tk.Entry(window, width=30, font=('Arial', 30),validate="key" )
entry.config(validatecommand=(window.register(game_start.validate_input), "%P"))
entry.pack()

button = tk.Button(window, text='確認', command=game_start.confirm_bottom, font=('Arial', 15))
button.pack(pady=10)

# 運行窗口主循環
window.mainloop()





# def get_user_input():
#     user_name = entry.get()
#     if user_name.strip() == '':
#         messagebox.showerror('錯誤', '請輸入有效的名稱')
#     else:
#         messagebox.showinfo('歡迎', f'歡迎, {user_name}!')
#         window.withdraw() #隱藏主視窗
#         open_game_window(user_name) #開啟遊戲

# def open_game_window(user_name):
#     # 創建新窗口
#     game_window = tk.Tk() #新建一個視窗
#     game_window.title('井字遊戲') #標題
#     game_window.geometry('1080x1080') #視窗大小

#     # 初始化井字遊戲狀態
#     game_state = [[' ']*3 for _ in range(3)]
#     current_player = 'X'

#     # 檢查遊戲是否結束...
#     # 點擊方格的事件處理函式...

#     # 電腦自動下棋
#     def computer_move():
#         nonlocal current_player

#         # 獲取空白方格的座標
#         empty_cells = []
#         for row in range(3):
#             for col in range(3):
#                 if game_state[row][col] == ' ':
#                     empty_cells.append((row, col))

#         if empty_cells:
#             # 隨機選擇一個空白方格下棋
#             row, col = random.choice(empty_cells)
#             game_state[row][col] = 'O'
#             button = buttons[row][col]
#             button.config(text='O', state=tk.DISABLED)

#             if check_game_over():
#                 messagebox.showinfo('遊戲結束', '電腦獲勝！')
#                 reset_game()
#             else:
#                 current_player = 'X'

#     # 重置遊戲狀態
#     def reset_game():
#         nonlocal current_player, game_state
#         current_player = 'X'
#         game_state = [[' ']*3 for _ in range(3)]
#         for row in buttons:
#             for button in row:
#                 button.config(text=' ', state=tk.NORMAL)

#     # 檢查遊戲是否結束
#     def check_game_over():
#         # 檢查行...
#         # 檢查列...
#         # 檢查對角線...
#         # 檢查是否平局...
#         return False
#     def on_cell_click(row, col):
#         nonlocal current_player

#         if game_state[row][col] == ' ':
#             game_state[row][col] = current_player
#             button = buttons[row][col]
#             button.config(text=current_player, state=tk.DISABLED)

#             if check_game_over():
#                 messagebox.showinfo('遊戲結束', f'玩家 {current_player} 獲勝！')
#                 reset_game()
#             else:
#                 current_player = 'O' if current_player == 'X' else 'X'
#                 computer_move() #電腦下棋
#     # 創建方格按鈕
#     buttons = []
#     for row in range(3):
#         game_window.grid_rowconfigure(row, weight=1)
#         game_window.grid_columnconfigure(row, weight=1)
#         button_row = []
#         for col in range(3):
#             button = tk.Button(game_window, text=' ', font=('Arial', 70), width=4, height=2,
#                                command=lambda r=row, c=col: on_cell_click(r, c))
#             button.grid(row=row, column=col, padx=5, pady=5)
#             button_row.append(button)
#         buttons.append(button_row)

#     # 創建重置按鈕
#     reset_button = tk.Button(game_window, text='重置遊戲', font=('Arial', 30), command=reset_game)
#     reset_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

#     # 添加電腦自動對戰的按鈕
#     auto_play_button = tk.Button(game_window, text='電腦自動對戰', font=('Arial', 20), command=computer_move)
#     auto_play_button.grid(row=4, column=0, columnspan=3, padx=5, pady=10)

#     # 運行遊戲窗口主循環
#     game_window.mainloop()

# # 創建窗口
# window = tk.Tk()
# window.title('My Application')
# window.geometry('1080x1080')

# label = tk.Label(window, text='請輸入你的名稱:', font=('Arial', 20))
# label.pack(pady=(300, 10))

# entry = tk.Entry(window, width=30, font=('Arial', 30))
# entry.pack()

# button = tk.Button(window, text='確認', command=get_user_input, font=('Arial', 15))
# button.pack(pady=10)

# # 運行窗口主循環
# window.mainloop()

