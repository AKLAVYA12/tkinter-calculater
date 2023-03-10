from tkinter import *

root = Tk()

root.title("Xdazi")
root.iconbitmap("logo.ico")


def update_label(num):
    global current_text
    current_text = label3["text"]
    label3.config(text=current_text + num)
    if len(current_text) >= 5:
        Button1.config(state=DISABLED)
        Button2.config(state=DISABLED)
        Button3.config(state=DISABLED)
        Button4.config(state=DISABLED)
        Button5.config(state=DISABLED)
        Button6.config(state=DISABLED)
        Button7.config(state=DISABLED)
        Button8.config(state=DISABLED)
        Button9.config(state=DISABLED)
        Buttonl.config(state=DISABLED)
        lable2.config(text='max reach')


def add():
    global Number1
    Number1 = int(label3["text"])
    label3.config(text="+")


def sub():
    global Number1
    Number1 = int(label3["text"])
    label3.config(text="-")


def mul():
    global Number1
    Number1 = int(label3["text"])
    label3.config(text="*")


def equal():
    global Number1, Number2
    equation = label3["text"]
    if "+" in equation:
        Number2 = int(equation.split("+")[1])
        label3.config(text=Number1 + Number2)
    elif "-" in equation:
        Number2 = int(equation.split("-")[1])
        label3.config(text=Number1 - Number2)
    elif "*" in equation:
        Number2 = int(equation.split("*")[1])
        label3.config(text=Number1 * Number2)


def click1():
    update_label("1")


def click2():
    update_label("2")


def click3():
    update_label("3")


def click4():
    update_label("4")


def click5():
    update_label("5")


def click6():
    update_label("6")


def click7():
    update_label("7")


def click8():
    update_label("8")


def click9():
    update_label("9")


def click0():
    update_label("0")


def click01():
    label3.config(text="")
    if len(current_text) >= 5:
        Button1.config(state=NORMAL)
        Button2.config(state=NORMAL)
        Button3.config(state=NORMAL)
        Button4.config(state=NORMAL)
        Button5.config(state=NORMAL)
        Button6.config(state=NORMAL)
        Button7.config(state=NORMAL)
        Button8.config(state=NORMAL)
        Button9.config(state=NORMAL)
        Buttonl.config(state=NORMAL)
        lable2.config(text='')

lable2 = Label(root)
lable2.grid(row=0, column=0)
label3 = Label(root, text=" ")
label3.grid(row=0, column=3)
Button1 = Button(root, text="1", padx=20, pady=10, command=click1)
Button1.grid(row=3, column=0)
Button2 = Button(root, text="2", padx=20, pady=10, command=click2)
Button2.grid(row=3, column=1)
Button3 = Button(root, text="3", padx=20, pady=10, command=click3)
Button3.grid(row=3, column=2)
Button31 = Button(root, text="+", padx=20, pady=10, command=add)
Button31.grid(row=3, column=3)
Button4 = Button(root, text="4", padx=20, pady=10, command=click4)
Button4.grid(row=4, column=0)
Button5 = Button(root, text="5", padx=20, pady=10, command=click5)
Button5.grid(row=4, column=1)
Button6 = Button(root, text="6", padx=20, pady=10, command=click6)
Button6.grid(row=4, column=2)
Button61 = Button(root, text="-", padx=20, pady=10, command=sub)
Button61.grid(row=4, column=3)
Button7 = Button(root, text="7", padx=20, pady=10, command=click7)
Button7.grid(row=5, column=0)
Button8 = Button(root, text="8", padx=20, pady=10, command=click8)
Button8.grid(row=5, column=1)
Button9 = Button(root, text="9", padx=20, pady=10, command=click9)
Button9.grid(row=5, column=2)
Button91 = Button(root, text="x", padx=20, pady=10, command=mul)
Button91.grid(row=5, column=3)
Buttonl = Button(root, text="0", padx=20, pady=10, command=click0)
Buttonl.grid(row=6, column=0)
Buttonl = Button(root, text="=", padx=20, pady=10, command=equal)
Buttonl.grid(row=6, column=1)
Buttonl1 = Button(root, text="clear", padx=10, pady=10, command=click01)
Buttonl1.grid(row=6, column=2)

root.resizable(False, False)

root.mainloop()
