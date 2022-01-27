from tkinter import *
import mysql.connector
import wolframalpha
import wikipedia
import speech_recognition as sr
def KAsistant():
   KAsistant=Tk()
   KAsistant.title('Asistant')
   KAsistant.geometry('455x768')
   KAsistant.configure(bg='white')
   KAsistant.resizable(0,0)
   r=sr.Recognizer()
   with sr.Microphone() as source:
      audio = r.listen(source)
      labela=Label(KAsistant,text='Lestening....')
      labela.pack()
      try:
            text1 = r.recognize_google(audio)
            label3=Label(KAsistant,text='Regognizing....').pack()
            label5=Label(KAsistant,text=text1).pack()
            if text1 == "stop":
               label4=Label(KAsistant,text='OK')
               label4.pack()
            else:
               window = Tk()
               window.geometry("700x600")
      
               try:
                     labelc=Label(window,text='Searching...')
                     labelc.pack()
                     app_id = "5R9TL5-TR9PUHAHW7"
                     client = wolframalpha.Client(app_id)
                     res = client.query(text1)
                     answer = next(res.results).text
                     label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')
                     label1.pack()
      	    
               except Exception as e:
                     answer1 = wikipedia.summary(text1)
                     print(answer1)
                     label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer1, font='times 15 bold')
                     label1.pack()
      except Exception as e:
            labeld=Label(KAsistant,text='again')
            labeld.pack()
KAsistant()
