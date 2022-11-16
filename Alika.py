import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyautogui
import webbrowser

escuchar = sr.Recognizer()

inicializar = pyttsx3.init()
velocidad_de_voz = 130
inicializar.setProperty('rate', velocidad_de_voz)
nombre = "Alika"

def habla(texto):
    inicializar.say(texto)
    inicializar.runAndWait()

def tomar():
    try:    
        with sr.Microphone() as voz:
            print("Escuchando...")
            voice = escuchar.listen(voz)
            command = escuchar.recognize_google(voice)
            command = command.lower()
            if nombre in command:
                command = command.replace(nombre,"")
                print(command)
    except:
        pass
    return command

def Alika():
    command = tomar()
    if "reproduce" in command:
        cancion = command.replace("reproduce", '')
        habla("Reproduciendo a " + cancion)
        pywhatkit.playonyt(cancion)

    elif "hora" in command:
        time = datetime.now().strftime('%I:%M:%p')
        print(time)
        habla("Son las: " + time)

    elif "wikipedia" in command:
        busqueda = command.replace("wikipedia", '')
        informacion = wikipedia.set_lang("es")
        informacion = wikipedia.summary(busqueda, 1)
        print(informacion)
        habla(informacion)

    elif "pantalla" in command:
        screenshot = pyautogui.screencshot()
        screenshot.save ("Screenshot.png")
        habla("Capturando la pantalla...")

    elif "google" in command:
        google = webbrowser.open('http://google.com')
        print(google)
        habla("Abriendo " + google)
    

    else:
        habla("Recuerda decir mi nombre")


