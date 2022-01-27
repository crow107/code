from tkinter import *
from tkinter import messagebox
import time as tm
import datetime
top = Tk()
def new_window():
   newWindow=Toplevel(top)
   newWindow.title('Hotel Management')
   newWindow.geometry('1366x768')
   Image = PhotoImage(file = "E://Image//hi.gif")
   newWindow_label=Label(newWindow, image=Image)
   newWindow_label.image = Image
   newWindow_label.place(x=0, y=0, relwidth=1, relheight=1)
   
def login_interface():
   login_interface=Toplevel(top)
   login_interface.geometry('280x380')
   login_interface.title('login')
   login_interface.configure(bg='black')
   login_interface.Login_Here=Label(top,text='Login Here',bg='black',fg='white',font=('times new roman',30,)).place(x=50,y=20)
   Username=Label(login_interface,text='Username',bg='black',fg='white',font=('times new roman',20,)).place(x=20,y=100)
   Password=Label(login_interface,text='Password',bg='black',fg='white',font=('times new roman',20,)).place(x=20,y=180)
   Entry1=Entry(login_interface,font=('times of roman',15)) 
   Entry1.place(x=20,y=150,width=200,height=20)
   Entry2=Entry(login_interface,font=('times of roman',15))
   Entry2.place(x=20,y=230,width=200,height=20)

   Login_button=Button(login_interface,text='LOGIN',command=acommand).place(x=20,y=280)

   def acommand():
      a=Entry1.get()
      b=Entry2.get()
      if a=='':
         messagebox.showerror("Error", "ENTER USERNAME")
      elif b=='':
         messagebox.showerror("Error", "ENTER PASSWORD")
      elif a=='kanishk':
         if b=='rawat':
            new_window()
         else:
            messagebox.showerror("Error", "WRONG PASSWORD")
      else:
         messagebox.showerror("Error","NO SUCH USER")
top = Tk()
top.title('Main screen')
top.geometry('1366x768')
Image = PhotoImage(file = "E://Image//hi.gif")
label=Label(top, image=Image)
label.image = Image
label.place(x=0, y=0, relwidth=1, relheight=1)
#-------button-----
Login_button=Button(top,text='LOGIN',command=login_interface).place(x=100,y=100)
#-------lable---
Label=Label(top,bg='grey',height=3, width=60)
Label.place(x=455,y=600)









top.mainloop
