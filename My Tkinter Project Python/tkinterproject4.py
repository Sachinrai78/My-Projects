# Write a program to create ListBox:
from tkinter import *
from tkinter import messagebox
win= Tk()
win.title("tk")
win.maxsize(width=300,height=250)
win.minsize(width=300,height=250)
lbl=Label(win,text="FOOD ITEMS",fg="black",font="arial")
lbl.pack()
lst=Listbox(win,width=20,height=20,bg="grey",fg="yellow",font="arial")
lst.pack()
items=["Nachos","Sandwich","Burger","Pizza","Burrito"]
for i in items:
    lst.insert(END,i,)
win.mainloop()