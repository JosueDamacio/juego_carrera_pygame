import pygame
import random
import texto_en_pantalla
import colores


def getSuperficie(path, ancho, alto):
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class Enemigo:
    def __init__(self, ancho, alto, path,numero_de_autos, velocidad):

        self.ancho = ancho
        self.alto = alto
        self.img_path = path
        self.imagen = getSuperficie(path, ancho, alto)
        self.rect_img = self.imagen.get_rect()
        self.rect_img.x = random.randrange(1700, 4100, 100)
        self.rect_img.y = random.randrange(600, 850, 50)
        self.rect_hitbox = self.rect_img.copy()
        self.cantidad = numero_de_autos
        self.movimiento = velocidad
        self.actualizar_hitbox()
        #self.velocidad_rebasamiento = 3 #en auto

    def actualizar_hitbox(self):
        self.rect_hitbox.width = self.rect_img.width - 30
        self.rect_hitbox.height = self.rect_img.height - 30
        self.rect_hitbox.x = self.rect_img.x + 15
        self.rect_hitbox.y = self.rect_img.y + 25

        '''self.ancho = ancho
        self.alto = alto
        self.img_path = path
        self.imagen = getSuperficie(path, ancho, alto)
        self.rect_img = self.imagen.get_rect()
        self.ancho_img = self.rect_img.width 
        self.alto_img = self.rect_img.height
        self.rect_img.x = random.randrange(1700,4100,100) #rango de aparicion al empezar
        self.rect_img.y = random.randrange(600,850,50)
        self.rect_hitbox = self.rect_img.copy()
        self.rect_hitbox.width = self.ancho_img -30
        self.rect_hitbox.height = self.alto_img -30
        self.rect_hitbox.x = self.rect_img.x +15
        self.rect_hitbox.y = self.rect_img.y +25
        self.cantidad = numero_de_autos
        self.movimiento = velocidad'''

    def avanzar(self, lista_objeto): 
        for objeto in lista_objeto:
            avance_entero = int(self.movimiento)
            objeto.rect_img.x -= avance_entero
            objeto.rect_hitbox.x = objeto.rect_img.x

    def reaparecer(self):
        self.rect_hitbox.x = random.randrange(1700,4100,100) #rango de aparicion continua
        self.rect_hitbox.y = random.randrange(600,850,50)
        self.rect_img.x = self.rect_hitbox.x
        self.rect_img.y = self.rect_hitbox.y -15

    def crear_lista_enemigo(self):
        lista_enemigos = []
        for e in range(self.cantidad):
            #el code piensa que esto es una tupla... y lo es xd
            enemigo = Enemigo(self.ancho,self.alto,self.img_path,self.cantidad,self.movimiento)
            lista_enemigos.append(enemigo)
        return lista_enemigos

    def actualizar_pantalla(self, lista_enemigos, pantalla, player):
        contador_autos_avanzados = 0
        velocidad_de_rebasamiento = 3
        for enemigo in lista_enemigos:
            if enemigo.rect_img.x < -180:
                enemigo.reaparecer()

            if player.rect_hitbox.colliderect(enemigo.rect_hitbox) and player.invulnerable == False:
                player.chocado = True
                player.invulnerable = True
                player.control_movimiento = 0
                player.vida -= 1
                #hacer que la explosion tomer las posicones del auto como parametro para mostrarse, porque sino no se mostrara correctamente
                #verificar que la explosion sea para el auto chocado en cuestion y no todos
                self.mostrar_explosion = True
                self.movimiento = self.movimiento *(-1 * velocidad_de_rebasamiento)
                enemigo.reaparecer()

            if enemigo.rect_img.x > 4100:
                contador_autos_avanzados += 1
                if contador_autos_avanzados > (self.cantidad -1):
                    player.invulnerable = False
                    player.chocado = False
                    player.control_movimiento = 1
                    #acá se podria agregar un delay o algo asi
                    self.movimiento = self.movimiento/velocidad_de_rebasamiento
                    self.movimiento = self.movimiento * -1
                    enemigo.reaparecer()
            pantalla.blit(enemigo.imagen, enemigo.rect_img)
            pygame.draw.rect(pantalla, colores.RED4, enemigo.rect_hitbox)
        texto_en_pantalla.actualiza_vida(pantalla, player)
    

    #def posicion_previa(self):
        #lista_auto_chocado = []
        #x = self.rect_img.x
        #y = self.rect_img.y
        #ancho = self.ancho_img
        #alto = self.alto_img
        #lista_auto_chocado.append(x,y,ancho,alto)

        #return lista_auto_chocado




'''  copia funcional 2:41am 11/6
import pygame
import random
import texto_en_pantalla
import colores


def getSuperficie(path, ancho, alto):
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class Enemigo:
    def __init__(self, ancho, alto, path,numero_de_autos, velocidad):
        self.ancho = ancho
        self.alto = alto
        self.img_path = path
        self.imagen = getSuperficie(path, ancho, alto)
        self.rect_img = self.imagen.get_rect()
        self.ancho_img = self.rect_img.width 
        self.alto_img = self.rect_img.height
        self.rect_img.x = random.randrange(1700,4100,100) #rango de aparicion al empezar
        self.rect_img.y = random.randrange(600,850,50)
        self.rect_hitbox = self.rect_img.copy()
        self.rect_hitbox.width = self.ancho_img -30
        self.rect_hitbox.height = self.alto_img -30
        self.rect_hitbox.x = self.rect_img.x +15
        self.rect_hitbox.y = self.rect_img.y +25
        self.cantidad = numero_de_autos
        self.movimiento = velocidad
        self.fraccion_decimal = 0.0
        #puede recibir valores decimales para ajustar mejor la velocidad
        
    #metodos, no funciones
    def avanzar(self, lista_enemigo): 
        #sos un capo, lo arreglaste
        for enemigo in lista_enemigo:
            avance_entero = int(self.movimiento)
            self.fraccion_decimal += self.movimiento - avance_entero
            if self.fraccion_decimal >= 1.0:
                avance_entero += 1
                self.fraccion_decimal -= 1.0
            enemigo.rect_img.x -= avance_entero #"avanza" con su rect
            enemigo.rect_hitbox.x = enemigo.rect_img.x #el rect

    def reaparecer(self):
        self.rect_hitbox.x = random.randrange(1700,4100,100) #rango de aparicion continua
        self.rect_hitbox.y = random.randrange(600,850,50)
        self.rect_img.x = self.rect_hitbox.x
        self.rect_img.y = self.rect_hitbox.y -15

    def crear_lista_enemigo(self):
        lista_enemigos = []
        for e in range(self.cantidad):
            #el code piensa que esto es una tupla... y lo es xd
            enemigo = Enemigo(self.ancho,self.alto,self.img_path,self.cantidad,self.movimiento)
            lista_enemigos.append(enemigo)
        return lista_enemigos

    def actualizar_pantalla(self, lista_enemigos, pantalla, player):
        contador_autos_avanzados = 0
        velocidad_de_rebasamiento = 3
        for enemigo in lista_enemigos:
            if enemigo.rect_img.x < -180:
                enemigo.reaparecer()

            if player.rect_hitbox.colliderect(enemigo.rect_hitbox) and player.invulnerable == False:
                player.chocado = True
                player.invulnerable = True
                player.control_movimiento = 0
                player.vida -= 1
                #hacer que la explosion tomer las posicones del auto como parametro para mostrarse, porque sino no se mostrara correctamente
                #verificar que la explosion sea para el auto chocado en cuestion y no todos
                self.mostrar_explosion = True
                self.movimiento = self.movimiento *(-1 * velocidad_de_rebasamiento)
                enemigo.reaparecer()

            if enemigo.rect_img.x > 4100:
                contador_autos_avanzados += 1
                if contador_autos_avanzados > (self.cantidad -1):
                    player.invulnerable = False
                    player.chocado = False
                    player.control_movimiento = 1
                    #acá se podria agregar un delay o algo asi
                    self.movimiento = self.movimiento/velocidad_de_rebasamiento
                    self.movimiento = self.movimiento * -1
                    enemigo.reaparecer()
            pantalla.blit(enemigo.imagen, enemigo.rect_img)
            #pygame.draw.rect(pantalla, colores.RED4, enemigo.rect_hitbox)
        texto_en_pantalla.actualiza_vida(pantalla, player)
    

    #def posicion_previa(self):
        #lista_auto_chocado = []
        #x = self.rect_img.x
        #y = self.rect_img.y
        #ancho = self.ancho_img
        #alto = self.alto_img
        #lista_auto_chocado.append(x,y,ancho,alto)

        #return lista_auto_chocado

'''