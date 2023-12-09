import serial
import speech_recognition as sr
from pynput import keyboard

arduino = None
arduino = serial.Serial("COM7", baudrate=9600, timeout=1)

r = sr.Recognizer()

continuar = True


def peticion(cadena):
    cadena = cadena.lower()
    palabras = cadena.split()
    match palabras[0]:
        case 'arriba':
            return '0'
        case 'abajo':
            return '1'
        case 'izquierda':
            return '2'
        case 'derecha':
            return '3'
        case 'detente':
            return '4'
        case _:
            return ''
while continuar:
    audio = None
    accion = ''
    comando = ''
    print("Di lo que necesitas")

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) #Ajustar para eliminar ruido ambiente
        try:
            audio = r.listen(source, timeout=3)
        except sr.WaitTimeoutError:
            print("Tiempo e espera agotado. Intenta de nuevo")
            continuar
    try:
        comando = r.recognize_google(audio, language="es-MX")
        accion = peticion(comando)
        print('Enviado a Arduino:', accion)

        arduino.write(accion.encode())
        print('Comando enviado a Arduino')

    except sr.UnknownValueError:
        print("No se puedo enetender el comando")
    except sr.RequestError as e:
        print("Request Error: {}".format(e))
    except Exception as ex:
        print("Error: {}".format(ex))

arduino.close()