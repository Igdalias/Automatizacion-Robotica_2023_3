import pygame, sys
from pygame.locals import *

# Inicializa pygame
pygame.init()
# Se crea la ventana definiendo el tamaño (Ancho, Alto)
ventana = pygame.display.set_mode((800, 600))
# Titulo de la ventana
pygame.display.set_caption('Carrito virtual')

# Se carga imagen del carrito
Car = pygame.image.load('Carrito.png')
Car = pygame.transform.scale(Car, (50, 45))
# Car = pygame.transform.rotate(Car, 90)
VelocidadCar = 3
direccion = True
CarPosX, CarPosY = 80, 60

fondo = 255, 255, 255
ventana.fill(fondo)
Color = pygame.Color(0, 0, 0)
pygame.draw.line(ventana, Color, (60, 80), (200, 80), 10)
pygame.draw.line(ventana, Color, (60, 76), (60, 500), 10)


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    ventana.blit(Car, (CarPosX, CarPosY))

    pygame.display.update()
