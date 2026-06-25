from tkinter import *

root = Tk()
root.title("991MS Calculator")
root.geometry("400x600")

exp = ""

def press(num):
    global exp
    exp += str(num)
    display.delete(0, END)
    display.insert(END, exp)

def equal():
    global exp
    try:
        result = str(eval(exp))
        display.delete(0, END)
        display.insert(END, result)
        exp = result
    except:
        display.delete(0, END)
        display.insert(END, "Error")
        exp = ""

def clear():
    global exp
    exp = ""
    display.delete(0, END)

display = Entry(root, font=("Arial", 24))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('=',4,2),('+',4,3)
]

for (text,row,col) in buttons:
    if text == "=":
        Button(root,text=text,width=8,height=3,
               command=equal).grid(row=row,column=col)
    else:
        Button(root,text=text,width=8,height=3,
               command=lambda t=text: press(t)
               ).grid(row=row,column=col)

Button(root,text="AC",width=35,height=2,
       command=clear).grid(row=5,column=0,columnspan=4)

root.mainloop()