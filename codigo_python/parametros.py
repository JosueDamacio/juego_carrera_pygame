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
LISTA_SKINS = ["Fotos\\v1_red.png","Fotos\\v1_blue.png","Fotos\\v1_green.png","Fotos\\v1_golden.png","Fotos\\v1_pink.png"]
PROBABILIDADES_SKINS = [0.3,0.2,0.2,0.2,0.1]
#PERSONAJE------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
player = Personaje(160,80,LISTA_SKINS,PROBABILIDADES_SKINS,130, 600,3)
#ENEMIGO--------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#auto_azul = Enemigo(100,50,"Fotos\B_CAR.png",6,12)
#lista_autos_azules = auto_azul.crear_lista_enemigo()

enemigo = AutoEnemigo(120,66,"Fotos\B_CAR.png",3,10)
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
#skin_btn = Imagen(ANCHO_VENTANA/2+50,460,100,100,"Fotos\skin_btn.png")
#LOGIN----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
login_fondo = Imagen(0,0,ANCHO_VENTANA,ALTO_VENTANA,"Fotos\login_desenfoque.png")
login_btn = Boton(752,450,200,100,"Fotos\login.png")
#JUEGO--------------------------------------------------------
#---------------------------------------------------------------------------------------
#ver como hacerlo con una sola img

ciudad =  FondoEnMovimiento(0,0,ANCHO_VENTANA,504,"Fotos\ñFINFALFAO-min.png",2,4,player)
lista_ciudad = ciudad.lista_imagenes()

camino = FondoEnMovimiento(0,500,ANCHO_VENTANA,440,"Fotos\camino.png",2,25,player)
lista_camino = camino.lista_imagenes()

#objeto coin
obj_coin = Moneda(60,60,"Fotos\coin.png",2,25)
lista_coins = obj_coin.crear_lista_objeto()
#objeto aceite
obj_aceite = Aceite(50,50,"Fotos\oil_car.png",1,25)
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
mostrar = 0
run = True
#ANIMACIONES---------------------------------------------------------------------------
#AL CHOCAR-----------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
explosion_choque = Animación(10,10,30,30,"Fotos\\frames_explosion.png",3,4)
#






''' copia funcional 0:25am 12/6

import pygame
from imagenes_en_pantalla import Imagen
from fondo_obj import FondoEnMovimiento
from personaje_obj import Personaje
from enemigo_obj import Enemigo

from botones_en_pantalla import Boton
from animaciones_obj import Animación
from moneda import Moneda
from mancha_aceite import Aceite
from bonus_vida import Curacion
from prueba_blue_car import AutoEnemigo

#GENERAL--------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
FPS = 60
ANCHO_VENTANA = 1700
ALTO_VENTANA = 900
#SKINS,PERSONAJE
LISTA_SKINS = ["Fotos\\v1_red.png","Fotos\\v1_blue.png","Fotos\\v1_green.png","Fotos\\v1_golden.png","Fotos\\v1_pink.png"]
PROBABILIDADES_SKINS = [0.3,0.2,0.2,0.2,0.1]
#PERSONAJE------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
player = Personaje(160,80,LISTA_SKINS,PROBABILIDADES_SKINS,130, 600,2)
#ENEMIGO--------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#auto_azul = Enemigo(100,50,"Fotos\B_CAR.png",6,12)
#lista_autos_azules = auto_azul.crear_lista_enemigo()

blue_car = AutoEnemigo(120,66,"Fotos\B_CAR.png",3,10)
lista_blue_car = blue_car.crear_lista_objeto()
#INICIO---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
titulo_juego = Imagen(600,0,500,350,"Fotos\\titulo_inicial.png")
fondo_principal = Animación(0,0,ANCHO_VENTANA,ALTO_VENTANA,"Fotos\\animasao_escalado.png",3,6)
score_board_text = Imagen(1300,200,260,80,"Fotos\high_score_2.png")
score_board = Imagen(1238,290,400,600,"Fotos\\bordescore_2.png")
start_btn = Boton(300,400,200,100,"Fotos\start_btn.png")
#skin_btn = Imagen(ANCHO_VENTANA/2+50,460,100,100,"Fotos\skin_btn.png")
#LOGIN----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
login_fondo = Imagen(0,0,ANCHO_VENTANA,ALTO_VENTANA,"Fotos\login_desenfoque.png")
login_btn = Boton(752,450,200,100,"Fotos\login.png")
#JUEGO--------------------------------------------------------
#---------------------------------------------------------------------------------------
#ver como hacerlo con una sola img

ciudad =  FondoEnMovimiento(0,0,ANCHO_VENTANA,504,"Fotos\ñFINFALFAO-min.png",2,4,player)
lista_ciudad = ciudad.lista_imagenes()

camino = FondoEnMovimiento(0,500,ANCHO_VENTANA,440,"Fotos\camino.png",2,25,player)
lista_camino = camino.lista_imagenes()

#objeto coin
obj_coin = Moneda(60,60,"Fotos\coin.png",2,25)
lista_coins = obj_coin.crear_lista_objeto()
#objeto aceite
obj_aceite = Aceite(50,50,"Fotos\oil_car.png",1,25)
lista_aceite = obj_aceite.crear_lista_objeto()
#objeto vida
obj_vida = Curacion(90,90,"Fotos\curacion.png",1,25)
lista_obj_vida = obj_vida.crear_lista_objeto()
#GAME OVER-----------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
try_agine_fondo = Imagen(550,100,650,500,"Fotos\game_over.jpeg")
try_again_btn = Boton(800,600,150,150,"Fotos\\try_again_btn_1.png")
menu_btn = Boton(20,800,150,70,"Fotos\\back.png")
#CONTROLA VENTANA A MOSTRAR------------------------------------------------------------
#--------------------------------------------------------------------------------------
mostrar = 0
run = True
#ANIMACIONES---------------------------------------------------------------------------
#AL CHOCAR-----------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
explosion_choque = Animación(10,10,30,30,"Fotos\\frames_explosion.png",3,4)
#
'''