import pygame

#Funcion para dibujar imagen del fondo del menu
def dibujar_fondo(pantalla):
    info = pygame.display.Info()
    image = pygame.image.load("recursos/fondos/fondo_menu.jpg")
    image = pygame.transform.scale(image, (info.current_w, info.current_h))
    pantalla.blit(image, (0, 0)) 

#-----------------------------------START
def inicio(pantalla):
    dibujar_fondo(pantalla)
