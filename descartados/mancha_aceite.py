import pygame
from objeto_en_pista import ObjetoEnPista
import colores
import texto_en_pantalla

class Aceite (ObjetoEnPista):
    def __init__(self, ancho, alto, path, numero_de_objetos, desplazamiento):
        super().__init__(ancho, alto, path, numero_de_objetos, desplazamiento)

        self.actualizar_hitbox()
        self.flag_aceite = False

    def actualizar_hitbox(self):
        self.rect_hitbox.width = self.rect_img.width
        self.rect_hitbox.height = self.rect_img.height
        self.rect_hitbox.x = self.rect_img.x
        self.rect_hitbox.y = self.rect_img.y

    def actualizar_en_pantalla(self,lista_objetos,pantalla,player):
        for objeto in lista_objetos:
            if objeto.rect_img.x < -800:
                objeto.reaparecer()

            if player.rect_hitbox.colliderect(objeto.rect_hitbox):
                if self.flag_aceite == False:
                    player.mancha_aceite = -2
                    player.score -=50
                    self.flag_aceite = True
                    objeto.reaparecer()
                else:
                    player.mancha_aceite = 1
                    objeto.reaparecer()
                    self.flag_aceite = False

            #pygame.draw.rect(pantalla, colores.ALICEBLUE, objeto.rect_hitbox)
            pantalla.blit(objeto.imagen, objeto.rect_img)
        texto_en_pantalla.actualiza_score(pantalla, player)

    def avanzar(self, lista_objeto,player):
        for objeto in lista_objeto:
            avance_entero = int(self.movimiento * player.control_movimiento)
            objeto.rect_img.x -= avance_entero
            objeto.rect_hitbox.x = objeto.rect_img.x
 
    #agregar un reaparecer distinto
#agregar temporizador para que aparezca