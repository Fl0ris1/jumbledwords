import tkinter
from tkinter import *
import random
from tkinter import messagebox


answers = [
    "apple",
    "mango",
    "banana",
    "achieve",
    "london",
    "evening",
    "servant",
    "receiver",
    "london",
    "ferrari",
    "hollow",
    "horror",
    "master",
    "morning",
    "bottle",
    "pen",
    "router",
    "copy",
    "narrow",
    "wide",
    "dive",
    "love",
    "block",
    "right",
    "simple",
    "deaf",
    "single",
    "knight",
    "hope",
]

words=[]

def jumble():
    for word in answers:
        new_word=random.shuffle(word)
        words.append(new_word)

root=Tk()


root.title("Jumbled Word Game")
root.geometry("500x500+500+150")
root.config(background="#8FB8DE")

heading_lbl=Label(root,text="Jumbled Word Game",font=("consolas",18,"bold"),bg="#8FB8DE",fg="#EC5766")
heading_lbl.pack(pady=5)

text_lbl=Label(root,font=("consolas",16,"bold"),bg="#8FB8DE",fg="#4E4C67")
text_lbl.pack(pady=30,ipadx=10,ipady=10)

ans=StringVar()

input_box=Entry(root,background="#8980F5",font=("consolas",16,"bold"),textvariable=ans)
input_box.pack(ipadx=5,ipady=5)

check_btn=Button(root,text="Check",font=("consolas",18,"bold"),bg="#5438DC",fg="#85BDBF",width=10)
check_btn.pack(pady=40)

reset_btn=Button(root,text="Reset",font=("consolas",18,"bold"),bg="#5438DC",fg="#85BDBF",width=10)
reset_btn.pack()









root.mainloop()