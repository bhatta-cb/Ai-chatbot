from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer
from tkinter import *

import pyttsx3 as pp #library for voice from bot

engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("Phone Specification")

convo = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "Who created you?",
    "Im created by Chirag..",
    "What are the different models of phone?",
    "Samsung Apple Google One Plus"
]


trainer = ListTrainer(bot)

trainer.train(convo)

# answer = bot.get_response("What are the different models of phone?")
# print(answer)

# print("You can communicate with the bot now")
#
# while True:
#     query=input();
#     if query== 'exit':
#         break
#     answer=bot.get_response(query)
#     print("Bot : ",answer)


main = Tk()
main.geometry("550x600")
main.title("Phone Specification")

img= PhotoImage(file="bot.png")
photol = Label(main, image=img)

photol.pack(pady=5)

def ask_from_bot():
    query= textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)  #to show the last message either from bot or you without scrolling

frame=Frame(main)
sc=Scrollbar(frame)

msgs= Listbox(frame,width=80,height=15,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

#creation of field to put questions

textF= Entry(main, font=("Times", 20, "bold italic"))
textF.pack(fill=X,pady=10)

#creating button
btn = Button(main, text="Ask?",font=("Times", 20, "bold italic"),command=ask_from_bot)
btn.pack()

#when we press enter to ask bot
def enter_function(event):
    btn.invoke()

main.bind('<Return>', enter_function)


main.mainloop()


