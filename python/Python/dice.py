from tkinter import *
import random

def face():
    x=random.randint(0,6)
Dice=Tk()
Dice.title("DICE")
a=Button(Dice,padx=12,pady=12,text=face(),fg='blue')
a.sort()           
Dice.mainloop
