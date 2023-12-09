import serial  # Se comunica con el Arduino
import pygame  # Leera el teclado cuando se pulse

ser = serial.Serial('COM6', 9600)  # Comunicacion con el puerto COM8, debes cambiarlo por el tuyo.

pygame.init()  # Inicia pygame
screen = pygame.display.set_mode((640, 480))  # Paremtros para dibujar una ventana
pygame.display.set_caption('Robot!')
pygame.mouse.set_visible(1)

val = '-'

while val != 'stop':
    # Si se presiona alguna flecha se enviara un caracter por el puerto al que se conecte el Arduino
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ser.write(str("a").encode())
            elif event.key == pygame.K_LEFT:
                ser.write(str('s').encode())
            elif event.key == pygame.K_RIGHT:
                ser.write(str('i').encode())
            elif event.key == pygame.K_DOWN:
                ser.write(str('r').encode())
            elif event.key == pygame.K_ESCAPE:
                val = 'stop'
        if event.type == pygame.KEYUP:  # Si se deja de presionar una tecla envia la instrucción de parada por Serial.
            ser.write(str('d').encode())