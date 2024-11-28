import pygame
import sys

#--------------PAGINAS
import paginas.menu as menu

pygame.init()
pantalla = pygame.display.set_mode((800,500))
pygame.display.set_caption("Truco Goat")
clock = pygame.time.Clock()

bandera = True

while bandera == True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          sys.exit()

    menu.inicio(pantalla)

    pygame.display.flip()     
    clock.tick(60)

pygame.quit()


