import pygame

def getSuperficie(ancho, alto, path):
    surface_imagen = pygame.image.load(path)
    surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
    return surface_imagen

class Imagen:
    def __init__(self, x, y, ancho, alto, path):
        self.imagen = getSuperficie(ancho, alto, path)
        self.coordenada_x = x
        self.coordenada_y = y
        
    
    def mostrar_imagen(self, pantalla):
        pantalla.blit(self.imagen, (self.coordenada_x, self.coordenada_y))
