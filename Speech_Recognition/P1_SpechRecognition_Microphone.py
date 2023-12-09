#pip install pyaudio
#pip install speechRecognition

import pyaudio
import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source:
    print("inicia: ")
    audio = r.listen(source)
    print("Registro generado!")
    try:
        print("Mensaje: " + r.recognize_google(audio, language="es-MX")) #personaLized
    except sr.UnknownValueError:
        print("Uknown Value Error")
    except sr.RequestError as e:
        print(e)
        print("Request Error: ".format(e))
