from tkinter import *
root = Tk()
root.title("calculator")
a = Entry(root, width = 20, borderwidth= 5)
a.grid(row=0, column=0, columnspan=2, padx = 5, pady=5)
e = Entry(root, width= 35, borderwidth=5)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))
    global curr
    curr = a.get()
    a.delete(0, END)
    a.insert(0, curr + str(number))


def clear():
    e.delete(0, END)
    a.delete(0, END)

def calc(symbol):
    global sign
    sign = symbol
    global num1
    num1 = e.get()
    curr = a.get()
    if "=" in curr:
        a.delete(0, END)
        a.insert(0, e.get() + sign)
    else:
        a.delete(0, END)
        a.insert(0, curr + sign)

    e.delete(0, END)

def equal():
   num2 = e.get()
   curr= a.get()
   e.delete(0, END)
   if sign == "+":
       e.insert(0, int(num1) + int(num2))
   if sign == "-":
       e.insert(0, int(num1) - int(num2))
   if sign == "*":
       e.insert(0, int(num1) * int(num2))
   if sign == "/":
       e.insert(0, int(num1) / int(num2))
   a.delete(0, END)
   a.insert(0, curr + "=" + e.get())


one = Button(root, text="1", padx=40, pady=20, command= lambda:click(1))
one.grid(row=4, column=0)
two = Button(root, text="2", padx=40, pady=20, command= lambda:click(2))
two.grid(row=4, column=1)
three = Button(root, text="3", padx=40, pady=20, command= lambda:click(3))
three.grid(row=4, column=2)
four = Button(root, text="4", padx=40, pady=20, command= lambda:click(4))
four.grid(row=3, column=0)
five= Button(root, text="5", padx=40, pady=20, command= lambda:click(5))
five.grid(row=3, column=1)
six= Button(root, text="6", padx=40, pady=20, command= lambda:click(6))
six.grid(row=3, column=2)
seven = Button(root, text="7", padx=40, pady=20, command= lambda:click(7))
seven.grid(row=2, column=2)
eight= Button(root, text="8", padx=40, pady=20, command= lambda:click(8))
eight.grid(row=2, column=1)
nine= Button(root, text="9", padx=40, pady=20, command= lambda:click(9))
nine.grid(row=2, column=0)
zero= Button(root, text="0", padx=40, pady=20, command= lambda:click(0))
zero.grid(row=5, column=0)
plus = Button(root, text="+", padx=39, pady=20, command=lambda:calc("+"))
plus.grid(row=2, column=3)
minus = Button(root, text="-", padx=39, pady=20, command=lambda:calc("-"))
minus.grid(row=3, column=3)
mult = Button(root, text="*", padx=39, pady=20, command=lambda:calc("*"))
mult.grid(row=4, column=3)
div = Button(root, text="/", padx=39, pady=20, command=lambda:calc("/"))
div.grid(row=5, column=3)
equal = Button(root, text="=", padx=91, pady=20, command= equal)
equal.grid(row=6, column=0, columnspan=3)
clear = Button(root, text="clear", padx=79, pady=20, command=clear)
clear.grid(row=5, column=1, columnspan=2)

root.mainloop()