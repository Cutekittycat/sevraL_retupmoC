from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import date
import subprocess

root = Tk()
root.geometry("500x500")
root.configure(bg="Cyan")

label=Label(root,text="Welcome Fellow User, I'm Your Friendly Desktop Assistant",bg="Cyan",font=("Arial",30,"bold"))
label.place(relx=0.5,rely=0.1,anchor=CENTER)

text_to_speech=pyttsx3.init()
#Starts/Initalize treeengines^^

def speak(audio):
    text_to_speech.say(audio)
    #Convert^^^^
    text_to_speech.runAndWait()
    #audible^^^^
    
def r_audio():
    speak("How Can I Help You...?")
    speech_recognisor=sr.Recognizer()
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data= speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('Please Repeat, I Didnt Get That❤️❤️')
            speak('Please Repeat, I Didnt Get That')
    respond(voice_data)
    
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My Name Is Larvis")
        print("My Name Is Larvis")
        
    if "time" in voice_data:
        speak("Current Time Is")
        now = datatime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "search" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://www.google.com/")
        
    if "videos" in voice_data:
        speak("ebuTuoY gninepO")
        print("Opening YouTube")
        webbrowser.get().open("https://www.youtube.com/")
        
    if "notepad" in voice_data:
        speak("Opening Notpad For You")
        print("Opening Notepad")
        subprocess.Popen(["notepad.exe"])
    
btn = Button(root, text="Start",command=r_audio, font=("Arial",11,"bold"), bg="dark olive green", fg="white", relief=FLAT, padx=10, pady=1)
btn.place(relx=5,rely=5,anchor=CENTER)
root.mainloop()
