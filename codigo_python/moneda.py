import pygame
import colores
import texto_en_pantalla
import random

def getSuperficie(path, ancho, alto):
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class Moneda :
    def __init__(self, ancho, alto, path,numero_de_objetos, velocidad):

        self.ancho = ancho
        self.alto = alto
        self.img_path = path
        self.imagen = getSuperficie(path, ancho, alto)
        self.cantidad = numero_de_objetos
        self.movimiento = velocidad
        self.img_dimensiones = self.imagen.get_rect()
        self.img_dimensiones.x = random.randrange(1700,4100,100)
        self.img_dimensiones.y = random.randrange(520,850,50)
        self.rect_hitbox = self.img_dimensiones.copy()
        self.rect_hitbox.x += 8
        self.rect_hitbox.y += 8
        self.rect_hitbox.width -= 20
        self.rect_hitbox.height -= 20

    def reaparecer(self):
        self.img_dimensiones.x = random.randrange(1700,4100,100)
        self.img_dimensiones.y = random.randrange(520,850,50)
        self.rect_hitbox.x = self.img_dimensiones.x + 8
        self.rect_hitbox.y = self.img_dimensiones.y + 8
        
    def crear_lista_objeto(self):
        lista_objetos = []
        for o in range(self.cantidad):
            objeto = Moneda(self.ancho,self.alto,self.img_path,self.cantidad,self.movimiento)
            lista_objetos.append(objeto)
        return lista_objetos
    
    def actualizar_en_pantalla(self,lista_objetos,pantalla,player):
        for objeto in lista_objetos:
            if objeto.img_dimensiones.x < -500:
                objeto.reaparecer()

            if player.rect_hitbox.colliderect(objeto.rect_hitbox):
                player.monedas += 100
                objeto.reaparecer()
            pantalla.blit(objeto.imagen, objeto.img_dimensiones)
            pygame.draw.rect(pantalla, colores.GREENYELLOW, objeto.rect_hitbox)
        texto_en_pantalla.actualiza_monedas(pantalla, player)

    def avanzar(self, lista_objeto,player):
        for objeto in lista_objeto:
            avance_entero = int(self.movimiento * player.control_movimiento)
            objeto.img_dimensiones.x -= avance_entero
            objeto.rect_hitbox.x -= avance_entero


    '''
    def reaparecer(self):
        porcentaje = 0.05
        self.img_dimensiones.x = random.randrange(1700, 4100, 100)
        self.img_dimensiones.y = random.randrange(520, 850, 50)
        self.rect_hitbox.x = self.img_dimensiones.x + (self.ancho // 2) - (self.rect_hitbox.width // 2)
        self.rect_hitbox.y = self.img_dimensiones.y + (self.alto // 2) - (self.rect_hitbox.height // 2)

    '''