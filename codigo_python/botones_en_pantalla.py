import pygame
from imagenes_en_pantalla import Imagen

class Boton(Imagen):
    def __init__(self, x, y, ancho, alto, path) -> None:
        super().__init__(x, y, ancho, alto, path)#hace referencia a la clase padre

        self.rectangulo = pygame.Rect(x, y, ancho, alto)

    def clickeado(self,lista_click,mostrar,numero_anterior,numero_actual):
        if lista_click[0] > self.rectangulo[0] and lista_click[0] < (self.rectangulo[0]+self.rectangulo[2]):
            if lista_click[1] > self.rectangulo[1] and lista_click[1] < (self.rectangulo[1]+self.rectangulo[3]):
                mostrar = numero_actual
                return mostrar
        else:
            mostrar = numero_anterior
            return mostrar

'''  copia funcional 19:41 12/6
import pygame
from imagenes_en_pantalla import Imagen

class Boton(Imagen):
    def __init__(self, x, y, ancho, alto, path) -> None:
        super().__init__(x, y, ancho, alto, path)#hace referencia a la clase padre

        self.rectangulo = pygame.Rect(x, y, ancho, alto)

    def clickeado(self,lista_click,mostrar,numero_anterior,numero_actual):
        if lista_click[0] > self.rectangulo[0] and lista_click[0] < (self.rectangulo[0]+self.rectangulo[2]):
            if lista_click[1] > self.rectangulo[1] and lista_click[1] < (self.rectangulo[1]+self.rectangulo[3]):
                mostrar = numero_actual
                return mostrar
        else:
            mostrar = numero_anterior
            return mostrar
'''