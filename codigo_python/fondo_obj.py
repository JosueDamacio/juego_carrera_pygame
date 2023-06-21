import pygame

def getSuperficie(ancho, alto,path):
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class FondoEnMovimiento():
    def __init__(self,x,y,ancho,alto,path:str,cantidad_imagenes,movimiento,player) -> None:
        self.path = path
        self.ancho = ancho
        self.imagen = getSuperficie(ancho, alto, path)
        self.rect_imagen = self.imagen.get_rect()  # Obtiene el rectángulo de la imagen
        self.pos_x = x
        self.pos_y = y
        #self.ancho = self.rect_imagen.width  # Obtiene el ancho del rectángulo
        self.alto = self.rect_imagen.height  # Obtiene el alto del rectángulo
        self.movimiento_ingresado = movimiento
        self.movimiento = self.movimiento_actual(player)
        self.cantidad = cantidad_imagenes #cuantas imagenes deben aparecer una detras de otra para no dejar un espacio vacio en la pantalla
        self.player = player

    def movimiento_actual(self, player):
        if player.control_movimiento == 0:
            return 0
        else:
            return self.movimiento_ingresado

    def lista_imagenes(self):
        lista_imagenes = []
        eje_x_agregado = 0
        for img in range(self.cantidad):
            imagen = FondoEnMovimiento(self.pos_x, self.pos_y, self.ancho, self.alto, self.path, self.cantidad, self.movimiento, self.player)
            imagen.pos_x = eje_x_agregado
            lista_imagenes.append(imagen)
            eje_x_agregado += self.ancho
        return lista_imagenes

    def avanzar(self, lista_imagenes, ancho_pantalla,ventana,player):
        #a cada imagen le resta en x lo establecido como velocidad
        for imagen in lista_imagenes:
            imagen.movimiento = self.movimiento_actual(player)
            imagen.pos_x -= imagen.movimiento
            if imagen.pos_x == ancho_pantalla * -1:
                #print(imagen.pos_x) = -1710, pero ancho_pantalla es 1700
                imagen.reaparecer(ancho_pantalla)
                imagen.movimiento_actual(player)
            ventana.blit(imagen.imagen, (imagen.pos_x, imagen.pos_y))

    def reaparecer(self, ancho_pantalla):
        self.pos_x = 0
        self.pos_x += ancho_pantalla
