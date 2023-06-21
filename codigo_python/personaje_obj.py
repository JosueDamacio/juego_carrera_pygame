import pygame
import colores
import random

def skin_aleatoria(self):
        skin_aleatoria = random.choices(self.skins_totales,self.probabilidades)[0]
        return (skin_aleatoria)

def getSuperficie(path, ancho, alto):
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class Personaje:
    def __init__(self, ancho,alto,skin, x, y,vidas_totales): #VELOCIDAD ENTORNO AGREGADO
        self.path = skin
        self.imagen = getSuperficie(self.path, ancho, alto)
        self.rect_img = pygame.Rect(x, y, 300, 150) #300 y 150 son valores no utilizados
        self.rect_hitbox = pygame.Rect(x + 9, y + 20, 120, 48)
        self.control_movimiento = 1
        self.mancha_aceite = 1
        self.invulnerable = False
        self.vida = vidas_totales
        self.nombre = ""
        self.tiempo_jugado = 0
        self.monedas = 0
        self.final_score = 0
        #self.control_movimineto multiplica las velocidades del fondo, para que
        #de ello dependa el movimineto de su entorno, paisaje y objetos como monedas

    def actualizar_pantalla(self, pantalla):
        pantalla.blit(self.imagen, self.rect_img)
        #pygame.draw.rect(pantalla, colores.BLUEVIOLET, self.rect_hitbox)
 
    def movimiento(self, velocidad, eje):
        cantidad = (velocidad * self.mancha_aceite)
        if eje == "x":
            limite_x = self.rect_img.x + cantidad
            limite_x = self.rect_hitbox.x + cantidad 
            if limite_x > 20 and limite_x < 1000:
                self.rect_img.x += cantidad
                self.rect_hitbox.x += cantidad

        if eje == "y":
            limite_y = self.rect_img.y + cantidad
            limite_y = self.rect_hitbox.y + cantidad 
            if limite_y >= 525 and limite_y < 850:
                self.rect_img.y += cantidad
                self.rect_hitbox.y += cantidad
    def invulnerabilidad(self):
        if self.control_movimiento < 1:
            self.invulnerable = True

    def calcula_score(self):
            self.final_score = self.monedas - self.tiempo_jugado
    def monedas_no_negativas(self):
        if self.monedas < 0:
             self.monedas = 0