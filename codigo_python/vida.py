import pygame
import colores
import texto_en_pantalla
import random

def getSuperficie(path, ancho, alto):
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class Curacion :
    def __init__(self, ancho, alto, path,numero_de_objetos, velocidad):

        self.ancho = ancho
        self.alto = alto
        self.img_path = path
        self.imagen = getSuperficie(path, ancho, alto)
        self.cantidad = numero_de_objetos
        self.movimiento = velocidad
        self.img_dimensiones = self.imagen.get_rect()
        self.img_dimensiones.x = random.randrange(8000,9100,100)
        self.img_dimensiones.y = random.randrange(520,850,30)
        self.rect_hitbox = self.img_dimensiones.copy()
        self.rect_hitbox.x += 24
        self.rect_hitbox.y += 24
        self.rect_hitbox.width -= 48
        self.rect_hitbox.height -= 48

    def crear_lista_objeto(self):
        lista_objetos = []
        for o in range(self.cantidad):
            objeto = Curacion(self.ancho,self.alto,self.img_path,self.cantidad,self.movimiento)
            lista_objetos.append(objeto)
        return lista_objetos
    
    def actualizar_en_pantalla(self,lista_objetos,pantalla,player):
        for objeto in lista_objetos:
            if objeto.img_dimensiones.x < -600:
                objeto.reaparecer()
            if player.rect_hitbox.colliderect(objeto.rect_hitbox):
                player.vida += 1
                objeto.reaparecer()
            #pygame.draw.rect(pantalla, colores.GREENYELLOW, objeto.rect_hitbox)
            pantalla.blit(objeto.imagen, objeto.img_dimensiones)
        texto_en_pantalla.actualiza_vida(pantalla, player)

    def avanzar(self, lista_objeto,player):
        for objeto in lista_objeto:
            avance_entero = int(self.movimiento * player.control_movimiento)
            objeto.img_dimensiones.x -= avance_entero
            objeto.rect_hitbox.x -= avance_entero

    def reaparecer(self):
        self.img_dimensiones.x = random.randrange(8000,9100,100)
        self.img_dimensiones.y = random.randrange(520,850,30)
        self.rect_hitbox.x = self.img_dimensiones.x + 24
        self.rect_hitbox.y = self.img_dimensiones.y + 24