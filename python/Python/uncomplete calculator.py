from tkinter import *

def btnclick(numbers):
   global operator
   operator=operator+str(numbers)
   text_input.set(operator)

def btnClear():
   global operator
   operator=""
   text_input.set('')

def btnEqual():
   global operator
   sumup=str(eval(operator))
   text_input.set(sumup)
   operator=""

cal=Tk()
cal.title("calculater")
operator=""
text_input=StringVar()

textdisplay=Entry(cal,font=("arial",20,"bold"),bd=30,textvariable=text_input,bg="green",insertwidth=4,justify='right').grid(columnspan=4)

btn7=Button(cal,padx=20,fg="black",bd=16,bg="green",font=("arial",20,"bold"),text="7",command=lambda:btnclick(7)).grid(row=1,column=0)

cal.mainloop
