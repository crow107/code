from tkinter import *
top=Tk()
top.title('checkbox')
var=IntVar()
Checkbutton(top, text="Mix Veg                                ",font=('times of roman',15), variable=var).place(x=0,y=0)
def bill():
   a=var.get()
   if a==1:
      print('mixed veg')
   else:
      c=1


B=Button(top,command=bill).place(x=100,y=0)

