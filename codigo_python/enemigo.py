import pygame
import random
import texto_en_pantalla
import colores

def skin_aleatoria(self):
        skin_aleatoria = random.choices(self.skins_totales,self.probabilidades)[0]
        return (skin_aleatoria)

def getSuperficie(path, ancho, alto):
    #reajusta el tamaño de la imagen y devuelve la superficie
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class AutoEnemigo:
    def __init__(self, ancho, alto,skins:list,probabilidades:list ,numero_de_autos, velocidad):
        self.skins_totales = skins
        self.probabilidades = probabilidades
        self.path = skin_aleatoria(self)
        self.imagen = getSuperficie(self.path, ancho, alto)
        self.ancho = ancho
        self.alto = alto
        self.cantidad = numero_de_autos
        self.movimiento = velocidad
        self.imagen_rect = self.imagen.get_rect()
        self.imagen_rect.x = random.randrange(1700, 4100, 100)
        self.imagen_rect.y = random.randrange(600, 850, 50)
        self.rect_hitbox = self.imagen_rect.copy()
        self.rect_hitbox.x += 12
        self.rect_hitbox.y += 25
        self.rect_hitbox.width -= 30
        self.rect_hitbox.height -= 30
        
    def reaparecer(self):
        #la imagen del auto reaparece dentro de un rango
        #junto al reajuste de su rectangulo
        self.imagen_rect.x = random.randrange(1700,4100,100) #rango de aparicion continua
        self.imagen_rect.y = random.randrange(600,850,50)
        self.rect_hitbox.x = self.imagen_rect.x + 15
        self.rect_hitbox.y = self.imagen_rect.y + 25

    def avanzar(self, lista_objeto):
        for objeto in lista_objeto:
            avance_entero = int(self.movimiento)
            objeto.imagen_rect.x -= avance_entero
            objeto.rect_hitbox.x -= avance_entero

    def crear_lista_enemigo(self):
        lista_enemigos = []
        for e in range(self.cantidad):
            #el code piensa que esto es una tupla... y lo es xd
            enemigo = AutoEnemigo(self.ancho,
                                  self.alto,
                                  self.skins_totales,
                                  self.probabilidades,
                                  self.cantidad,
                                  self.movimiento)
            lista_enemigos.append(enemigo)
        return lista_enemigos

    def actualizar_pantalla(self, lista_enemigos, pantalla, player):
        contador_autos_avanzados = 0
        velocidad_de_rebasamiento = 3
        for enemigo in lista_enemigos:
            if enemigo.imagen_rect.x < -180:
                enemigo.reaparecer()

            if player.rect_hitbox.colliderect(enemigo.rect_hitbox) and player.invulnerable == False:
                player.chocado = True
                player.invulnerable = True
                player.control_movimiento = 0
                player.vida -= 1
                player.monedas -= 75
                #hacer que la explosion tomer las posicones del auto como parametro para mostrarse, porque sino no se mostrara correctamente
                #verificar que la explosion sea para el auto chocado en cuestion y no todos
                self.mostrar_explosion = True
                self.movimiento = self.movimiento *(-1 * velocidad_de_rebasamiento)
 
            if enemigo.imagen_rect.x > 4100:
                contador_autos_avanzados += 1
                if contador_autos_avanzados > (self.cantidad -1):
                    player.invulnerable = False
                    player.chocado = False
                    player.control_movimiento = 1
                    #acá se podria agregar un delay o algo asi
                    self.movimiento = self.movimiento/velocidad_de_rebasamiento
                    self.movimiento = self.movimiento * -1
                    enemigo.reaparecer()
            pantalla.blit(enemigo.imagen, enemigo.imagen_rect)
            #pygame.draw.rect(pantalla, colores.RED4, enemigo.rect_hitbox)
        texto_en_pantalla.actualiza_monedas(pantalla,player)
        texto_en_pantalla.actualiza_vida(pantalla, player)