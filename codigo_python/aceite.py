import pygame
import colores
import texto_en_pantalla
import random

def getSuperficie(path, ancho, alto):
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class Aceite :
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
        self.rect_hitbox.x += 7
        self.rect_hitbox.y += 7
        self.rect_hitbox.width -= 7
        self.rect_hitbox.height -= 7
        self.flag_aceite = False

    def crear_lista_objeto(self):
        #por cada auto ingresado, se crea un objeto con el tipo auto
        lista_objetos = []
        for o in range(self.cantidad):
            objeto = Aceite(self.ancho,self.alto,self.img_path,self.cantidad,self.movimiento)
            lista_objetos.append(objeto)
        return lista_objetos
    
    def actualizar_en_pantalla(self,lista_objetos,pantalla,player):
        #se encarga de ejecutar sus efectos respecto a la pantalla
        #o interaccion con el jugador
        for objeto in lista_objetos:
            if objeto.img_dimensiones.x < -800:
                objeto.reaparecer()

            if player.rect_hitbox.colliderect(objeto.rect_hitbox):
                if self.flag_aceite == False:
                    player.mancha_aceite = -2
                    player.monedas -=50
                    self.flag_aceite = True
                    objeto.reaparecer()
                else:
                    player.mancha_aceite = 1
                    objeto.reaparecer()
                    self.flag_aceite = False

            #pygame.draw.rect(pantalla, colores.WHITE, objeto.rect_hitbox)
            pantalla.blit(objeto.imagen, objeto.rect_hitbox)
        texto_en_pantalla.actualiza_monedas(pantalla, player)

    def avanzar(self, lista_objeto,player):
        for objeto in lista_objeto:
            avance_entero = int(self.movimiento * player.control_movimiento)
            objeto.img_dimensiones.x -= avance_entero
            objeto.rect_hitbox.x -= avance_entero

    def reaparecer(self):
        self.img_dimensiones.x = random.randrange(3000,3400,100)
        self.img_dimensiones.y = random.randrange(600,850,25)
        self.rect_hitbox.x = self.img_dimensiones.x + 7
        self.rect_hitbox.y = self.img_dimensiones.y + 7