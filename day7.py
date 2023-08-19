import speech_recognition as sr
import datetime

popo="reminder.txt"

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')      
engine.setProperty('voice', voices[1].id)  

def speak(speak_text):
    engine.say(speak_text)
    engine.runAndWait()

tips=("'say set a reminder' to set a reminder and\n  say 'what is my reminder' to listen your reminder")
print(tips)
speak(tips)

def reminders():
    r=sr.Recognizer()
    with sr.Microphone(1) as micro:
        date=datetime.datetime.now()
        date_formate=date.strftime(" %Y %B %d")
        print("i am lestening your  reminder...")
        try:
            mic=r.listen(micro)
            print('reconizing your reminder ...(wait)')
            voice_text=r.recognize_google(mic)
            print(f'your reminder:{voice_text}')
            return_value= f'{date_formate} {voice_text}'
            return return_value
        except:
            return None

def take_command()-> str:
    r=sr.Recognizer()
    with sr.Microphone(1) as micro:
        print("listening...")
        mic=r.listen(micro)
        try:
            print('reconizing your sound...')
            voice_text=r.recognize_google(mic)
            print(f'you:{voice_text}')
            return voice_text.lower()
        except:
            print("your voice is not reconizing...(try to speak in english)")
            return ''

while True:
    voice_command=take_command()
    if "set" in voice_command and "reminder" in voice_command:
        speak('ok tell me what you want me to remind')
        p=str(reminders())
        if p==None:
            speak('unable to recoinze reminder, try again')
        else:
            with open(popo,"a") as f:
                f.write(p)
            speak('your reminder has been set')
            
    if "what" in voice_command and "reminder" in voice_command:    
     print("thi i orking")
     dear=datetime.datetime.now()
     date_formate=dear.strftime("%Y %B %d ")
     with open('reminder.txt','r') as p:
        o=p.readlines()
     for i in o:
        splitted=i.split(' ')
        m=date_formate.split(' ')
        lol=(m[0:3])        
        if splitted[1:4]==lol:
            k=' '.join(splitted[4::])
            print(k)
            speak(k)
  
    elif voice_command=='quite' or voice_command=='quit':
        speak('ok quiting ')
        break