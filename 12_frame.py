from textwrap import fill
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+3000+200") # 가로 * 세로 + x좌표 + y좌표

Label(root, text="메뉴를 선택해주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")


# 메뉴 프레임
frame_burget = Frame(root, relief="solid", bd=1)
frame_burget.pack(side="left", fill="both", expand=True)

Button(frame_burget, text="햄버거").pack()
Button(frame_burget, text="치킨버거").pack()
Button(frame_burget, text="치즈버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()


root.mainloop()

