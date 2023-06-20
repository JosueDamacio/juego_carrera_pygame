import pygame

def get_superficie(path,filas,columnas):
    lista = []
    superficie_img = pygame.image.load(path)
    ancho_fotograma = int(superficie_img.get_width()/columnas)
    alto_fotograma = int(superficie_img.get_height()/filas)

    for fila in range(filas):
        for columna in range(columnas):
            x = columna * ancho_fotograma #al fotograma le da el ancho y alto que tiene 
            y = fila * alto_fotograma
            #guarda un trozo superficial de la imagen grande
            superficie_fotograma = superficie_img.subsurface(x,y,ancho_fotograma,alto_fotograma)
            lista.append(superficie_fotograma)

    return(lista)

class Animación:
    def __init__(self,x,y,ancho,alto,path_sprites,filas,columnas) -> None:
        self.total_frames = get_superficie(path_sprites,filas,columnas) #3,4
        self.frame_actual = 0
        self.animacion = self.total_frames
        self.imagen = self.animacion[self.frame_actual]
        self.pos_x = x
        self.pos_y = y
        self.ancho = ancho
        self.alto = alto
        self.mostrar_animacion = False

    def actualizar(self):
    #en el caso de animaciones debemos limitar la cantidad de filas y columnas
    #para que no se nos vaya de mambo
        #print("EL FRAME ACTUAL ES", self.frame_actual)
        if (self.frame_actual < len(self.animacion)-1):
            self.frame_actual += 1
        else:
            self.frame_actual = 0
    def dibujar_animación(self,pantalla):
        self.imagen = self.animacion[self.frame_actual]
        pantalla.blit(self.imagen,(self.pos_x,self.pos_y))