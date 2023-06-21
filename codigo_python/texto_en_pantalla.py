import pygame
import colores

#se encarga de mostrar la vida, el tiempo y las monedas, estas funciones 
#se llaman desde distintas partes del codigo segun lo requieran
def actualiza_vida(ventana, personaje):
    font = pygame.font.SysFont("Arial Narrow", 45)
    text = font.render("Vidas: {0}".format(personaje.vida), True, colores.RED2)
    ventana.blit(text, (10, 10))

def mostrar_tiempo(ventana,minutos,segundos):

    font = pygame.font.SysFont("Arial Narrow", 45)
    text = font.render("Tiempo:{0}:{1}".format(minutos,segundos), True, colores.BLACK)
    ventana.blit(text, (800, 10))

def actualiza_monedas(ventana,personaje):
    font = pygame.font.SysFont("Arial Narrow", 45)
    text = font.render("Monedas: {0}".format(personaje.monedas), True, colores.ORANGE)
    ventana.blit(text, (1200, 10))
