from tkinter import *
import random as r
import sys
from tkinter import messagebox
#---------------button-------
def button(frame):
   b=Button(frame,padx=1,bg="papaya whip",width=3,text="   ",font=('arial',60,'bold'),relief=FLAT,bd=10)
   return b
def reset():                
   for i in range(9):
      b[no]["text"]=" "
      b[no]["state"]=NORMAL

def check():                
   if (b1["text"]==b2["text"]==b3["text"]) :
      messagebox.showinfo("Congrats!!","'"a"' has won")
   elif (b4["text"]=b5["text"]=b6["text"]):
      messagebox.showinfo("Congrats!!",a" has won")
   elif (b7["text"]=b8["text"]=b9["text"]):
      messagebox.showinfo("Congrats!!",a" has won")
   elif (b1["text"]==b4["text"]==b7["text"]) :
      messagebox.showinfo("Congrats!!","'"a"' has won")
   elif (b2["text"]=b5["text"]=b8["text"]):
      messagebox.showinfo("Congrats!!",a" has won")
   elif (b3["text"]=b6["text"]=b9["text"]):
      messagebox.showinfo("Congrats!!",a" has won")
   elif (b1["text"]=b5["text"]=b9["text"]):
      messagebox.showinfo("Congrats!!",a" has won")
   elif (b3["text"]=b5["text"]=b7["text"]):
      messagebox.showinfo("Congrats!!",a" has won")   
   elif (b1["state"]==b2["state"]==b3["state"]==b4["state"]==b5["state"]==b6["state"]==b7["state"]==b8["state"]==b9["state"]==DISABLED):
      messagebox.showinfo("Tied!!","The match ended in a draw")
def click(no):  
   b[no].config(text=a,state=DISABLED,disabledforeground=colour[a])
   check()
top=Tk()
top.title('tic tak toe')
top.geometry('1366x768')
top.configure(bg='black')
top.resizable(0,0)
#----------frame---------------
canvas=Canvas(top)
canvas.place(x=500,y=130,width=5,height=540)
canvas1=Canvas(top)
canvas1.place(x=800,y=130,width=5,height=540)
canvas2=Canvas(top)
canvas2.place(x=250,y=285,width=800,height=5)
canvas3=Canvas(top)
canvas3.place(x=250,y=485,width=800,height=5)
#------------label--------------
name=Label(top,text='TIC TAK TOE',font=('fixedsys',50),bg='black',fg='white')
name.place(x=420,y=10)
a=r.choice(['O','X'])       
colour={'O':"deep sky blue",'X':"lawn green"}

