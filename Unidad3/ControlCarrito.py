
import serial as s
#from pynput.keyboard import Controller, Key, Listener
from pynput import keyboard

arduino = None
arduino = s.Serial("COM7", baudrate=9600, timeout=1)

#keyboard = Controller()




def on_press(key):
    if key == keyboard.Key.up:
        print('up')
        arduino.write(str("2").encode())
    elif key == keyboard.Key.down:
        print('down')
        arduino.write(str("1").encode())
    elif key == keyboard.Key.left:
        print('left')
        arduino.write(str("3").encode())
    elif key == keyboard.Key.right:
        print('right')
        arduino.write(str("4").encode())

def on_release(key):
    if key == keyboard.Key.up:
        print('up')
        arduino.write(str("0").encode())
    elif key == keyboard.Key.down:
        print('down')
        arduino.write(str("0").encode())
    elif key == keyboard.Key.left:
        print('left')
        arduino.write(str("0").encode())
    elif key == keyboard.Key.right:
        print('right')
        arduino.write(str("0").encode())

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()