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

'''  copia funcional 2:41am 11/6

import pygame
import colores

#QUIERO QUE LA VIDA SE MUESTRE COMO CORAZONES (IMAGEN) #para hacer
def actualiza_vida(ventana, personaje): #usado en auto_azul
    font = pygame.font.SysFont("Arial Narrow", 45)
    text = font.render("VIDAS: {0}".format(personaje.vida), True, colores.WHITE)
    ventana.blit(text, (10, 10))
    
def actualiza_score(ventana,personaje): #no usado aun
    font = pygame.font.SysFont("Arial Narrow", 45)
    text = font.render("PUNTAJE: {0}".format(personaje.score), True, colores.GOLD2)
    ventana.blit(text, (800, 10))

def mostrar_tiempo(ventana,time): #usado en main

    font = pygame.font.SysFont("Arial Narrow", 45)
    text = font.render("SEGUNDOS: {0}".format(time), True, colores.GREEN2)
    ventana.blit(text, (800, 10))
'''