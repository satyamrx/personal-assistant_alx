from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from tkinter.ttk import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import wikipedia
import webbrowser
import time
import os
import requests
from bs4 import BeautifulSoup
from platform import *



engine = pp.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()


mybot = ChatBot("alx")


# print("Talk to alx ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = mybot.get_response(query)
#     print("alx : ", answer)
main = Tk()

main.geometry("400x700")

main.title("alx")
photo = PhotoImage(file ="r.gif") 
 
photoL = Label(main, image=photo)
photoL.pack(pady=10)

#taking speech and convert into query


def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Alx is listening try to speak")
    with s.Microphone() as m:
        audio = sr.listen(m)
        

        try:
            query = sr.recognize_google(audio)
            print(query)
            textf.delete(0, END)
            textf.insert(0, query)


        # or: return recognizer.recognize_google(audio)
        except s.UnknownValueError:

            print("sorry sir i do not understand")


        except s.RequestError as e:

            print("not understand sir")
        except s.WaitTimeoutError:
            speak("soryy sir it seems to be good if i am shutdown")
    
        ask_from_alx()
# corona virus update link
def getdata(url):
    r=requests.get(url)
    return r.text




def ask_from_alx():
    query=textf.get().lower()
    if "hello" in query or "hye" in query or "hay" in query:
        
        answer_from_alx="hye sir"
     #query for wiki,fb,youtube
    elif "wikipedia" in query:
        speak(" searching wikipedia sir please wait...")
        query=query.replace("wikipdeia","")
        answer_from_alx=wikipedia.summary(query,sentences=2)
        speak("according to wikipedia sir : ")
    elif "open youtube" in query:
        speak("opening youtube for you sir enjoy")
        webbrowser.open("https://www.youtube.com/")
        answer_from_alx="opening youtube..... please wait"

    elif "open facebook" in query:
        speak("sir I am opening facebook but please do not we lazy")
        webbrowser.open("https://www.facebook.com/")
        answer_from_alx="opening facebook..... please wait"

    elif "email" in query or "gmail" in query:
        speak("opening email for you sir")
        webbrowser.open("https://mail.google.com/")
        answer_from_alx="opening gmail..... please wait"
    elif "whatsapps" in query or "whatsapp" in query:
        answer_from_alx="opening whatapp sir please wait"
        webbrowser.open("https://web.whatsapp.com/")
       
    elif "how are you" in query:
        answer_from_alx="I am doing great these days sir"

    elif "time" in query:
        answer_from_alx = time.strftime("%H:%M:%S",time.localtime() )


    elif "shutdown" in query or "quit" in query:
        speak("ok sir, command for system shutdown")
        os._exit(1)
    elif "play music" in query or "song" in query:
        answer_from_alx="gaana.com is now ready for you, enjoy your music"
        webbrowser.open("https://gaana.com/")
    elif "thanku" in query or "thank" in query:
        answer_from_alx="its my pleasure sir to stay with you"
    elif "good morning" in query:
        answer_from_alx="Good morning sir, i think you might need some help"
    elif "good night" in query:
        answer_from_alx="A well-spent day brings happy sleep, good night sir "
    elif "live" in query or "where are you" in query:
        answer_from_alx="i am everywhere sir"
    elif "who invent you" in query or "who develop you" in query or "who is your father" in query:
        answer_from_alx="i am developed by satyam kumar"
    elif "can you do for me" in query:
        answer_from_alx="mostly i will able to do search wikipedia, youtube, google, send email, set remainder, news, play music, facebook, whatapps, and many more sir"
    elif "corona" in query or "covid" in query:
        speak(" getting infromation sir, please wait...")

        htmldata=getdata("https://www.mohfw.gov.in/")
        soup = BeautifulSoup(htmldata, 'html.parser')
        #print(soup.prettify())
        mydata_str=""
        for tr in soup.find_all('tbody')[0].find_all("tr"):
        #print(tr.get_text())
            mydata_str +=tr.get_text().lower()
        mydata_str=mydata_str[1:]
        item_list=mydata_str.split("\n\n")
        data_list=[]
        for item in item_list[37:41]:
            data_list.append(item.split("\n"))

        speak("Active Cases in india is "+data_list[0][2])
        speak("total Cured  in india is "+str(data_list[1]))
        speak("total Deaths in india is "+data_list[2][1])

        answer_from_alx="stay safe sir, total confirmed cases is "+data_list[3][1]
    elif "platform" in query:
        answer_from_alx=("you are currently working in "+ platform(0, 1))


    elif "processor" in query:
        answer_from_alx=("you are using " +processor() + " sir")

    elif "weather" in query:
        speak("getting weather information sir please wait")
        htmldata=getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")
        soup = BeautifulSoup(htmldata, 'html.parser')
        # print(soup.prettify())
        current_temp=soup.find_all("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
        chances_rain=soup.find_all("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
        temp=(str(current_temp))   
        temp_rain=str(chances_rain)
        answer_from_alx="current_temp "+temp[128:-9] +"  in patna bihar "+ temp_rain[131:-14]
    
    else:
        answer_from_alx="sorry sir i am still baby alx, I dont now that one, please pardon sir"

    msg.insert(END, "you : " + query )
    msg.insert(END, "Alx : " + str(answer_from_alx) )
    speak(answer_from_alx)


    textf.delete(0,END)
    msg.yview(END)


    
frame=Frame(main)
sc= Scrollbar(frame)
msg=Listbox(frame,width=70, height=10)

sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#text field

textf=Entry(main,font=("verdana",20))
textf.pack(fill=X,pady=10)

#button ask from alx

btn = Button(main, text="Ask from Alx", command=ask_from_alx)
btn.pack()
# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()


