import tkinter
from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.title("Jumbled Word Game")
root.geometry("500x500+500+150")
root.config(background="#8FB8DE")

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
    global words
    my_list=[]
    new_word=""
    for word in answers:
        new_word=""
        my_list=[]
        for ch in word:
            my_list.append(ch)
        random.shuffle(my_list) 
        new_word="".join(my_list)
        words.append(new_word)
        
    return words

main_words=jumble()  
num=random.randrange(0,len(main_words),1)
score=0
q_count=0
score_txt=""
s_lbl=Label(root)

def default():
    global main_words, answers, num
    text_lbl.config(text=main_words[num])

def reset():
    global main_words, answers, num
    num=random.randrange(0,len(main_words),1)    
    text_lbl.config(text=main_words[num])
    input_box.delete(0,END)

def check_ans():
    global main_words, answers, num, score, q_count, score_txt, s_lbl
    q_count+=1
    input_answer=input_box.get()
    if input_answer==answers[num]:
        score+=1
        messagebox.showinfo("CORRECT","YOUR ANSWER IS CORRECT")
    
    else:
        messagebox.showerror("INCORRECT","YOUR ANSWWER IS INCORRECT")

    score_txt="score: "+str(score)+"/"+str(q_count)
    s_lbl.forget()
    s_lbl=Label(root,text=score_txt,font=("consolas",18,"bold"),bg="#8FB8DE",fg="#5438DC")
    s_lbl.pack(side=LEFT)
    reset()

heading_lbl=Label(root,text="Jumbled Word Game",font=("consolas",18,"bold"),bg="#8FB8DE",fg="#EC5766")
heading_lbl.pack(pady=5)

text_lbl=Label(root,font=("consolas",16,"bold"),bg="#8FB8DE",fg="#4E4C67")
text_lbl.pack(pady=30,ipadx=10,ipady=10)

ans=StringVar()

input_box=Entry(root,background="#8980F5",font=("consolas",16,"bold"),textvariable=ans)
input_box.pack(ipadx=5,ipady=5)

check_btn=Button(root,text="Check",font=("consolas",18,"bold"),bg="#5438DC",fg="#85BDBF",width=10,command=check_ans)
check_btn.pack(pady=40)

reset_btn=Button(root,text="Reset",font=("consolas",18,"bold"),bg="#5438DC",fg="#85BDBF",width=10,command=reset)
reset_btn.pack()







default()

root.mainloop()