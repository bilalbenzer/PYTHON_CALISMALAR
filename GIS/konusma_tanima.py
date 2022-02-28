import speech_recognition as sr
import pyttsx3


def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio,language="tr-TR")
                print(str(text1).capitalize())
            except:
                pass
            return text1
recordvoice()
