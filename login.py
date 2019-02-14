from tkinter import *
import random
from tkinter import messagebox
import sqlite3

#signin method
def signin():
    root=Tk()
   # curs.execute('create table signin(username,password)')
    label=Label(root,text="USER LOGIN")
    label.grid(row=0,column=1)
   
    l2 = Label(root, width=20,text=" Username",font="calibri")
    l2.grid(row=1,column=0)
    e1 = Entry(root)
    e1.grid(row=1,column=1)
    l3 = Label(root, width=20,text=" Password",font="calibri")
    l3.grid(row=2,column=0)
    e2 = Entry(root)
    e2.grid(row=2,column=1)
    #signin validation
    def callsigninvalid():
        def ok():
            exit(0)
        
        def game():
            root=Tk()
            root.geometry("200x200")
            
            def gen():
                letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
                capt = ""
                for i in range(0,7):
                    capt=capt+random.choice(letters)
                return capt
            l9= Label(root,text=" captcha",font="calibri")
            l9.grid(row=1,column=0)
            captcha=gen()
            en1=Entry.insert(7,captcha)
            en1.grid(row=1,column=1)
            l9= Label(root,text=" Re-Type",font="calibri")
            l9.grid(row=2,column=0)
            e8=Entry(root)
            e8.grid(row=2,column=1)
            l10= Label(root,text=" Score",font="calibri",anchor="center")
            l10.grid(row=4,column=0)
            if(captcha==e8.get()):
                s=s+5
                en2=entry.insert(1,s)
                en2.grid(row=4,column=1)
            else:
                c=c+1
            if(c==3):
                messagebox.showinfo("Out" ,"Game Over"+s)
                exit(0)
            bt=Button(root,text="EXIT",command=ok)
            bt.pack()
            
        #messagebox.showinfo("1","ok")
        root=Tk()
        frm=Frame(root)
        data=(e1.get(),e2.get())
        curs.execute('select username,password1 from login')
        rows=curs.fetchall()
        for row in rows:
            if(data==row):
                messagebox.showinfo(e1.get() ,"login successful")
                l8= Label(root,text=" Instructions!!",font="calibri",anchor="center")
                l8.grid(row=1,column=2)
                l9= Label(root,text=" 1.Type the generated CAPTCHA in the textbox !!",font="calibri")
                l9.grid(row=2,column=0)
                l10= Label(root, text="2.For each correct captcha ,the score will be incremented by 5",font="calibri")
                l10.grid(row=3,column=0)
                l11= Label(root,text=" 3.If you type the captcha incorrectly for three times,you will be out",font="calibri")
                l11.grid(row=4,column=0)
                bb1 = Button(root, text = 'Go', command = game)
                bb1.grid(row=5,column=2)
                break;
            else:
                messagebox.showinfo("Error" ,"Invalid Username and password")
                break;
       

    b3 = Button(root, text = 'Login', command = callsigninvalid)
    b3.grid(row=3,column=1)
            
#signup method
def signup():
    root=Tk()
    #curs.execute('create table login(username,password1,password2,email)')
    l4 = Label(root, width=20,text=" Username",font="calibri")
    l4.pack()
    e3 = Entry(root)
    e3.pack()
    l5= Label(root, width=20,text=" Password",font="calibri")
    l5.pack()
    e4 = Entry(root)
    e4.pack()
    l6= Label(root, width=20,text=" Retype-Password",font="calibri")
    l6.pack()
    e5 = Entry(root)
    e5.pack()
    l7= Label(root, width=20,text=" E-mail ID",font="calibri")
    l7.pack()
    e6 = Entry(root)
    e6.pack()
    #signup validation
    def callsignupvalid():
        name=e3.get()
        pass1=e4.get()
        pass2=e5.get()
        mail=e6.get()
        data=(name,pass1,pass2,mail)
        sql="insert into login values(?,?,?,?)"
        curs.execute(sql,data)
        conn.commit()
        messagebox.showinfo("Done","Registered succesfully")
        signin()
    b4 = Button(root, text = 'Login', command =callsignupvalid )
    b4.pack()
#page 1 for signin and signup
root = Tk()
root.geometry("200x200")
l1= Label(root,text=" Captcha World!!",font="calibri",anchor="center")
l1.pack()
conn=sqlite3.connect('captcha.db')
curs=conn.cursor()
b1 = Button(root, text = 'Sign in', command = signin)
b1.pack()
b2 = Button(root, text = 'Sign up', command = signup)
b2.pack()
root.mainloop()
