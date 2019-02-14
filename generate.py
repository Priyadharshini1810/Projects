from tkinter import *
import random
from tkinter import messagebox
import sqlite3

def game():
    root=Tk()
    root.geometry("200x200")
    s=0
    c=0    
    def done():
       
        if(e10.get()==e8.get()):
            s=e11.get()
            m=int(s)+5
            e11.delete(0,END)
            e11.insert(0,m)
            e10.delete(0,END)
            e8.delete(0,END)
            e10.insert(7,gen())
            done()
       
              
    def exitt():
        exit(0)
    def gen():
        letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
        capt = ""
        for i in range(0,7):
            capt=capt+random.choice(letters)
        return capt
    l9= Label(root,text=" captcha",font="calibri")
    l9.pack()
    e10=Entry(root)
    e10.pack()
    gen()
    e10.insert(7,gen())
    l11= Label(root,text=" Re-Type",font="calibri")
    l11.pack()
    e8=Entry(root)
    e8.pack()
    bt=Button(root,text="DONE",command=done)
    bt.pack()
    bt1=Button(root,text="EXIT",command=exitt)
    bt1.pack()
    l10= Label(root,text=" SCORE",font="calibri")
    l10.pack()
    e11=Entry(root)
    e11.pack()
    e11.insert(1,0)
root = Tk()
root.geometry("200x200")


l1= Label(root,text=" Captcha World!!",font="calibri",anchor="center")
l1.pack()
bb1 = Button(root, text = 'Go', command = game)
bb1.pack()   
