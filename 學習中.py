import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGame:
    def __init__(self):
        self.current_player = None
        self.game_state = [[' ']*3 for _ in range(3)]

    def open_game_window(self, user_name, player_choice, game_mode):
        self.current_player = player_choice

        game_window = tk.Toplevel()
        game_window.title('井字遊戲')
        game_window.geometry('1080x1080')

        def on_cell_click(row, col):
            if self.game_state[row][col] == ' ':
                self.game_state[row][col] = self.current_player
                button = buttons[row][col]
                button.config(text=self.current_player, state=tk.DISABLED)

                if self.check_game_over():
                    if self.check_game_over() == "平局":
                        messagebox.showinfo('遊戲結束', '此局平手')
                    else:
                        messagebox.showinfo('遊戲結束', f'玩家 {self.current_player} 獲勝！')
                    self.reset_game()
                else:
                    if game_mode == "人機對戰" and self.current_player != player_choice:
                        self.computer_move()
                    else:
                        self.current_player = 'O' if self.current_player == 'X' else 'X'

        def computer_move():
            empty_cells = [(row, col) for row in range(3) for col in range(3) if self.game_state[row][col] == ' ']
            if empty_cells:
                row, col = random.choice(empty_cells)
                self.game_state[row][col] = 'O'
                button = buttons[row][col]
                button.config(text='O', state=tk.DISABLED)
                if self.check_game_over():
                    if self.check_game_over() == "平局":
                        messagebox.showinfo('遊戲結束', '此局平手')
                    else:
                        messagebox.showinfo('遊戲結束', '電腦獲勝！')
                    self.reset_game()
                else:
                    self.current_player = 'X'

        def check_game_over():
            for row in range(3):
                if self.game_state[row][0] == self.game_state[row][1] == self.game_state[row][2] != ' ':
                    return True
            for col in range(3):
                if self.game_state[0][col] == self.game_state[1][col] == self.game_state[2][col] != ' ':
                    return True
            if self.game_state[0][0] == self.game_state[1][1] == self.game_state[2][2] != ' ':
                return True
            if self.game_state[0][2] == self.game_state[1][1] == self.game_state[2][0] != ' ':
                return True
            if all(self.game_state[row][col] != ' ' for row in range(3) for col in range(3)):
                return "平局"
            return False

        def reset_game():
            self.current_player = player_choice
            self.game_state = [[' ']*3 for _ in range(3)]
            for row in buttons:
                for button in row:
                    button.config(text=' ', state=tk.NORMAL)

        buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                buttons[row][col] = tk.Button(game_window, text=' ', font=('Arial', 30), width=3, height=1,
                                               command=lambda r=row, c=col: on_cell_click(r, c))
                buttons[row][col].grid(row=row, column=col)

        if game_mode == "人機對戰" and player_choice == "O":
            self.computer_move()

def start_game(user_name, player_choice, game_mode):
    welcome_window.withdraw()
    game = TicTacToeGame()
    game.open_game_window(user_name, player_choice, game_mode)

def on_choice_click(player_choice, game_mode):
    start_game(entry.get(), player_choice, game_mode)

welcome_window = tk.Tk()
welcome_window.title('歡迎')
welcome_window.geometry('1080x1080')

label = tk.Label(welcome_window, text='請輸入你的名稱:', font=('Arial', 20))
label.pack(pady=20)

entry = tk.Entry(welcome_window, width=20, font=('Arial', 15))
entry.pack(pady=10)

label2 = tk.Label(welcome_window, text='請選擇你的角色:', font=('Arial', 15))
label2.pack(pady=10)

frame = tk.Frame(welcome_window)
frame.pack()

btn_x = tk.Button(frame, text="X", command=lambda: on_choice_click("X", "人機對戰"), font=('Arial', 15))
btn_x.pack(side=tk.LEFT, padx=5)

btn_o = tk.Button(frame, text="O", command=lambda: on_choice_click("O", "人機對戰"), font=('Arial', 15))
btn_o.pack(side=tk.LEFT, padx=5)

label3 = tk.Label(welcome_window, text='請選擇遊戲模式:', font=('Arial', 15))
label3.pack(pady=10)

frame2 = tk.Frame(welcome_window)
frame2.pack()

btn_pvp = tk.Button(frame2, text="人人對戰", command=lambda: on_choice_click(None, "人人對戰"), font=('Arial', 15))
btn_pvp.pack(side=tk.LEFT, padx=5)

btn_pvc = tk.Button(frame2, text="人機對戰", command=lambda: on_choice_click(None, "人機對戰"), font=('Arial', 15))
btn_pvc.pack(side=tk.LEFT, padx=5)

welcome_window.mainloop()
