from tkinter import *

class OnOffButton(Button):
    def __init__(self,master=None,text=None):
        Button.__init__(self,master,text=text)
        self['command'] = self._onButtonClick

    def _onButtonClick(self):
        print('button clicked')
class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)

        self.labelHello = Label(self,text="Hello World")
        self.labelHello['fg'] = "red"
        self.labelHello.grid()

        self.button1 = OnOffButton(self,text="Click Me")
        self.button1.grid()

        self.button2 = OnOffButton(self,text="Click me?")
        self.button2.grid()

def main():
    root = Tk()
    app = App(master=root)
    app.grid()
    root.mainloop()

if __name__ == '__main__':
    main()
