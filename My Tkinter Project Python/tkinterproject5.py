# How to Create optionMenu in tkinter
from tkinter import *
win=Tk()
win.title("Vinayak App")
win.maxsize(width=400,height=300)
win.minsize(width=400,height=300)
lbl=Label(win,text="Choose the week day here",fg='black',font="arial")
lbl.place(x=5,y=5)
variable = StringVar()
variable.set("Weekdays")
o= OptionMenu(win, variable, "Sunday","Monday", "Tuesday", "Wednesday","Thursday", "Friday","Saturday")
o.config(bg="GREEN", fg="WHITE")
o["menu"].config(bg="RED")
o.place(x=20,y=50)
win.mainloop()









