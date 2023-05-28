# WAP to create a window there is one label and 4 checkbox buttons like:
from tkinter import *
from  tkinter import ttk
win=Tk()
win.title("tk")
win.maxsize(width=600,height=300)
win.minsize(width=600,height=300)
lbl=Label(win,text="Select Programming Language Of Your Choice",font="arial")
lbl.place(x=10,y=5)
def func():
    print(checkbtn1.get())
    print(checkbtn2.get())
    print(checkbtn3.get())
    print(checkbtn4.get())
checkbtn1=IntVar()
checkbtn2=IntVar()
checkbtn3=IntVar()
checkbtn4=IntVar()
select=Checkbutton(win,text="Java",variable=checkbtn1,font="arial")
select.place(x=30,y=40)
select=Checkbutton(win,text="C++",variable=checkbtn2,font="arial")
select.place(x=30,y=70)
select=Checkbutton(win,text="Python",variable=checkbtn3,font="arial")
select.place(x=30,y=100)
select=Checkbutton(win,text="C",variable=checkbtn4,font="arial")
select.place(x=30,y=130)


win.mainloop()
