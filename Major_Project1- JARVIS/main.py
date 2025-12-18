# #  JARVIS - VOICE-ACTIVATED VIRTUAL ASSISTANT 

import speech_recognition as sr             # used to convert speech to text
import webbrowser                           # Interfaces for launching and remotely controlling the webbrowser
import win32com.client                      # Windows built-in text-to-speech library
import musicLibrary
import requests
from groq import Groq
import config  # Import your config file
import os

# Now creating the objecs

recognizer = sr.Recognizer()                # Speech recognizer object (recognizes the speech)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
newsApi = "6ca8369b92df4aa7acf59f0a6233bd00"

def speak(text):
    print(f"Speaking: {text}")
    speaker.Speak(text)

# function for giving the commands and get the response from the AI

def ai_process(command):
    client = Groq(api_key=config.GROQ_API_KEY)
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Groq's fast model
        messages=[
            {
                "role": "system", 
                "content": "You are Jarvis, a virtual assistant skilled in general tasks like Alexa and Google Cloud. Give brief, helpful responses."
            },
            {
                "role": "user", 
                "content": command
            }
        ],
        temperature=0.7,
        max_tokens=100
    )
    
    return completion.choices[0].message.content

def processCommand(c):

    # functionality for opening the different platforms, can add more 
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    # Open Local Apps (Calculator, Notepad, VS Code), can add more
    elif "open calculator" in c.lower():
        speak("opening calculator")
        os.system("calc")
    elif "open vscode" in c.lower():
        speak("opening vscode")
        os.system("code")
    elif "open file explorer" in c.lower():
        speak("opening file explporer")
        os.system("explorer")
    elif "open whatsapp" in c.lower():
        speak("opening whatsapp")
        os.system("whatsapp")
    # Weather (Simple – browser based)
    elif "weather" in c.lower():
        webbrowser.open("https://www.google.com/search?q=weather")

    

    # functionality for playing the musics, can add more
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    # functionality for getting the news
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApi}")
        if r.status_code == 200:
            # parse the json response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles[:5]:
                speak(article['title'])
    else:
        # let AI handle the request
        
        output = ai_process(c)
        speak(output) 

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:

        # Listen for the wake word "Jarvis"

        # obtain the audio from the microphone 

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            
            print("Recognizing...")
            word = recognizer.recognize_google(audio)
            print(f"Heard: '{word}'")
            
            if "jarvis" in word.lower():
                speak("Ya")
                
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source)
                
                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)

        except sr.WaitTimeoutError:
            continue
        except Exception as e:
            print(f"Error: {e}")


