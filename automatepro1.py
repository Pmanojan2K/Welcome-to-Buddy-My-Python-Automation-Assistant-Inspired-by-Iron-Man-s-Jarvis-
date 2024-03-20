# Automation project like a simple jarvis 
# Libraries
import pyttsx3  # Text to speech
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # male voice

# Function to speak out the given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on time of the day
def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak('Good morning buddy')
    elif 12 <= hour < 18:
        speak('Good afternoon buddy')
    else:
        speak('Good evening buddy')
    speak('Hey dude, how can I help you buddy?')

# Function to take voice commands from the user
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing your voice....') 
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')
    except Exception as e:
        print('Say that again...')
        return ""

    return query.lower()

# Function to send email
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('mymail@gmail.com', 'passwordno')  # Enter your email credentials
        server.sendmail('mymail@gmail.com', to, content)
        server.close()
        speak('Your email has been sent successfully')
    except Exception as e:
        print(e)
        speak('I am unable to send the email. Please check the error')


if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand()

        if 'Open wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('open wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            speak(result)

        elif 'Open notepad' in query:
            os.system('start notepad.exe')

        elif 'Open word' in query:
            os.system('start WINWORD.EXE')

        elif 'Open youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'Open linkedin' in query:
            webbrowser.open('https://www.linkedin.com/')

        elif 'Open google' in query:
            webbrowser.open('https://www.google.com')

        elif 'Open github' in query:
            webbrowser.open('https://github.com/')

        elif 'Current time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'The current time is {strTime}')

        elif 'email to friend' in query:
            try:
                speak('What should I say?')
                content = takecommand()
                to = 'friend_email@gmail.com'  # Enter receiver email address
                sendEmail(to, content)
                speak('Your email has been sent successfully')
            except Exception as e:
                print(e)
                speak('I am unable to send the email. Please check the error')
