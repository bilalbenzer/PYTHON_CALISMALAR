import speech_recognition
import pyttsx3
class kayit_olustur():

    def __init__(self,acik_kapali=None):
        if acik_kapali == "Açık":
            self.ses_tanima_acik_kapali = "Açık"
        else:
            self.ses_tanima_acik_kapali = "Kapalı"
        
    def kayit(self):
        if self.ses_tanima_acik_kapali =="Açık":
            with speech_recognition.Microphone() as source:
                self.r = speech_recognition.Recognizer()
                print("Şuan sizi dinliyorum.(5 saniye boyunca..)")
                self.audio_data = self.r.record(source,duration=5)
                self.text = str(self.r.recognize_google(self.audio_data,language="tr-TR")).lower()
        else:
            print("Sesli Tanıma Kapalı")
