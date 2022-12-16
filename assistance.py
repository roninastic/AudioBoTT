import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
 #print(voices[0].id):
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Well come!!!! to the new AI system Known to be Friday")
speak("Well come!!!! to the new AI system Known to be Friday")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    if hour>=12 and hour<=18:
        speak("Good Afternoon!")   

    if hour > 18:
        speak("Good Evening!")  

    speak("I am Friday Sir. Please tell me , How may I help you ? ")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pannasanjaypatel8173@gmail.com', 'hetvaidik17')
    server.sendmail('pannasanjaypatel8173@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=95)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        if 'open google' in query:
            webbrowser.open("google.com")

        if 'open facebook' in query:
            webbrowser.open("facebook.com")   
        
        if 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        
        if 'who are you' in query:
            speak("I am friday! ,creaction of Mr het patel And version 1.2")
            print("I am friday! ,creaction of Mr Het patel And version 1.2")
        


        if 'play music' in query:
            music_dir = 'F:\\REAL MUSIC\\Bollywood music\\audio'
            songs = os.listdir(music_dir)   
            os.startfile(os.path.join(music_dir, songs[0]))
        
        if 'play  bollywood movie' in query:
            music_dir = 'E:\\Bollywood\\Hindi movies'
            songs = os.listdir(music_dir)   
            os.startfile(os.path.join(music_dir, songs[10]))

        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        if 'open code' in query:
            codePath = "C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        if 'open chrome' in query:
            codePath = "C:\\Users\\abc\\AppData\\Local\\Google\\Chrome\\Application\\chrome"
            os.startfile(codePath)
        
        if 'hello ' in query:
            print("Hello sir")
            speak("Hello sir")

        

        if 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "het15018173@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend het. I am not able to send this email") 
    while False:
        speak('sorry sir the is beyond my limit  ')
    
        

    
        
        
        
        

 
