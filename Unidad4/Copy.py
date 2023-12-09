import pygame
import sys
from pygame.locals import QUIT

# Inicializa pygame
pygame.init()
# Se crea la ventana definiendo el tamaño (Ancho, Alto)
ventana = pygame.display.set_mode((800, 600))
# Titulo de la ventana
pygame.display.set_caption('Carrito virtual')

# Se carga imagen del carrito
Car = pygame.image.load('Carrito.png')
Car = pygame.transform.scale(Car, (50, 45))

VelocidadCar = 3
direccion = True
CarPosX, CarPosY = 80, 60

# Lista de puntos a visitar
points_to_visit = [(200, 200), (400, 300), (600, 100)]
current_point = 0

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

    # Lógica de movimiento
    if current_point < len(points_to_visit):
        target_x, target_y = points_to_visit[current_point]
        direction_x = 1 if target_x > CarPosX else -1 if target_x < CarPosX else 0
        direction_y = 1 if target_y > CarPosY else -1 if target_y < CarPosY else 0

        CarPosX += direction_x * VelocidadCar
        CarPosY += direction_y * VelocidadCar

        # Verifica si ha llegado al punto y actualiza al siguiente
        if (direction_x > 0 and CarPosX >= target_x) or (direction_x < 0 and CarPosX <= target_x):
            if (direction_y > 0 and CarPosY >= target_y) or (direction_y < 0 and CarPosY <= target_y):
                current_point += 1

    ventana.fill(fondo)  # Limpia la pantalla
    pygame.draw.line(ventana, Color, (60, 80), (200, 80), 10)
    pygame.draw.line(ventana, Color, (60, 76), (60, 500), 10)
    ventana.blit(Car, (CarPosX, CarPosY))

    pygame.display.update()