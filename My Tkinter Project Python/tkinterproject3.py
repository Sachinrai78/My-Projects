# Create a labelFrame and add text on it:
from tkinter import *
from tkinter import ttk
win=Tk()
win.title("tk")
win.maxsize(width=400,height=300)
win.minsize(width=400,height=300)
lab1=Label(win,text="This is Label Frame",fg="blue",font="Arial")
lab1.place(x=10,y=10)
lab2=Label(win,text="1.This is a Label.",fg="black",font="Arial")
lab2.place(x=5,y=40)
lab3=Label(win,text="2.This is another Label.",fg="black",font="Arial")
lab3.place(x=5,y=80)
lab3=Label(win,text="3.We can add mutliple widgets in it.",fg="black",font="Arial")
lab3.place(x=5,y=120)
win.mainloop()