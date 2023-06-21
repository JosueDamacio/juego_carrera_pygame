import pygame
from imagenes_en_pantalla import Imagen
from fondo_obj import FondoEnMovimiento
from personaje_obj import Personaje

from botones_en_pantalla import Boton
from animaciones_obj import Animación
from moneda import Moneda
from aceite import Aceite
from vida import Curacion
from enemigo import AutoEnemigo

#GENERAL--------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
FPS = 60
ANCHO_VENTANA = 1700
ALTO_VENTANA = 900
#SKINS,PERSONAJE
LISTA_SKINS = [
               "Fotos\\v1_blue.png",
               "Fotos\\v1_green.png",
               "Fotos\\v1_pink.png",
               "Fotos\\v1_celeste.png",
               "Fotos\\v1_cian.png",
               "Fotos\\v1_a.png",
               "Fotos\\v1_golden.png",
               "Fotos\\v1_acua.png",
               "Fotos\\v1_newred.png",
               "Fotos\quemavistas.png"]
PROBABILIDADES_SKINS = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
#PERSONAJE------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
player = Personaje(160,80,"Fotos\\v1_red.png",130, 600,3)
#ENEMIGO--------------------------------------------------------------------------------
enemigo = AutoEnemigo(150,70,LISTA_SKINS,PROBABILIDADES_SKINS,5,10)
lista_enemigo = enemigo.crear_lista_enemigo()

#INICIO---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
titulo_juego = Imagen(600,0,500,350,"Fotos\\titulo_inicial.png")
fondo_principal = Animación(0,0,ANCHO_VENTANA,ALTO_VENTANA,"Fotos\\animasao_escalado.png",3,6)
score_board_text = Imagen(1300,200,260,80,"Fotos\high_score_2.png")
score_board = Imagen(1238,290,400,600,"Fotos\\bordescore_2.png")
jugadores_left = 40
jugadores_top = 40
start_btn = Boton(200,500,200,100,"Fotos\start_btn.png")
info_btn = Boton(220,420,70,70,"Fotos\info_img.png")
save_btn = Boton(308,420,65,65,"Fotos\save.png")

#LOGIN----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
login_fondo = Imagen(0,0,ANCHO_VENTANA,ALTO_VENTANA,"Fotos\login_desenfoque.png")
login_btn = Boton(752,450,200,100,"Fotos\login.png")
#JUEGO--------------------------------------------------------
#---------------------------------------------------------------------------------------

ciudad =  FondoEnMovimiento(0,0,ANCHO_VENTANA,504,"Fotos\ñFINFALFAO-min.png",2,4,player)
lista_ciudad = ciudad.lista_imagenes()
camino = FondoEnMovimiento(0,500,ANCHO_VENTANA,440,"Fotos\camino.png",2,25,player)
lista_camino = camino.lista_imagenes()
#objeto coin
obj_coin = Moneda(60,60,"Fotos\coin.png",2,25)
lista_coins = obj_coin.crear_lista_objeto()
#objeto aceite
obj_aceite = Aceite(65,65,"Fotos\oil_car.png",1,25)
lista_aceite = obj_aceite.crear_lista_objeto()
#objeto vida
obj_vida = Curacion(90,90,"Fotos\curacion.png",1,25)
lista_obj_vida = obj_vida.crear_lista_objeto()

#GAME OVER-----------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
try_agine_fondo = Imagen(550,100,650,500,"Fotos\game_over.jpeg")
try_again_btn = Boton(800,600,150,150,"Fotos\\try_again_btn_1.png")
menu_btn = Boton(50,780,150,70,"Fotos\menu_btn.png")
#INFO--
#---
info_img = Imagen(0,0,ANCHO_VENTANA,ALTO_VENTANA,"Fotos\informacion.png")
#CONTROLA VENTANA A MOSTRAR------------------------------------------------------------
#--------------------------------------------------------------------------------------
mostrar = 4
run = True
