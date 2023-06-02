# import time
# print('Loading',end = '')
# while True:
#     for i in range(6):
#         print('.',end = '',flush = True)
#         time.sleep(0.5)
#     n = 10
#     for i in range(n+1):
#         print(f'\r倒數 {n-i} 秒', end='')
#         time.sleep(1)
#     print('\r時間到', end='')    


# import tkinter as tk

# def update_loading_animation(label, dots):
#     dots = (dots + 1) % 4
#     loading_text = "loading" + "." * dots
#     label.config(text=loading_text)
#     label.after(500, update_loading_animation, label, dots)

# # 创建窗口
# window = tk.Tk()
# window.title("Loading Animation")

# # 创建标签
# loading_label = tk.Label(window, text="loading")
# loading_label.pack()

# # 更新加载动画
# update_loading_animation(loading_label, 0)

# # 运行窗口主循环
# window.mainloop()




import tkinter as tk

def update_loading_animation(label, dots):
    dots = (dots + 1) % 4
    loading_text = "loading" + "." * dots
    label.config(text=loading_text)
    
    if dots == 0:
        delay = 1  # 点之间的间隔时间
    else:
        delay = 1500  # 点之间的间隔时间为1.5秒
    
    label.after(delay, update_loading_animation, label, dots)

# 创建窗口
window = tk.Tk()
window.title("Loading Animation")

# 创建标签
loading_label = tk.Label(window, text="loading")
loading_label.pack()

# 更新加载动画
update_loading_animation(loading_label, 0)

# 运行窗口主循环
window.mainloop()






