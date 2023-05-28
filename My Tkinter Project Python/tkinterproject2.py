# Write a program to create a window and add a simple button or checkbox like:
from tkinter  import *
from tkinter import ttk
win=Tk()
win.title("tk")
win.maxsize(width=400,height=300)
win.minsize(width=400,height=300)
lbl=Label(win,text="This is Label Frame",fg="blue",font="arial")
lbl.place(x=10,y=10)
btn1=Button(win,text="Button 1",fg="black",bd=5)
btn1.place(x=50,y=40)
btn2=Button(win,text="Button 2",fg="black",bd=5)
btn2.place(x=150,y=40)
chbtn1=Checkbutton(win,text="Checkbutton 1",fg="black")
chbtn1.place(x=50,y=100)
chbtn2=Checkbutton(win,text="Checkbutton 2",fg="black")
chbtn2.place(x=50,y=150)
win.mainloop()