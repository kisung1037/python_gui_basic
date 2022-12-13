import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+3000+200") # 가로 * 세로 + x좌표 + y좌표

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")

# progressbar.start(10)
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progessbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progessbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i)
        progessbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()
root.mainloop()
