
import wolframalpha
import wikipedia
from tkinter import *
import speech_recognition as sr

while True:
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Listening.....")
		audio = r.listen(source)
		try:
                        print("Regognizing....")
			text = r.recognize_google(audio)
			print('You said: ' + text)
			if text == "stop":
				print("Program will exit.")
				break
			else:
				window = Tk()
				window.geometry("700x600")
				try:
					app_id = "5R9TL5-TR9PUHAHW7"
					client = wolframalpha.Client(app_id)
					res = client.query(text)
					answer = next(res.results).text
					print("Answer from Wolfram|Alpha:")
					print(answer)
					label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')
					label1.pack()
					window.after(5000, lambda: window.destroy())
					mainloop()
				except Exception as e:
					answer = wikipedia.summary(text)
					print("Answer from Wikipedia:")
					print(answer)
					label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer, font='times 15 bold')
					label1.pack()
					window.after(500000, lambda: window.destroy())
					mainloop()
		except Exception as e:
			print(e)
			answer = "Sorry we cannt hear you"
			print(answer)
