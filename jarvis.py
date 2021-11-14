from playsound import playsound
from gtts import gTTS
import speech_recognition as sr

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan : Anlamadım Lütfen Tekrar Dene")
        except sr.RequestError:
            print("Asistan : Sistem Kullanılamıyor")
        return voice
voice = record()

def speak(string):
    tts = gTTS(text = string, lang= "tr")
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
speak(voice)

if voice != "":
    print(voice)
