from tkinter import * 
  
 
master = Tk() 
  

l1 = Label(master, text = "First:") 
l2 = Label(master, text = "Second:") 
  

l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
l2.grid(row = 1, column = 0, sticky = W, pady = 2) 
  
e1 = Entry(master) 
e2 = Entry(master) 
  
e1.grid(row = 0, column = 1, pady = 2) 
e2.grid(row = 1, column = 1, pady = 2) 
   
master.mainloop() 
