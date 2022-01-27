from tkinter import *

root = Tk()
root.title("Coin toss")
root.geometry("600x400")
photo1 = PhotoImage(file = "E://Image//calculator3.png")
button = Button(root, bg = "grey", image= photo1 ,text = "Start" ).place(x=200, y=50 , height= 100 , width= 100)


root.mainloop()
