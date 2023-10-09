from tkinter import *
import tkinter
window = Tk()
window.title("Calculator")
window.geometry("450x350")
window.config(background = "black")


expression = ""
def press(num):
    global expression
    expression = expression+str(num)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set(expression)

def btn_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""


input_text = StringVar()

frame = Frame(window,bg="black") 
frame.pack(side=TOP)

bottomframe = Frame(window,bg="orange") 
bottomframe.pack(side=TOP)

label = Label(frame, text = "CALCULATOR", font = 'arial 25 bold', width = 23, bd = 5, bg = 'orange', fg = 'black')
label.grid(row=0,column=0)

expression_field = Entry(frame,textvariable = input_text, font = 'arial 25 bold',width=25,bd=5)
expression_field.grid(row=2,column=0)

btn7 = Button(bottomframe,command = lambda: press(7), width=6,height=1,text="7",font=("arial",20,"bold"),bg="black",fg="white").grid(row=2,column=0)
btn8 = Button(bottomframe,command = lambda: press(8),width=6,height=1,text="8",font=("arial",20,"bold"),bg="black",fg="white").grid(row=2,column=1)
btn9 = Button(bottomframe,command = lambda: press(9),width=6,height=1,text="9",font=("arial",20,"bold"),bg="black",fg="white").grid(row=2,column=2)
btn_add = Button(bottomframe,command = lambda: press("+"),width=6,height=1,text="+",font=("arial",20,"bold"),bg="black",fg="white").grid(row=2,column=3)
btn4 = Button(bottomframe,command = lambda: press(4),width=6,height=1,text="4",font=("arial",20,"bold"),bg="black",fg="white").grid(row=3,column=0)
btn5 = Button(bottomframe,command = lambda: press(5),width=6,height=1,text="5",font=("arial",20,"bold"),bg="black",fg="white").grid(row=3,column=1)
btn6 = Button(bottomframe,command = lambda: press(6),width=6,height=1,text="6",font=("arial",20,"bold"),bg="black",fg="white").grid(row=3,column=2)
btn_sub = Button(bottomframe,command = lambda: press("-"),width=6,height=1,text="-",font=("arial",20,"bold"),bg="black",fg="white").grid(row=3,column=3)
btn1 = Button(bottomframe,command = lambda: press(1),width=6,height=1,text="1",font=("arial",20,"bold"),bg="black",fg="white").grid(row=4,column=0)
btn2 = Button(bottomframe,command = lambda: press(2),width=6,height=1,text="2",font=("arial",20,"bold"),bg="black",fg="white").grid(row=4,column=1)
btn3 = Button(bottomframe,command = lambda: press(3),width=6,height=1,text="3",font=("arial",20,"bold"),bg="black",fg="white").grid(row=4,column=2)
btn_mul = Button(bottomframe,command = lambda: press("*"),width=6,height=1,text="*",font=("arial",20,"bold"),bg="black",fg="white").grid(row=4,column=3)
btn_zero = Button(bottomframe,command = lambda: press(0),width=6,height=1,text="0",font=("arial",20,"bold"),bg="black",fg="white").grid(row=5,column=0)
clear = Button(bottomframe,command = lambda: btn_clear(),width=6,height=1,text="C",font=("arial",20,"bold"),bg="black",fg="white").grid(row=5,column=1)
btn_res = Button(bottomframe,command = lambda: btn_equal(),width=6,height=1,text="=",font=("arial",20,"bold"),bg="black",fg="white").grid(row=5,column=2)
btn_div = Button(bottomframe,command = lambda: press("/"),width=6,height=1,text="/",font=("arial",20,"bold"),bg="black",fg="white").grid(row=5,column=3)

window.mainloop()