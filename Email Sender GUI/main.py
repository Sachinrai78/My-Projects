from tkinter import *
from tkinter import messagebox,filedialog
from email.message import EmailMessage
import smtplib
import os
import imghdr
check=False
def attachment():
    global filename,filetype,filepath,check
    check=True

    filepath=filedialog.askopenfilename(initialdir='c:/',title='Select File')
    filetype=filepath.split('.')
    filetype=filetype[1]
    filename=os.path.basename(filepath)
    textarea.insert(END,f'\n{filename}\n')
def sendingEmail(toAddress,subject,body):
    f=open('credentials.txt','r')
    for i in f:
        credentials=i.split(',')

    message=EmailMessage()
    message['subject']=subject
    message['to']=toAddress
    message['from']=credentials[0]
    message.set_content(body)
    if check:
        if filetype=='png' or filetype=='jpg' or filetype=='jpeg':
            f=open(filepath,'rb')
            file_data=f.read()
            subtype=imghdr.what(filepath)
            message.add_attachment(file_data,maintype='image',subtype=subtype,filename=filename)

        else:
            f = open(filepath, 'rb')
            file_data = f.read()
            message.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=filename)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(credentials[0],credentials[1])
    s.send_message(message)
    x=s.ehlo()
    if x[0]==250:
        return 'sent'
    else:
        return 'failed'
def send_email():
    if toEntryField.get()=='' or subjectEntryField.get()=='' or textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','All Fields Are Required',parent=win)

    else:
        if choice.get()=='single':
            result=sendingEmail(toEntryField.get(),subjectEntryField.get(),textarea.get(1.0,END))
            if result=='sent':
                messagebox.showinfo('Success','Email is sent successfulyy')

            if result=='failed':
                messagebox.showerror('Error','Email is not sent.')

        if choice.get()=='multiple':
            sent=0
            failed=0
            for x in final_emails:
                result=sendingEmail(x,subjectEntryField.get(),textarea.get(1.0,END))
                if result=='sent':
                    sent+=1
                if result=='failed':
                    failed+=1

                totalLabel.config(text='')
                sentLabel.config(text='Sent:' + str(sent))
                leftLabel.config(text='Left:' + str(len(final_emails) - (sent + failed)))
                failedLabel.config(text='Failed:' + str(failed))

                totalLabel.update()
                sentLabel.update()
                leftLabel.update()
                failedLabel.update()

            messagebox.showinfo('Success','Emails are sent successfully')
def settings():
    def clear1():
        fromEntryField.delete(0,END)
        passwordEntryField.delete(0,END)

    def save():
        if fromEntryField.get()=='' or passwordEntryField.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=win1)

        else:
            f=open('credentials.txt','w')
            f.write(fromEntryField.get()+','+passwordEntryField.get())
            f.close()
            messagebox.showinfo('Information','CREDENTIALS SAVED SUCCESSFULLY',parent=win1)

    win1=Toplevel()
    win1.title('Setting')
    win1.maxsize(width=660,height=600)
    win1.minsize(width=660,height=600)

    win1.config(bg='skyblue')

    Label(win1,text='Credential Settings',image=logoImage,compound=LEFT,font=('arial',40,'bold'),
          fg='white',bg='blue').grid(padx=60)

    fromLabelFrame = LabelFrame(win1, text='From (Email Address)', font=('times new roman', 16, 'bold'), bd=5, fg='white',
                              bg='dodger blue2')
    fromLabelFrame.grid(row=1, column=0,pady=20)

    fromEntryField = Entry(fromLabelFrame, font=('times new roman', 18, 'bold'), width=30)
    fromEntryField.grid(row=0, column=0)

    passwordLabelFrame = LabelFrame(win1, text='Password', font=('times new roman', 16, 'bold'), bd=5,
                                fg='white',
                                bg='dodger blue2')
    passwordLabelFrame.grid(row=2, column=0, pady=20)

    passwordEntryField = Entry(passwordLabelFrame, font=('times new roman', 18, 'bold'), width=30,show='*')
    passwordEntryField.grid(row=0, column=0)

    Button(win1,text='SAVE',font=('times new roman',18,'bold'),cursor='hand2',bg='gold',fg='black'
           ,command=save).place(x=210,y=280)
    Button(win1,text='CLEAR',font=('times new roman',18,'bold'),cursor='hand2',bg='gold2',fg='black'
           ,command=clear1).place(x=340,y=280)

    f=open('credentials.txt','r')
    for i in f:
        credentials=i.split(',')
    fromEntryField.insert(0,credentials[0])
    passwordEntryField.insert(0,credentials[1])
    win1.mainloop()
def iexit():
    result=messagebox.askyesno('Notification','Do you want to exit?')
    if result:
        win.destroy()
    else:
        pass

def clear():
    toEntryField.delete(0,END)
    subjectEntryField.delete(0,END)
    textarea.delete(1.0,END)

win=Tk()
win.title('Email sender app')
win.geometry('780x620+100+50')
win.resizable(0,0)
win.config(bg='skyblue')

titleFrame=Frame(win,bg='white')
titleFrame.grid(row=0,column=0)
logoImage=PhotoImage(file='email.png')
titleLabel=Label(titleFrame,text='  Email Sender',image=logoImage,compound=LEFT,font=('arial',28,'bold'),
                 bg='white',fg='blue')
titleLabel.grid(row=0,column=0)
settingImage=PhotoImage(file='setting.png')

Button(titleFrame,image=settingImage,bd=0,bg='white',cursor='hand2',activebackground='white'
       ,command=settings).grid(row=0,column=1,padx=20)

chooseFrame=Frame(win,bg='skyblue')
chooseFrame.grid(row=1,column=0,pady=10)
choice=StringVar()

singleRadioButton=Radiobutton(chooseFrame,text='Single',font=('times new roman',25,'bold')
                              ,variable=choice,value='single',bg='skyblue',activebackground='skyblue')
singleRadioButton.grid(row=0,column=0,padx=20)

multipleRadioButton=Radiobutton(chooseFrame,text='Multiple',font=('times new roman',25,'bold')
                              ,variable=choice,value='multiple',bg='skyblue',activebackground='skyblue')
multipleRadioButton.grid(row=0,column=1,padx=20)

choice.set('single')

toLabelFrame=LabelFrame(win,text='To (Email Address)',font=('times new roman',16,'bold'),bd=5,fg='white',bg='skyblue')
toLabelFrame.grid(row=2,column=0,padx=100)

toEntryField=Entry(toLabelFrame,font=('times new roman',18,'bold'),width=30)
toEntryField.grid(row=0,column=0)

browseImage=PhotoImage(file='browse.png')

browseButton=Button(toLabelFrame,text=' Browse',image=browseImage,compound=LEFT,font=('arial',12,'bold'),
       cursor='hand2',bd=0,bg='skyblue',activebackground='skyblue',state=DISABLED)
browseButton.grid(row=0,column=1,padx=20)

subjectLabelFrame=LabelFrame(win,text='Subject',font=('times new roman',16,'bold'),bd=5,fg='white',bg='skyblue')
subjectLabelFrame.grid(row=3,column=0,pady=10)

subjectEntryField=Entry(subjectLabelFrame,font=('times new roman',18,'bold'),width=30)
subjectEntryField.grid(row=0,column=0)

emailLabelFrame=LabelFrame(win,text='Compose Email',font=('times new roman',16,'bold'),bd=5,fg='white',bg='skyblue')
emailLabelFrame.grid(row=4,column=0,padx=20)
attachImage=PhotoImage(file='attachments.png')

Button(emailLabelFrame,text=' Attachment',image=attachImage,compound=LEFT,font=('arial',12,'bold'),
       cursor='hand2',bd=0,bg='skyblue',activebackground='skyblue',command=attachment).grid(row=0,column=0)

textarea=Text(emailLabelFrame,font=('times new roman',14,),height=8)
textarea.grid(row=1,column=0,columnspan=2)

sendImage=PhotoImage(file='send.png')
Button(win,image=sendImage,bd=0,bg='skyblue',cursor='hand2',activebackground='skyblue'
       ,command=send_email).place(x=490,y=540)

clearImage=PhotoImage(file='clear.png')
Button(win,image=clearImage,bd=0,bg='skyblue',cursor='hand2',activebackground='skyblue'
       ,command=clear).place(x=590,y=550)

exitImage=PhotoImage(file='exit.png')
Button(win,image=exitImage,bd=0,bg='skyblue',cursor='hand2',activebackground='skyblue'
       ,command=iexit).place(x=690,y=550)

totalLabel=Label(win,font=('times new roman',18,'bold'),bg='skyblue',fg='black')
totalLabel.place(x=10,y=560)

sentLabel=Label(win,font=('times new roman',18,'bold'),bg='skyblue',fg='black')
sentLabel.place(x=100,y=560)

leftLabel=Label(win,font=('times new roman',18,'bold'),bg='skyblue',fg='black')
leftLabel.place(x=190,y=560)

failedLabel=Label(win,font=('times new roman',18,'bold'),bg='skyblue',fg='black')
failedLabel.place(x=280,y=560)

win.mainloop()