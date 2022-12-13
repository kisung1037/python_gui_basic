from tkinter import *

root = Tk()

root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END,"글자를 입력하세요\n홀리몰리")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력하세요")

def btncmd():
    # 내용출력
    print(txt.get("2.0", END)) # 1: 첫번쨰 라인, 0 : 0번쨰 column 위치
    print(e.get())

    # 내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
