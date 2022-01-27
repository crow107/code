import time
from tkinter import *

top=Tk()
top.geometry('359x150')

top.configure(bg='black')
top.resizable(0,0)

def start():
    text=time.strftime('%H:%M:%S')
    label.config(text=text)
    label.after(200,start)
label=Label(top,font=('ds-digital',50,'bold'),bg='black',fg='blue',bd=50)
label.grid(row=0,column=1)
start()
print('done')
top.mainloop()
