from tkinter import *

root = Tk()
root.title('background image')

image1 = PhotoImage(file='E://Image//login.gif')

# get the image size
w = image1.width()
h = image1.height()

# make the root window the size of the image
root.geometry("%dx%d" % (w, h))

# root has no image argument, so use a label as a panel
panel1 = Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')

# put a button/label on the image panel to test it
label1 = Label(panel1, text='here i am').pack()
root.wm_attributes("-transparentcolor")




# start the event loop
root.mainloop()
