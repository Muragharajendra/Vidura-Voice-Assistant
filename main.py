import speech_recognition as sr
import webbrowser
import requests
import pygame
import os
import google.generativeai as genai
import musicLibrary
from speech_engine import speak  # Updated to use edge-tts speak()

# Configure Gemini API
genai.configure(api_key="AIzaSyCUkveVkumefvziKzFx_TYdD1FlKOB0GDs")  # Replace with your Gemini key
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

recognizer = sr.Recognizer()
newsapi = "8b8f153572284645b9517cf3d970b868"

def aiProcess(command):
    try:
        response = model.generate_content(
            f"You are a voice assistant named Vidhura. Please give short, clear answers without any markdown or formatting. {command}",
            generation_config={
                "temperature": 0.3,
                "max_output_tokens": 100,
                "top_p": 1,
                "top_k": 10
            }
        )
        return response.text
    except Exception as e:
        print("AI Error:", e)
        return "Sorry, something went wrong."

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:3]:
                speak(article['title'])
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Vidhura....")
    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            word = recognizer.recognize_google(audio)
            if word.lower() in ["vidhura", "hey brother", "hey guru", "hai guru ","namaste vidhura","namaste vidura","vidura"]:
                if word.lower() in ["vidhura", "hey brother", "hey guru", "hai guru "]:
                    vc="How can I help you"
                else:
                    vc="namaste .. How can I help you"

                speak(vc)
                with sr.Microphone() as source:
                    print("Vidhura Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error:", e)
