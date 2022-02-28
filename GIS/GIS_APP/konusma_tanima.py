
import speech_recognition as sr
import pyttsx3

def kayit():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        print("Şuan sizi dinliyorum.(5 saniye boyunca..)")
        audio_data = r.record(source,duration=5)  
        text = str(r.recognize_google(audio_data,language="tr-TR"))
        b = []
        b.append(text)
        
        print(b)
kayit()
