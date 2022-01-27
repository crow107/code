from tkinter import *
from tkinter import messagebox
import random as r
def button(frame):
    b=Button(frame,bg="papaya whip",text="   ",font=('arial',60,'bold'),relief=FLAT,bd=10)
    return b
def change_a():         
    global a
    for i in ['O','X']:
          if not(i==a):
             a=i
             break
def reset():    
      global a
      for i in range(3):
          for j in range(3):
                  b[i][j]["text"]=" "
                  b[i][j]["state"]=NORMAL

def check():            
      for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                      messagebox.showinfo("Congrats!!","'"+a+"' has won")
                      reset()
      if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
         messagebox.showinfo("Congrats!!","'"+a+"' has won")
         reset()   
      elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
          messagebox.showinfo("Tied!!","The match ended in a draw")
          reset()
def click(row,col):
         b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
         check()
         change_a()
#----------- Main Program ---------#
top=Tk()
top.title('tic tak toe')
top.geometry('1366x768')
top.configure(bg='white')
top.resizable(0,0)

#------------label--------------
Image = PhotoImage(file = "E://Image//hi.gif")
label=Label(top, image=Image)
label.image = Image
label.place(x=0, y=0, relwidth=1, relheight=1)
name=Label(top,text='TIC TAK TOE',font=('fixedsys',50),bg='white',fg='black')
name.place(x=400,y=30) 
a=r.choice(['O','X'])       
colour={'O':"deep sky blue",'X':"lawn green"}
b=[[],[],[]]
for i in range(3):
      for j in range(3):
               b[i].append(button(top))
               b[i][j].config(command= lambda row=i,col=j:click(row,col))
for i in range(3):
    b[0][i].place(x=250*(i+1),y=160,width=250,height=160)
for i in range(3):
    b[1][i].place(x=250*(i+1),y=320,width=250,height=160)
for i in range(3):
    b[2][i].place(x=250*(i+1),y=480,width=250,height=160)

#----------frame---------------
canvas=Canvas(top,bg='black')
canvas.place(x=500,y=160,width=15,height=480)
canvas1=Canvas(top,bg='black')
canvas1.place(x=750,y=160,width=15,height=480)
canvas2=Canvas(top,bg='black')
canvas2.place(x=250,y=320,width=750,height=15)
canvas3=Canvas(top,bg='black')
canvas3.place(x=250,y=480,width=750,height=15)
top.mainloop()



