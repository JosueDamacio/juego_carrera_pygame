import pygame
import random
import colores


def getSuperficie(path, ancho, alto):
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class ObjetoEnPista:
    def __init__(self, ancho, alto, path,numero_de_objetos, velocidad):
        self.ancho = ancho
        self.alto = alto
        self.img_path = path
        self.imagen = getSuperficie(path, ancho, alto)
        self.rect_img = self.imagen.get_rect()
        self.rect_img.x = random.randrange(1700, 4100, 100)
        self.rect_img.y = random.randrange(600, 850, 50)
        self.rect_hitbox = self.rect_img.copy()
        self.cantidad = numero_de_objetos
        self.movimiento = velocidad
        #self.actualizar_hitbox() #en todos


        #self.velocidad_rebasamiento = 3 #en auto


    #agregar y cambiar segun el objeto
    '''def actualizar_hitbox(self):
        self.rect_hitbox.width = self.rect_img.width - 30
        self.rect_hitbox.height = self.rect_img.height - 30
        self.rect_hitbox.x = self.rect_img.x + 15
        self.rect_hitbox.y = self.rect_img.y + 25'''
        
    def avanzar(self, lista_objeto): 
        for objeto in lista_objeto:
            avance_entero = int(self.movimiento)
            objeto.rect_img.x -= avance_entero
            objeto.rect_hitbox.x = objeto.rect_img.x

    def reaparecer(self):
        porcentaje = 0.05
        self.rect_img.x = random.randrange(1700,4100,100) #rango de aparicion continua
        self.rect_img.y = random.randrange(520,850,50)
        self.rect_hitbox.x = self.rect_img.x 
        self.rect_hitbox.y = self.rect_img.y -5 #el rect aparece mas arriba

    def crear_lista_objeto(self):
        lista_objetos = []
        for o in range(self.cantidad):
            objeto = ObjetoEnPista(self.ancho,self.alto,self.img_path,self.cantidad,self.movimiento)
            lista_objetos.append(objeto)
        return lista_objetos


#SE HARA UN ACTUALIZAR DISTINTO PARA CADA HEREDERO
    '''def actualizar(self,lista_objetos,pantalla):
        for objeto in lista_objetos:
            if objeto.rect_img.x < -(objeto.rect_img.x): #change: no se harcodea cuan fuera de la pantalla debe estar pa reaparecer
                objeto.reaparecer()'''
            

    '''
    #si hay error es porque elimine un par de cosas 


    def actualizar_pantalla(self, lista_objetos, pantalla, player):
        for objeto in lista_objetos:
            if objeto.rect_img.x < -180:
                objeto.reaparecer()

            if player.rect_hitbox.colliderect(objeto.rect_hitbox) and player.invulnerable == False:
                player.chocado = True
                player.invulnerable = True
                player.control_movimiento = 0
                player.vida -= 1
                #hacer que la explosion tomer las posicones del auto como parametro para mostrarse, porque sino no se mostrara correctamente
                #verificar que la explosion sea para el auto chocado en cuestion y no todos
                self.mostrar_explosion = True
                self.movimiento = self.movimiento *(-1 * velocidad_de_rebasamiento)
                objeto.reaparecer()

            if objeto.rect_img.x > 4100:
                contador_objetos_avanzados += 1
                if contador_objetos_avanzados > (self.cantidad -1):
                    player.invulnerable = False
                    player.chocado = False
                    player.control_movimiento = 1
                    #acá se podria agregar un delay o algo asi
                    self.movimiento = self.movimiento/velocidad_de_rebasamiento
                    self.movimiento = self.movimiento * -1
                    objeto.reaparecer()
            pantalla.blit(objeto.imagen, objeto.rect_img)
            #pygame.draw.rect(pantalla, colores.RED4, objeto.rect_hitbox)
        texto_en_pantalla.actualiza_vida(pantalla, player)'''


        #hacer un contador comun con el user event en el main, que se reciba por parametro en un acumuldaor local
        #y cuando dicho acumulador llegue a X valor, hacer reaparecer e igualar el acumulador a 0