from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from tkinter import *
from PIL import Image, ImageTk

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

bot = ChatBot("My Bot")

convo=[
    "Hii" ,
    "Hey ! How can i help you",

    "hello",
    "Hey ! How can i help you",

    "hey",
    "Hey ! How can i help you",

    "what is the registration fee for the examination",
    "1000 rs for online and 1500 for off-line",

    "modes of examination",
    "online and offline for 3 hours"
    
    "examination pattern",
    "90 mcqs for 3 hrs of 360 marks",

    "syllabus of the examination",
    "complete syllabus of 11th and 12th physics chemistry and maths",

    "how to apply",
    "online as well as offline aslo",

    "how to apply online",
    "Go to freeservice.com   then select application form check the eligibility criteria",

    "What is the eligibility criteria for the examination",
    "you must have above 75% in 12th"
    "  OR  "
    "you are above 80 percentile of your respective board",

    "payment modes",
    "All type of online transactions Paytm  UPI  AmazonPay  PhonePe",

    "how to apply offline",
    "Nearby aplication centres. Go to official website freeservice.com and search the centre nearer to you",

    "bye",
    "Have a good day\n All the best"

]
trainer=ListTrainer(bot)
trainer.train(convo)

root=Tk()
root.title("My ChatBot")
root.geometry("520x650")

def ask_to_bot():
    query=textF.get()
    if str(query)=="Exit" or str(query)=="exit":
        msgs.delete(0,END)
        exit()
    ans = bot.get_response(str(query))
    x=str(ans)
    msgs.insert(END, "You : ",query)
    msgs.insert(END,"Bot : ",x)

image=Image.open("k.png")
photo=ImageTk.PhotoImage(image)
imagel=Label(root,image=photo)

frame=Frame(root)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80 ,height=20)

textF=Entry(root,font=("verdana",12))
btn=Button(root,text="AskToBot",font=("verdana",15),command=ask_to_bot)

sc.pack(side=RIGHT ,fill=Y )
msgs.pack(side=LEFT, fill=BOTH)

imagel.pack(pady=10)
frame.pack(pady=15)
textF.pack(fill=X,pady=10,padx=5)
btn.pack(pady=10)
root.mainloop()