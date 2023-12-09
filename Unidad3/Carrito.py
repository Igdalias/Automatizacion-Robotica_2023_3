import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación Seguidor de Línea")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

robot_width, robot_height = 30, 30
robot_x, robot_y = width // 2, height // 2
robot_speed = 5

# Definir las coordenadas de la ruta
ruta_rectangular = [(100, 100), (700, 100), (700, 500), (100, 500)]

# Añadir líneas adicionales
linea_adicional_1 = [(200, 200), (400, 200)]
linea_adicional_2 = [(500, 300), (600, 300)]

ruta_rectangular.extend(linea_adicional_1)
ruta_rectangular.extend(linea_adicional_2)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Mover el robot
    if keys[pygame.K_LEFT]:
        robot_x -= robot_speed
    if keys[pygame.K_RIGHT]:
        robot_x += robot_speed
    if keys[pygame.K_UP]:
        robot_y -= robot_speed
    if keys[pygame.K_DOWN]:
        robot_y += robot_speed

    # Dibujar el fondo
    screen.fill(white)

    # Dibujar la ruta rectangular
    pygame.draw.polygon(screen, red, ruta_rectangular)

    # Dibujar el robot
    pygame.draw.rect(screen, black, (robot_x, robot_y, robot_width, robot_height))

    # Actualizar la pantalla
    pygame.display.flip()

    pygame.time.Clock().tick(30)