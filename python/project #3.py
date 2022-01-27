
from tkinter import *
from tkinter import messagebox
import time 
import datetime
import random as r
import sys
# import mysql.connector
# import wolframalpha
# import wikipedia
# import speech_recognition as sr
#---------------------------window-------------------------------------------------
def window():
   Window=Toplevel(top)
   Window.title('All apps')
   Window.geometry('455x768')
   Window.resizable(0,0)
   Image = PhotoImage(file = "E://Image//hi.gif")
   label=Label(Window, image=Image)
   label.image = Image
   label.place(x=0, y=0, relwidth=1, relheight=1)
   def tic_tak_toe():
      def button(frame):          
          b=Button(frame,bg="papaya whip",text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
          return b
      def change_a():             
          nonlocal a
          for i in ['O','X']:
              if i!=a:
                  a=i
                  break
      def reset():               
          nonlocal a
          for i in range(3):
              for j in range(3):
                   b[i][j]["text"]=" "
                   b[i][j]["state"]=NORMAL
          a=r.choice(['O','X'])
      def check():                
          for i in range(3):
               if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                       messagebox.showinfo("Congrats!!","'"+a+"' has won")
                       reset()
               elif(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
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
      tic_tak_toe=Tk()
      tic_tak_toe.title('tic tak toe')
      tic_tak_toe.geometry('1366x768')
      tic_tak_toe.configure(bg='white')
      tic_tak_toe.resizable(0,0)

      #------------label--------------
      name=Label(tic_tak_toe,text='TIC TAK TOE',font=('fixedsys',50),bg='white',fg='black')
      name.place(x=400,y=30) 
      a=r.choice(['O','X'])       
      colour={'O':"deep sky blue",'X':"lawn green"}
      b=[[],[],[]]
      for i in range(3):
            for j in range(3):
                  b[i].append(button(tic_tak_toe))
                  b[i][j].config(command= lambda row=i,col=j:click(row,col))
      for i in range(3):
          b[0][i].place(x=250*(i+1),y=160,width=250,height=160)
      for i in range(3):
          b[1][i].place(x=250*(i+1),y=320,width=250,height=160)
      for i in range(3):
          b[2][i].place(x=250*(i+1),y=480,width=250,height=160)

      #----------frame---------------
      canvas=Canvas(tic_tak_toe,bg='black')
      canvas.place(x=500,y=160,width=15,height=480)
      canvas1=Canvas(tic_tak_toe,bg='black')
      canvas1.place(x=750,y=160,width=15,height=480)
      canvas2=Canvas(tic_tak_toe,bg='black')
      canvas2.place(x=250,y=320,width=750,height=15)
      canvas3=Canvas(tic_tak_toe,bg='black')
      canvas3.place(x=250,y=480,width=750,height=15)
      tic_tak_toe.mainloop()
   #------------------------calculator--------------------------------------------------------
   def calculator():
      def btnClick(numbers):
         nonlocal operator
         operator=operator + str(numbers)
         text_Input.set(operator)

      def btnClearDisplay():
         global operator
         operator=""
         text_Input.set("")
      def btnEqualsInput():
         nonlocal operator
         sumup=str(eval(operator))
         text_Input.set(sumup)
         operator=""

      cal = Toplevel(top)
      cal.title("calculator")
      operator=""
      text_Input =StringVar()

      txtDisplay = Entry(cal,font=('arial',20,'bold'),
                      textvariable=text_Input, bd=30,insertwidth=4,
                      bg="light blue",justify='right').grid(columnspan=4)


      btn7=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="7",command=lambda:btnClick(7)).grid(row=1,column=0)

      btn8=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="8",command=lambda:btnClick(8)).grid(row=1,column=1)

      btn9=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="9",command=lambda:btnClick(9)).grid(row=1,column=2)

      Addition=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="+",command=lambda:btnClick("+")).grid(row=1,column=3)
      #=============================================================================================================
      btn4=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="4",command=lambda:btnClick(4)).grid(row=2,column=0)

      btn5=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="5",command=lambda:btnClick(5)).grid(row=2,column=1)

      btn6=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
   
      subtraction=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="-",command=lambda:btnClick("-")).grid(row=2,column=3)
      #===================================================================================================================
      btn1=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="1",command=lambda:btnClick(1)).grid(row=3,column=0)

      btn2=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="2",command=lambda:btnClick(2)).grid(row=3,column=1)

      btn3=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
   
      multiply=Button(cal,padx=16,bg="light blue",bd=8,fg="black",font=('are-ial',20,'bold'),
               text="*",command=lambda:btnClick("*")).grid(row=3,column=3)
      #=====================================================================================================
      btn0=Button(cal,padx=16,pady=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="0",command=lambda:btnClick(0)).grid(row=4,column=0)

      btnClear=Button(cal,padx=16,pady=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="C",command= btnClearDisplay).grid(row=4,column=1)
   
      btnequal=Button(cal,padx=16,pady=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="=",command=btnEqualsInput).grid(row=4,column=2)

      division=Button(cal,padx=16,pady=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="/",command=lambda:btnClick("/")).grid(row=4,column=3)
   
   #-----------------------login_interface---------------------------------------------------------------      
   def login_interface():
      def message():
         a=Entry1.get()
         b=Entry2.get()
         if a=='':
            messagebox.showerror("Error", "ENTER USERNAME")
         elif b=='':
            messagebox.showerror("Error", "ENTER PASSWORD")
         elif a=='k':
            if b=='r':
               new_window()
            else:
               messagebox.showerror("Error", "WRONG PASSWORD")
         else:
            messagebox.showerror("Error","NO SUCH USER")
      login_interface=Toplevel(top)
      login_interface.geometry('280x330')
      login_interface.title('login')
      login_interface.configure(bg='black')
      login_interface.Login_Here=Label(login_interface,text='Login Here',bg='black',fg='white',font=('times new roman',30,)).place(x=50,y=20)
      Username=Label(login_interface,text='Username',bg='black',fg='white',font=('times new roman',20,)).place(x=30,y=100)
      Password=Label(login_interface,text='Password',bg='black',fg='white',font=('times new roman',20,)).place(x=30,y=170)
      Entry1=Entry(login_interface,font=('times of roman',15)) 
      Entry1.place(x=30,y=140,width=200,height=20)
      Entry2=Entry(login_interface,font=('times of roman',15))
      Entry2.place(x=30,y=210,width=200,height=20)

      Login_button=Button(login_interface,text='LOGIN',command=message).place(x=30,y=260)
   #--------------------------clock------------------------------------------------------
   def clock():
      clock=Toplevel(top)
      clock.geometry('359x150')
      clock.configure(bg='black')
      clock.resizable(0,0)
      text=time.strftime('%H:%M:%S')
      label=Label(clock,text=text,font=('ds-digital',50,'bold'),bg='black',fg='lawn green')
      label.place(x=30,y=20)
   #-------wikipedia--------------------
   def wikipedia():
      def get():
      
         try:
               a=entryk.get()
               answer1 = wikipedia.summary(a)
               label1 = Label(window1,fg='white',text=answer1, font='times 15 bold')
               label1.place(x=0,y=250)
         except Exception as e:
               labeld=Label(window1,text='again')
               labeld.pack()
      kwikipedia=Toplevel(top)
      kwikipedia.geometry('1366x768')
      window1 = Toplevel(kwikipedia)
      window1.geometry("1366x768")
      r=sr.Recognizer()
      Image = PhotoImage(file = "E://Image//wiki.png")
      label=Label(kwikipedia, image=Image)
      label.image = Image
      label.place(x=0,y=0)
      entryk = Entry(kwikipedia,bg="white")
      entryk.place(width=450,height=55,x=425,y=551)
    
      button= Button(kwikipedia,image=P1,relief=FLAT,command=get)
      button.place(x=875,y=550,width=65,height=55)
      try:
               answer1 = wikipedia.summary(a)
               label1 = Label(window1,fg='white',text=answer1, font='times 15 bold')
               label1.place(x=0,y=250)
      except Exception as e:
               labeld=Label(window1,text='again')
               labeld.pack()      
#--------------------------KAsistant-----------------------------------------------
   def KAsistant():
      window = Toplevel(top)
      window.geometry("700x600")
      r=sr.Recognizer()
      with sr.Microphone() as source:
         audio = r.listen(source)
         try:
               text1 = r.recognize_google(audio)
               if text1 == "stop":
                  label4=Label(KAsistant,text='OK')
                  label4.pack()
               else:
                  try:
                        app_id = "5R9TL5-TR9PUHAHW7"
                        client = wolframalpha.Client(app_id)
                        res = client.query(text1)
                        answer = next(res.results).text
                        label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')
                        label1.pack()
               
                  except Exception as e:
                        answer1 = wikipedia.summary(text1)
                        label1 = Label(window, justify=LEFT, compound=CENTER, text=answer, font='times 15 bold')
                        label1.pack()
         except Exception as e:
               labeld=Label(window,text='again')
               labeld.pack()
    
   #-------------------------new_window-------------------------------------------------------------------

   def new_window():
      def details():
         a=Entry4.get()
         b=Entry5.get()
         c=Entry6.get()
         d=Entry7.get()
         f=open("school.txt" ,"a")
         f.write(c)
         f.write('\t')
         f.write(d)
         f.write('\t')
         f.write(a)
         f.write('\t')
         f.write(b)
         f.write('\n')
      def Read():
         Read=Toplevel(top)
         Read.title('Details')
         Read.geometry('1366x768')
         Read.configure(bg='black')
         f=open("school.txt" ,"r")
         read=f.read()
         label=Label(Read,text=read,bg='black',fg='white',font=('times new roman',25))
         label.place(x=10,y=20)
   

      newWindow=Toplevel(top)
      newWindow.title('Hotel Management')
      newWindow.geometry('1366x768')
      newWindow.configure(bg='black')
      #--------label-----
      name=Label(newWindow,text='Name',bg='black',fg='white',font=('times new roman',25)).place(x=50,y=70)
      PhoneNo=Label(newWindow,text='Phone number',bg='black',fg='white',font=('times new roman',25,)).place(x=20,y=120)
      Hotel=Label(newWindow,text='PARADISE',bg='black',fg='white',font=('times new roman',30,)).place(x=455,y=10)
      OrderNo=Label(newWindow,text='Order number',bg='black',fg='white',font=('times new roman',25,)).place(x=500,y=70)
      Date=Label(newWindow,text='Amount',bg='black',fg='white',font=('times new roman',25,)).place(x=500,y=120)
      Roti=Label(newWindow,text='           Roti       ',bg='white',fg='black',font=('times new roman',25,)).place(x=20,y=200)
      Naan=Label(newWindow,text='         Naan        ',bg='black',fg='white',font=('times new roman',25,)).place(x=250,y=200)
      Nonveg=Label(newWindow,text='           Non Veg       ',bg='white',fg='black',font=('times new roman',25,)).place(x=500,y=200)
      Veg=Label(newWindow,text='         Veg        ',bg='black',fg='white',font=('times new roman',25,)).place(x=740,y=200)
      Ice=Label(newWindow,text='           Ice         ',bg='white',fg='black',font=('times new roman',25,)).place(x=20,y=420)
      Cream=Label(newWindow,text='         Cream        ',bg='black',fg='white',font=('times new roman',25,)).place(x=250,y=420)
      Drink=Label(newWindow,text='           Drink        ',bg='white',fg='black',font=('times new roman',25,)).place(x=500,y=420)
      Beverages=Label(newWindow,text='         Beverages        ',bg='black',fg='white',font=('times new roman',25,)).place(x=740,y=420)

   
      #--------checkbox---------
      var1 = IntVar()
      Checkbutton(newWindow, text="Paratha                    ",font=('times of roman',15), variable=var1).place(x=20,y=250)
      var2 = IntVar()  
      Checkbutton(newWindow, text="Roti                        ",font=('times of roman',15), variable=var2).place(x=20,y=280)
      var3 = IntVar()         
      Checkbutton(newWindow, text="Naan                       ",font=('times of roman',15), variable=var3).place(x=20,y=310)
      var4 = IntVar()
      Checkbutton(newWindow, text="Butter Naan             ",font=('times of roman',15), variable=var4).place(x=20,y=340)
      var5 = IntVar()
      Checkbutton(newWindow, text="Methi Roti               ",font=('times of roman',15), variable=var5).place(x=20,y=370)
      var6 = IntVar()
      Checkbutton(newWindow, text="Chicken Tandoori              ",font=('times of roman',15), variable=var6).place(x=500,y=250)
      var7 = IntVar()  
      Checkbutton(newWindow, text="Chicken Tandoori kabab       ",font=('times of roman',15), variable=var7).place(x=500,y=280)
      var8 = IntVar()         
      Checkbutton(newWindow, text="Butter Paneer                       ",font=('times of roman',15), variable=var8).place(x=500,y=310)
      var9 = IntVar()
      Checkbutton(newWindow, text="Mix Veg                                ",font=('times of roman',15), variable=var9).place(x=500,y=340)
      var10 = IntVar()
      Checkbutton(newWindow, text="Dal Makhani                         ",font=('times of roman',15), variable=var10).place(x=500,y=370)
      var11 = IntVar()
      Checkbutton(newWindow, text="Mineral Water                   ",font=('times of roman',15), variable=var11).place(x=20,y=470)
      var12 = IntVar()  
      Checkbutton(newWindow, text="Coke                        ",font=('times of roman',15), variable=var12).place(x=20,y=500)
      var13 = IntVar()         
      Checkbutton(newWindow, text="Tea                          ",font=('times of roman',15), variable=var13).place(x=20,y=530)
      var14 = IntVar()
      Checkbutton(newWindow, text="Sweet Lassi            ",font=('times of roman',15), variable=var14).place(x=20,y=560)
      var15 = IntVar()
      Checkbutton(newWindow, text="Coffee                       ",font=('times of roman',15), variable=var15).place(x=20,y=590)
      var16 = IntVar()
      Checkbutton(newWindow, text="Ice cream                      ",font=('times of roman',15), variable=var16).place(x=500,y=470)
      var17 = IntVar()   
      Checkbutton(newWindow, text="Choco lava Cake          ",font=('times of roman',15), variable=var17).place(x=500,y=500)
      var18 = IntVar()         
      Checkbutton(newWindow, text="Rasgulla                             ",font=('times of roman',15), variable=var18).place(x=500,y=530)
      var19 = IntVar()
      Checkbutton(newWindow, text="Jalebi                                ",font=('times of roman',15), variable=var19).place(x=500,y=560)
      var20 = IntVar()
      Checkbutton(newWindow, text="Curd                                 ",font=('times of roman',15), variable=var20).place(x=500,y=590)


       #--------line-----------
      canvas=Canvas(newWindow)
      canvas.place(x=0,y=170,width=1366,height=5)

      #--------Entry------------
      Entry4=Entry(newWindow,font=('times of roman',15))
      Entry4.place(x=250,y=73) 
      Entry5=Entry(newWindow,font=('times of roman',15))
      Entry5.place(x=250,y=123)
      Entry6=Entry(newWindow,font=('times of roman',15))
      Entry6.place(x=710,y=73) 
      Entry7=Entry(newWindow,font=('times of roman',15))
      Entry7.place(x=710,y=123)

      #-----------Button-----------
      Done=Button(newWindow,text='Done',command=details).place(x=200,y=680)
      Read=Button(newWindow,text='Read',command=Read).place(x=250,y=680)
      #------image-------------
      Image = PhotoImage(file = "E://Image//naan2.gif")
      label=Label(newWindow, image=Image)
      label.image = Image
      label.place(x=230,y=250,width=230,height=155)
      Image2 = PhotoImage(file = "E://Image//Dal2.gif")
      label2=Label(newWindow, image=Image2)
      label2.image = Image2
      label2.place(x=740,y=250,width=230,height=155)
      Image3 = PhotoImage(file = "E://Image//cake2.gif")
      label3=Label(newWindow, image=Image3)
      label3.image = Image3
      label3.place(x=230,y=470,width=230,height=155)
      Image4 = PhotoImage(file = "E://Image//drink.gif")
      label4=Label(newWindow, image=Image4)
      label4.image = Image4
      label4.place(x=740,y=470,width=230,height=155)

   
   app=Label(Window,bg='grey')
   app.place(x=90,y=20,width=200,height=400)
   #---
   Hotel2=Button(Window,bg='grey',image=photo,command=login_interface)
   Hotel2.place(x=100,y=40,width=40,height=40)
   #---

   calculator2=Button(Window,bg='grey',image=photo1,command=calculator)
   calculator2.place(x=100,y=100,width=40,height=40)
   #---
 
   tic_tak_toe2=Button(Window,bg='grey',image=photo2,command=tic_tak_toe)
   tic_tak_toe2.place(x=100,y=160,width=40,height=40)
   #---
   clock=Button(Window,bg='grey',image=photo4,command=clock)
   clock.place(x=100,y=220,width=40,height=40)
   #---
   KAsistant1=Button(Window,bg='grey',image=photo5,command=KAsistant,relief=FLAT)
   KAsistant1.place(x=100,y=280,width=40,height=40)
   #---
   wikipedia1=Button(Window,bg='grey',image=photo6,command=wikipedia,relief=FLAT)
   wikipedia1.place(x=100,y=340,width=40,height=40)
#-------wikipedia--------------------
def wikipedia():
   def get():
      a=entryk.get()
   def result():
      get()
      answer1 = wikipedia.summary(a)
      label1 = Label(window1,fg='white',text=answer1, font='times 15 bold')
      label1.place(x=0,y=250)
      
   kwikipedia=Toplevel(top)
   kwikipedia.geometry('1366x768')
   window1 = Toplevel(kwikipedia)
   window1.geometry("1366x768")
   r=sr.Recognizer()
   Image = PhotoImage(file = "E://Image//wiki.png")
   label=Label(kwikipedia, image=Image)
   label.image = Image
   label.place(x=0,y=0)
   entryk = Entry(kwikipedia,bg="white")
   entryk.place(width=450,height=55,x=425,y=551)
   button= Button(kwikipedia,image=P1,relief=FLAT,command=result)
   button.place(x=875,y=550,width=65,height=55)     
#--------------------------KAsistant-----------------------------------------------
def KAsistant():
   window = Toplevel(top)
   window.geometry("700x600")
   r=sr.Recognizer()
   with sr.Microphone() as source:
      audio = r.listen(source)
      try:
            text1 = r.recognize_google(audio)
            if text1 == "stop":
               label4=Label(KAsistant,text='OK')
               label4.pack()
            else:
               try:
                     app_id = "5R9TL5-TR9PUHAHW7"
                     client = wolframalpha.Client(app_id)
                     res = client.query(text1)
                     answer = next(res.results).text
                     label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')
                     label1.pack()
      	    
               except Exception as e:
                     answer1 = wikipedia.summary(text1)
                     label1 = Label(window, justify=LEFT, compound=CENTER, text=answer, font='times 15 bold')
                     label1.pack()
      except Exception as e:
            labeld=Label(window,text='again')
            labeld.pack()
#-------------------------tic_tak_toe-----------------------------------------------------------
def tic_tak_toe():
   def button(frame):          
       b=Button(frame,bg="papaya whip",text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
       return b
   def change_a():             
       nonlocal a
       for i in ['O','X']:
           if i!=a:
               a=i
               break
   def reset():               
       global a
       for i in range(3):
           for j in range(3):
                   b[i][j]["text"]=" "
                   b[i][j]["state"]=NORMAL
       a=r.choice(['O','X'])
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
   tic_tak_toe=Toplevel(top)
   tic_tak_toe.title('tic tak toe')
   tic_tak_toe.geometry('1366x768')
   tic_tak_toe.configure(bg='white')
   tic_tak_toe.resizable(0,0)

   #------------label--------------
   name=Label(tic_tak_toe,text='TIC TAK TOE',font=('fixedsys',50),bg='white',fg='black')
   name.place(x=400,y=30) 
   a=r.choice(['O','X'])       
   colour={'O':"deep sky blue",'X':"lawn green"}
   b=[[],[],[]]
   for i in range(3):
         for j in range(3):
               b[i].append(button(tic_tak_toe))
               b[i][j].config(command= lambda row=i,col=j:click(row,col))
   for i in range(3):
       b[0][i].place(x=250*(i+1),y=160,width=250,height=160)
   for i in range(3):
       b[1][i].place(x=250*(i+1),y=320,width=250,height=160)
   for i in range(3):
       b[2][i].place(x=250*(i+1),y=480,width=250,height=160)

   #----------frame---------------
   canvas=Canvas(tic_tak_toe,bg='black')
   canvas.place(x=500,y=160,width=15,height=480)
   canvas1=Canvas(tic_tak_toe,bg='black')
   canvas1.place(x=750,y=160,width=15,height=480)
   canvas2=Canvas(tic_tak_toe,bg='black')
   canvas2.place(x=250,y=320,width=750,height=15)
   canvas3=Canvas(tic_tak_toe,bg='black')
   canvas3.place(x=250,y=480,width=750,height=15)
   tic_tak_toe.mainloop()
#------------------------calculator---abel.place(x=230,y=250,width=230,height=155)abel.place(x=230,y=250,width=230,height=155)-----------------------------------------------------
def calculator():
   def btnClick(numbers):
      nonlocal operator
      operator=operator + str(numbers)
      text_Input.set(operator)

   def btnClearDisplay():
      nonlocal operator
      operator=""
      text_Input.set("")
   def btnEqualsInput():
      nonlocal operator
      sumup=str(eval(operator))
      text_Input.set(sumup)
      operator=""

   cal = Toplevel(top)
   cal.title("calculator")
   operator=""
   text_Input =StringVar()

   txtDisplay = Entry(cal,font=('arial',20,'bold'),
                      textvariable=text_Input, bd=30,insertwidth=4,
                      bg="light blue",justify='right').grid(columnspan=4)


   btn7=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="7",command=lambda:btnClick(7)).grid(row=1,column=0)

   btn8=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="8",command=lambda:btnClick(8)).grid(row=1,column=1)

   btn9=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="9",command=lambda:btnClick(9)).grid(row=1,column=2)

   Addition=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="+",command=lambda:btnClick("+")).grid(row=1,column=3)
   #=============================================================================================================
   btn4=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="4",command=lambda:btnClick(4)).grid(row=2,column=0)

   btn5=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="5",command=lambda:btnClick(5)).grid(row=2,column=1)

   btn6=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
   
   subtraction=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="-",command=lambda:btnClick("-")).grid(row=2,column=3)
   #===================================================================================================================
   btn1=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="1",command=lambda:btnClick(1)).grid(row=3,column=0)

   btn2=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="2",command=lambda:btnClick(2)).grid(row=3,column=1)

   btn3=Button(cal,padx=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
   
   multiply=Button(cal,padx=16,bg="light blue",bd=8,fg="black",font=('are-ial',20,'bold'),
               text="*",command=lambda:btnClick("*")).grid(row=3,column=3)
   #=====================================================================================================
   btn0=Button(cal,padx=16,pady=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="0",command=lambda:btnClick(0)).grid(row=4,column=0)

   btnClear=Button(cal,padx=16,pady=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="C",command= btnClearDisplay).grid(row=4,column=1)
   
   btnequal=Button(cal,padx=16,pady=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="=",command=btnEqualsInput).grid(row=4,column=2)

   division=Button(cal,padx=16,pady=16,bd=8,bg="light blue",fg="black",font=('are-ial',20,'bold'),
               text="/",command=lambda:btnClick("/")).grid(row=4,column=3)

#-----------------------login_interface---------------------------------------------------------------      
def login_interface():
   def message():
      a=Entry1.get()
      b=Entry2.get()
      if a=='':
         messagebox.showerror("Error", "ENTER USERNAME")
      elif b=='':
         messagebox.showerror("Error", "ENTER PASSWORD")
      elif a=='k':
         if b=='r':
            new_window()
         else:
            messagebox.showerror("Error", "WRONG PASSWORD")
      else:
         messagebox.showerror("Error","NO SUCH USER")
   login_interface=Toplevel(top)
   login_interface.geometry('280x330')
   login_interface.title('login')
   login_interface.configure(bg='black')
   login_interface.Login_Here=Label(login_interface,text='Login Here',bg='black',fg='white',font=('times new roman',30,)).place(x=50,y=20)
   Username=Label(login_interface,text='Username',bg='black',fg='white',font=('times new roman',20,)).place(x=30,y=100)
   Password=Label(login_interface,text='Password',bg='black',fg='white',font=('times new roman',20,)).place(x=30,y=170)
   Entry1=Entry(login_interface,font=('times of roman',15)) 
   Entry1.place(x=30,y=140,width=200,height=20)
   Entry2=Entry(login_interface,font=('times of roman',15))
   Entry2.place(x=30,y=210,width=200,height=20)

   Login_button=Button(login_interface,text='LOGIN',command=message).place(x=30,y=260)
#--------------------------clock------------------------------------------------------
def clock():
   clock=Toplevel(top)
   clock.geometry('600x300')
   clock.configure(bg='black')
   clock.resizable(0,0)
   text=time.strftime('%H: %M')
   label=Label(clock,text=text,font=('arial',100,'bold'),bg='black',fg='lawn green')
   label.place(x=100,y=60)
   localtime=time.asctime(time.localtime(time.time()))
   label2=Label(clock,text=localtime,font=('arial',20,'bold'),bg='black',fg='lawn green')
   label2.place(x=30,y=220)
#-------------------------new_window-------------------------------------------------------------------

def new_window():
   def bill1():
      
      e=var1.get()
      f=var2.get()
      g=var3.get()
      h=var4.get()
      i=var5.get()
      j=var6.get()
      k=var7.get()
      l=var8.get()
      m=var9.get()
      n=var10.get()
      o=var11.get()
      p=var12.get()
      q=var13.get()
      r=var14.get()
      s=var15.get()
      t=var16.get()
      u=var17.get()
      v=var18.get()
      w=var19.get()
      x=var20.get()
     
      #------------------DAtA--------BichAra------
      if e==1:
         A=('Paratha')
      if f==1:
         B=('Roti')
      if g==1:
         C=('Naan')
      if h==1:
         D=('Butter Naan')
      if i==1:
         E=('Methi Roti')
      if j==1:
         F=('Chicken Tandoori')
      if k==1:
         G=('Chicken Tandoori kabab')
      if l==1:
         H=('Butter Paneer')
      if m==1:
         I=('Mix Veg')
      if n==1:
         J=('Dal Makhani')
      if o==1:
         K=('Mineral Water')
      if p==1:
         L=('Coke')
      if q==1:
         M=('Tea')
      if r==1:
         M=('Sweet Lassi')
      if s==1:
         O=('Coffee')
      if t==1:
         P=('Ice cream')
      if u==1:
         Q=('Choco lava Cake')
      if v==1:
         R=('Rasgulla')
      if w==1:
         S=('Jalebi')
      if x==1:
         T=('Curd')
      else:
         hello=1
   def bill():
      a=Entry4.get()
      b=Entry5.get()
      c=Entry6.get()
      d=Entry7.get()
      #-----------------mysql--bill--------
      mydb = mysql.connector.connect(host="localhost",user="root",password="kanishk",database='kanishk')
      cur = mydb.cursor()
      i= "INSERT INTO bills (Sno,_Name,Phone_No,Amount) VALUES (%s, %s, %s, %s)"
      da= (c,a,b,d)
      cur.execute(i,da)
      mydb.commit()
   def print_bill():
      print("helo")
      
   def details():
      a=Entry4.get()
      b=Entry5.get()
      c=Entry6.get()
      d=Entry7.get()
      f=open("school.txt" ,"a")
      f.write(c)
      f.write('\t')
      f.write(d)
      f.write('\t')
      f.write(a)
      f.write('\t')
      f.write(b)
      f.write('\n')
   def Read():
      Read=Toplevel(top)
      Read.title('Details')
      Read.geometry('1366x768')
      Read.configure(bg='black')
      f=open("school.txt" ,"r")
      read=f.read()
      label=Label(Read,text=read,bg='black',fg='white',font=('times new roman',25))
      label.place(x=10,y=20)
   

   newWindow=Toplevel(top)
   newWindow.title('Hotel Management')
   newWindow.geometry('1366x768')
   newWindow.configure(bg='black')
   #--------label-----
   name=Label(newWindow,text='Name',bg='black',fg='white',font=('times new roman',25)).place(x=50,y=70)
   PhoneNo=Label(newWindow,text='Phone number',bg='black',fg='white',font=('times new roman',25,)).place(x=20,y=120)
   Hotel=Label(newWindow,text='PARADISE',bg='black',fg='white',font=('times new roman',30,)).place(x=455,y=10)
   OrderNo=Label(newWindow,text='Order number',bg='black',fg='white',font=('times new roman',25,)).place(x=500,y=70)
   Date=Label(newWindow,text='Amount',bg='black',fg='white',font=('times new roman',25,)).place(x=500,y=120)
   Roti=Label(newWindow,text='           Roti       ',bg='white',fg='black',font=('times new roman',25,)).place(x=20,y=200)
   Naan=Label(newWindow,text='         Naan        ',bg='black',fg='white',font=('times new roman',25,)).place(x=250,y=200)
   Nonveg=Label(newWindow,text='           Non Veg       ',bg='white',fg='black',font=('times new roman',25,)).place(x=500,y=200)
   Veg=Label(newWindow,text='         Veg        ',bg='black',fg='white',font=('times new roman',25,)).place(x=740,y=200)
   Ice=Label(newWindow,text='           Ice         ',bg='white',fg='black',font=('times new roman',25,)).place(x=20,y=420)
   Cream=Label(newWindow,text='         Cream        ',bg='black',fg='white',font=('times new roman',25,)).place(x=250,y=420)
   Drink=Label(newWindow,text='           Drink        ',bg='white',fg='black',font=('times new roman',25,)).place(x=500,y=420)
   Beverages=Label(newWindow,text='         Beverages        ',bg='black',fg='white',font=('times new roman',25,)).place(x=740,y=420)

   
   #--------checkbox---------
   var1 = IntVar()
   Checkbutton(newWindow, text="Paratha                    ",font=('times of roman',15), variable=var1).place(x=20,y=250)
   var2 = IntVar()  
   Checkbutton(newWindow, text="Roti                        ",font=('times of roman',15), variable=var2).place(x=20,y=280)
   var3 = IntVar()         
   Checkbutton(newWindow, text="Naan                       ",font=('times of roman',15), variable=var3).place(x=20,y=310)
   var4 = IntVar()
   Checkbutton(newWindow, text="Butter Naan             ",font=('times of roman',15), variable=var4).place(x=20,y=340)
   var5 = IntVar()
   Checkbutton(newWindow, text="Methi Roti               ",font=('times of roman',15), variable=var5).place(x=20,y=370)
   var6 = IntVar()
   Checkbutton(newWindow, text="Chicken Tandoori              ",font=('times of roman',15), variable=var6).place(x=500,y=250)
   var7 = IntVar()  
   Checkbutton(newWindow, text="Chicken Tandoori kabab       ",font=('times of roman',15), variable=var7).place(x=500,y=280)
   var8 = IntVar()         
   Checkbutton(newWindow, text="Butter Paneer                       ",font=('times of roman',15), variable=var8).place(x=500,y=310)
   var9 = IntVar()
   Checkbutton(newWindow, text="Mix Veg                                ",font=('times of roman',15), variable=var9).place(x=500,y=340)
   var10 = IntVar()
   Checkbutton(newWindow, text="Dal Makhani                         ",font=('times of roman',15), variable=var10).place(x=500,y=370)
   var11 = IntVar()
   Checkbutton(newWindow, text="Mineral Water                   ",font=('times of roman',15), variable=var11).place(x=20,y=470)
   var12 = IntVar()  
   Checkbutton(newWindow, text="Coke                        ",font=('times of roman',15), variable=var12).place(x=20,y=500)
   var13 = IntVar()         
   Checkbutton(newWindow, text="Tea                          ",font=('times of roman',15), variable=var13).place(x=20,y=530)
   var14 = IntVar()
   Checkbutton(newWindow, text="Sweet Lassi            ",font=('times of roman',15), variable=var14).place(x=20,y=560)
   var15 = IntVar()
   Checkbutton(newWindow, text="Coffee                       ",font=('times of roman',15), variable=var15).place(x=20,y=590)
   var16 = IntVar()
   Checkbutton(newWindow, text="Ice cream                      ",font=('times of roman',15), variable=var16).place(x=500,y=470)
   var17 = IntVar()   
   Checkbutton(newWindow, text="Choco lava Cake          ",font=('times of roman',15), variable=var17).place(x=500,y=500)
   var18 = IntVar()         
   Checkbutton(newWindow, text="Rasgulla                             ",font=('times of roman',15), variable=var18).place(x=500,y=530)
   var19 = IntVar()
   Checkbutton(newWindow, text="Jalebi                                ",font=('times of roman',15), variable=var19).place(x=500,y=560)
   var20 = IntVar()
   Checkbutton(newWindow, text="Curd                                 ",font=('times of roman',15), variable=var20).place(x=500,y=590)


    #--------line-----------
   canvas=Canvas(newWindow)
   canvas.place(x=0,y=170,width=1000,height=5)
   canvas1=Canvas(newWindow)
   canvas1.place(x=1000,y=0,width=5,height=768)
   #--------Entry------------
   Entry4=Entry(newWindow,font=('times of roman',15))
   Entry4.place(x=250,y=73) 
   Entry5=Entry(newWindow,font=('times of roman',15))
   Entry5.place(x=250,y=123)
   Entry6=Entry(newWindow,font=('times of roman',15))
   Entry6.place(x=710,y=73) 
   Entry7=Entry(newWindow,font=('times of roman',15))
   Entry7.place(x=710,y=123)

   #-----------Button-----------
   Done=Button(newWindow,text='Done',command=details).place(x=1200,y=680)
   Read=Button(newWindow,text='Read',command=Read).place(x=1150,y=680)
   Bill=Button(newWindow,text='Bill',command=bill).place(x=1100,y=680)
   #------image-------------
   Image = PhotoImage(file = "E://Image//naan2.gif")
   label=Label(newWindow, image=Image)
   label.image = Image
   label.place(x=230,y=250,width=230,height=155)
   Image2 = PhotoImage(file = "E://Image//Dal2.gif")
   label2=Label(newWindow, image=Image2)
   label2.image = Image2
   label2.place(x=740,y=250,width=230,height=155)
   Image3 = PhotoImage(file = "E://Image//cake2.gif")
   label3=Label(newWindow, image=Image3)
   label3.image = Image3
   label3.place(x=230,y=470,width=230,height=155)
   Image4 = PhotoImage(file = "E://Image//drink.gif")
   label4=Label(newWindow, image=Image4)
   label4.image = Image4
   label4.place(x=740,y=470,width=230,height=155)
   
   
#-----------------------main------------------------------------------
top = Tk()
top.title('Main screen')
top.geometry('1366x768')
top
Image = PhotoImage(file = "E://Image//wallpaper.gif")
label=Label(top, image=Image)
label.image = Image
label.place(x=0, y=0, relwidth=1, relheight=1)
label1=Label(top,bg='black').place(x=0,y=0,width=100,height=768)
label2=Label(top,bg='black').place(x=1266,y=0,width=100,height=768) 
#------------hopbar-----
hopbar=Label(top,bg='grey')
hopbar.place(x=455,y=600,width=450,height=60)
#-------hotel-----
photo = PhotoImage(file = "E://Image//hotel3.png")
Hotel=Button(top,bg='grey',image=photo,command=login_interface,relief=FLAT)
Hotel.place(x=470,y=610,width=40,height=40)

#-------calculator--
photo1 = PhotoImage(file = "E://Image//calculator3.png")
calculator=Button(top,bg='grey',image=photo1,command=calculator,relief=FLAT)
calculator.place(x=520,y=610,width=40,height=40)

#-------tic_tak_toe---
photo2 = PhotoImage(file = "E://Image//tic tak toe 3.png")
tic_tak_toe=Button(top,bg='grey',image=photo2,command=tic_tak_toe,relief=FLAT)
tic_tak_toe.place(x=570,y=610,width=40,height=40)

#-------Clock-----
photo4= PhotoImage(file = "E://Image//clock3.png")
clock=Button(top,bg='grey',image=photo4,command=clock,relief=FLAT)
clock.place(x=620,y=610,width=40,height=40)
#-------APP drawer---
P1= PhotoImage(file = "E://Image//search1.png")
photo7= PhotoImage(file = "E://Image//app_drawer.png")
clock=Button(top,bg='grey',image=photo7,command=window,relief=FLAT)
clock.place(x=770,y=610,width=40,height=40)
#-------KASistant-------
photo5= PhotoImage(file = "E://Image//asistant2.png")
KAsistant=Button(top,bg='grey',image=photo5,command=KAsistant,relief=FLAT)
KAsistant.place(x=670,y=610,width=40,height=40)
#-------Wikipedia--------
photo6= PhotoImage(file = "E://Image//wikipedia 1.png")
wikipedia=Button(top,bg='grey',image=photo6,command=wikipedia,relief=FLAT)
wikipedia.place(x=720,y=610,width=40,height=40)
top.mainloop()