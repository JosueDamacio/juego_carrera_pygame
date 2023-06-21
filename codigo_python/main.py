import pygame
import colores
from parametros import *
import texto_en_pantalla
import pygame.mixer
from funcion_guardar import guardar_progreso

import sqlite3

'''
agregar sonido de aceite y vida
-Skins random a enemigo
'''
acu_segundos = 0
acu_minutos = 0

ventana_principal = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
pygame.display.set_caption("Carreras 01")

#INIT DEL JUEGO
pygame.init()

#BASE DE DATOS
#se crea la base de datos
with sqlite3.connect("base_datos_prueba.db") as conexion:
    try:
        sentencia = ''' create table jugadores
                    (

                            id integer primary key autoincrement,
                            nombre_jugador text,
                            puntaje integer

                    )
                '''
        conexion.execute(sentencia)
        print("se creo la tabla")

    except sqlite3.OperationalError:
        print("tabla ya creada")

    #solo se seleccionan los primeros 6 de forma descendente y se guardan en una lista de
    #diccionarios para luego imprimirlos en el scoreboard dentro de "MENU DEL JUEGO"
    cursor = conexion.execute("SELECT * FROM jugadores ORDER BY puntaje DESC LIMIT 6")
    jugadores_totales = cursor.fetchall()

    font_nombre_jugadores = pygame.font.SysFont("Arial", 30)
    font_score_jugadores = pygame.font.SysFont("Arial", 30)

    jugadores_lista = []

    for i, jugador in enumerate(jugadores_totales):
        nombre = jugador[1]
        puntaje = str(jugador[2])

        jugador_dict = {"nombre": nombre, "puntaje": puntaje}
        jugadores_lista.append(jugador_dict)

#SONIDOS DEL JUEGO-------------------
canal_sonidos = pygame.mixer.Channel(1)

sonido_botones = pygame.mixer.Sound("sonidos\login.mp3")
sonido_botones.set_volume(0.3)
sonido_perder = pygame.mixer.Sound("sonidos\\0_hearts.mp3")
sonido_perder.set_volume(0.3)
sonido_vida = pygame.mixer.Sound("sonidos\\aceite.mp3")
sonido_vida.set_volume(0.3)
sonido_aceite = pygame.mixer.Sound("sonidos\one_more_heart.mp3")
sonido_aceite.set_volume(0.3)
sonido_moneda = pygame.mixer.Sound("sonidos\coin.mp3")
sonido_moneda.set_volume(0.2)

musica_menu = pygame.mixer.Sound("sonidos\inicio_music_bajo.mp3")
musica_menu.set_volume(0.1)
musica_en_juego = pygame.mixer.Sound("sonidos\in_game_2.mp3")
musica_en_juego.set_volume(0.03)
musica_game_over = pygame.mixer.Sound("sonidos\game_over.mp3")
musica_game_over.set_volume(0.07)

#login_texto======
font_login = pygame.font.SysFont("Arial",30)
nombre = ""
ingreso_rect = pygame.Rect(750,400,200,40)

reloj = pygame.time.Clock()

#USEREVENT:
contador_segundos = pygame.USEREVENT+10
pygame.time.set_timer(contador_segundos, 1000)
timer_20_ms = pygame.USEREVENT + 1
pygame.time.set_timer(timer_20_ms,100)
contador_fps = pygame.USEREVENT + 2
pygame.time.set_timer(contador_fps,FPS)

#MENU DEL JUEGO==============================================
while run:

    lista_evento = pygame.event.get()
    if mostrar == 0:
        musica_game_over.stop()
        musica_menu.play(-1)

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False
            #botones
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if start_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = 1
                elif info_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = 4
                elif save_btn.rectangulo.collidepoint(lista_click):
                    if player.nombre is not "":
                        player.calcula_score()
                        try:
                            jugador_datos = (player.nombre, player.final_score)
                            conexion.execute("INSERT INTO jugadores (nombre_jugador, puntaje) VALUES (?,?)", jugador_datos)
                            conexion.commit()
                            canal_sonidos.play(sonido_botones)
                            print("jugador insertado exitosamente")
                        except sqlite3.Error:
                            print("error al insertar el jugador")
                    else:
                        canal_sonidos.play(sonido_botones)
                        print(" ERROR debes ingresar nombre")


            if evento.type == pygame.USEREVENT + 1:
                if evento.type == timer_20_ms:
                    fondo_principal.actualizar()
                    fondo_principal.dibujar_animación(ventana_principal)

        titulo_juego.mostrar_imagen(ventana_principal)
        score_board_text.mostrar_imagen(ventana_principal)
        score_board.mostrar_imagen(ventana_principal)
        start_btn.mostrar_imagen(ventana_principal)
        info_btn.mostrar_imagen(ventana_principal)
        save_btn.mostrar_imagen(ventana_principal)
        
        #por cada jugador de la lista, se imprime el nombre y puntaje
        for i, jugador in enumerate(jugadores_lista):
                nombre = jugador["nombre"]
                puntaje = jugador["puntaje"]
                txt_nombre_jugadores = font_nombre_jugadores.render("{0}".format(nombre), True, colores.WHITE)
                txt_score_jugadores = font_score_jugadores.render("{0}".format(puntaje), True, colores.WHITE)
                ventana_principal.blit(txt_nombre_jugadores, (1270, 360 + (i * 70)))
                ventana_principal.blit(txt_score_jugadores, (1552, 360 + (i * 70)))
        
    #VENTANA LOGIN=============================================
    if mostrar == 1:
        
        login_fondo.mostrar_imagen(ventana_principal)
        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False
            #ingreso de nombre con un maximo de 6 caracteres
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE or len(nombre) == 6:
                    nombre = nombre[0:-1]
                else:
                    nombre += evento.unicode
        pygame.draw.rect(ventana_principal,colores.RED2,ingreso_rect,2)
        font_login_surface = font_login.render(nombre,True,colores.WHITE)
        ventana_principal.blit(font_login_surface,(ingreso_rect.x+8,ingreso_rect.y+4))

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False
            #botones
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if login_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = login_btn.clickeado(lista_click, mostrar, 1,2)
                    print(nombre)
                    player.nombre = nombre
                else:
                    continue
        login_btn.mostrar_imagen(ventana_principal)
        
    #PISTA DE JUEGO==============================================
    if mostrar == 2:
        musica_game_over.stop()
        musica_menu.stop()
        musica_en_juego.play(-1)
                
        ventana_principal.fill(colores.BLUE3)
        ciudad.avanzar(lista_ciudad,ANCHO_VENTANA,ventana_principal,player)
        camino.avanzar(lista_camino, ANCHO_VENTANA,ventana_principal,player)

        obj_coin.avanzar(lista_coins,player)
        obj_coin.actualizar_en_pantalla(lista_coins,ventana_principal,player)
        #cada 45 segundos aparece una vida durante 15 segundos
        #y a partir del minuto 1 apareceran manchas de aceite
        if acu_segundos > 45 and acu_segundos < 60:
            obj_vida.avanzar(lista_obj_vida,player)
            obj_vida.actualizar_en_pantalla(lista_obj_vida,ventana_principal,player)
        elif acu_minutos >= 1:
            obj_aceite.avanzar(lista_aceite,player)
            obj_aceite.actualizar_en_pantalla(lista_aceite,ventana_principal,player)

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                player.calcula_score()
                try:
                    jugador_datos = (player.nombre, player.final_score)
                    conexion.execute("INSERT INTO jugadores (nombre_jugador, puntaje) VALUES (?, ?)", jugador_datos)
                    conexion.commit()
                    canal_sonidos.play(sonido_botones)
                    print("Jugador insertado exitosamente")
                except sqlite3.Error as error:
                    print("Error al insertar el jugador:", error)
                run = False
            #contador de tiempo
            if evento.type == pygame.USEREVENT+10:
                if evento.type == contador_segundos:
                    acu_segundos += 1
                    if acu_segundos % 60 == 0:
                        acu_minutos += 1
                        acu_segundos -= 60

                    player.tiempo_jugado = acu_segundos + (acu_minutos * 60)
        
        enemigo.avanzar(lista_enemigo)
        enemigo.actualizar_pantalla(lista_enemigo,ventana_principal,player)
        player.actualizar_pantalla(ventana_principal)
        player.monedas_no_negativas()
        
        texto_en_pantalla.mostrar_tiempo(ventana_principal,acu_minutos,acu_segundos)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.movimiento(-14, "x")
        if keys[pygame.K_d]:
            player.movimiento(14, "x")
        if keys[pygame.K_s]:
            player.movimiento(14, "y")
        if keys[pygame.K_w]:
            player.movimiento(-14, "y")

        if player.vida == 0:
            canal_sonidos.play(sonido_perder)
            mostrar = 3
    #GAME OVER==============================================
    if mostrar == 3:
        musica_en_juego.stop()
        musica_menu.stop()
        musica_game_over.play(-1)

        pygame.draw.rect(ventana_principal, colores.BLACK,(0,0,ANCHO_VENTANA,ALTO_VENTANA))
        try_agine_fondo.mostrar_imagen(ventana_principal)
        try_again_btn.mostrar_imagen(ventana_principal)
        menu_btn.mostrar_imagen(ventana_principal)

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                guardar_progreso(player,conexion)
                run = False
            #botones
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if try_again_btn.rectangulo.collidepoint(lista_click) and player.monedas >= 300:
                    canal_sonidos.play(sonido_botones)
                    mostrar = 2
                    player.vida = 1
                    player.monedas -= 300
                elif menu_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = 0
                else:
                    pass
    #INFORMACION
    if mostrar == 4:
        musica_en_juego.play(-1)
        info_img.mostrar_imagen(ventana_principal)
        menu_btn.mostrar_imagen(ventana_principal)

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if menu_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = 0
                
    reloj.tick(FPS)
    pygame.display.flip()
    pygame.mixer.music.stop()

pygame.quit()

''' copia funcional ----------
import pygame
import colores
from parametros import *
import texto_en_pantalla
import pygame.mixer

import sqlite3

#AUN NO IMPLEMENTADA BASE DE DATOS

acu_segundos = 0
acu_minutos = 0

ventana_principal = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
pygame.display.set_caption("Carreras 01")

#INIT DEL JUEGO
pygame.init()

#SONIDOS DEL JUEGO-------------------
sonido_botones = pygame.mixer.Sound("sonidos\login.mp3")
sonido_botones.set_volume(0.3)
canal_sonidos = pygame.mixer.Channel(1)
sonido_perder = pygame.mixer.Sound("sonidos\\0_hearts.mp3")
sonido_perder.set_volume(0.3)

musica_menu = pygame.mixer.Sound("sonidos\inicio_music_bajo.mp3")
musica_menu.set_volume(0.1)
musica_en_juego = pygame.mixer.Sound("sonidos\in_game_2.mp3")
musica_en_juego.set_volume(0.03)
musica_game_over = pygame.mixer.Sound("sonidos\game_over.mp3")
musica_game_over.set_volume(0.07)

#login_texto======
font_login = pygame.font.SysFont("Arial",30)
nombre = ""
ingreso_rect = pygame.Rect(750,400,200,40)

reloj = pygame.time.Clock()

#USEREVENT:
contador_segundos = pygame.USEREVENT+10
pygame.time.set_timer(contador_segundos, 1000)
timer_20_ms = pygame.USEREVENT + 1
pygame.time.set_timer(timer_20_ms,100)
contador_fps = pygame.USEREVENT + 2
pygame.time.set_timer(contador_fps,FPS)

contador = 0

#MENU DEL JUEGO==============================================
while run:

    lista_evento = pygame.event.get()
    if mostrar == 0:
        musica_game_over.stop()
        musica_menu.play(-1)

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False
            #botones
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if start_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = 1
                elif info_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = 4

            if evento.type == pygame.USEREVENT + 1:
                if evento.type == timer_20_ms:
                    fondo_principal.actualizar()
                    fondo_principal.dibujar_animación(ventana_principal)

        #ACA ESTABA EL SCOREBOARD

        score_board_text.mostrar_imagen(ventana_principal)
        score_board.mostrar_imagen(ventana_principal)
        start_btn.mostrar_imagen(ventana_principal)
        info_btn.mostrar_imagen(ventana_principal)
        titulo_juego.mostrar_imagen(ventana_principal)
        
    #VENTANA LOGIN=============================================
    if mostrar == 1:
        
        login_fondo.mostrar_imagen(ventana_principal)
        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False
            #ingreso de nombre con un maximo de 5 caracteres
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE or len(nombre) == 5:
                    nombre = nombre[0:-1]
                else:
                    nombre += evento.unicode
        pygame.draw.rect(ventana_principal,colores.RED2,ingreso_rect,2)
        font_login_surface = font_login.render(nombre,True,colores.WHITE)
        ventana_principal.blit(font_login_surface,(ingreso_rect.x+8,ingreso_rect.y+4))

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False
            #botones
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if login_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = login_btn.clickeado(lista_click, mostrar, 1,2)
                    print(nombre)
                    player.nombre = nombre
                else:
                    continue
        login_btn.mostrar_imagen(ventana_principal)
        
    #PISTA DE JUEGO==============================================
    if mostrar == 2:
        musica_game_over.stop()
        musica_menu.stop()
        musica_en_juego.play(-1)
                
        ventana_principal.fill(colores.BLUE3)
        ciudad.avanzar(lista_ciudad,ANCHO_VENTANA,ventana_principal,player)
        camino.avanzar(lista_camino, ANCHO_VENTANA,ventana_principal,player)

        obj_coin.avanzar(lista_coins,player)
        obj_coin.actualizar_en_pantalla(lista_coins,ventana_principal,player)
        #cada 45 segundos aparece una vida durante 15 segundos
        #y a partir del minuto 1 apareceran manchas de aceite
        if acu_segundos > 45 and acu_segundos < 60:
            obj_vida.avanzar(lista_obj_vida,player)
            obj_vida.actualizar_en_pantalla(lista_obj_vida,ventana_principal,player)
        elif acu_minutos >= 1:
            obj_aceite.avanzar(lista_aceite,player)
            obj_aceite.actualizar_en_pantalla(lista_aceite,ventana_principal,player)

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False
            #contador de tiempo
            if evento.type == pygame.USEREVENT+10:
                if evento.type == contador_segundos:
                    acu_segundos += 1
                    if acu_segundos % 60 == 0:
                        acu_minutos += 1
                        acu_segundos -= 60

                    player.tiempo_jugado = acu_segundos + (acu_minutos * 60)
        
        enemigo.avanzar(lista_enemigo)
        enemigo.actualizar_pantalla(lista_enemigo,ventana_principal,player)
        player.actualizar_pantalla(ventana_principal)
        player.monedas_no_negativas()
        
        texto_en_pantalla.mostrar_tiempo(ventana_principal,acu_minutos,acu_segundos)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.movimiento(-14, "x")
        if keys[pygame.K_d]:
            player.movimiento(14, "x")
        if keys[pygame.K_s]:
            player.movimiento(14, "y")
        if keys[pygame.K_w]:
            player.movimiento(-14, "y")

        if player.vida == 0:
            canal_sonidos.play(sonido_perder)
            mostrar = 3
    #GAME OVER==============================================
    if mostrar == 3:
        musica_en_juego.stop()
        musica_menu.stop()
        musica_game_over.play(-1)

        pygame.draw.rect(ventana_principal, colores.BLACK,(0,0,ANCHO_VENTANA,ALTO_VENTANA))
        try_agine_fondo.mostrar_imagen(ventana_principal)
        try_again_btn.mostrar_imagen(ventana_principal)
        menu_btn.mostrar_imagen(ventana_principal)

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False
            #botones
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if try_again_btn.rectangulo.collidepoint(lista_click) and player.monedas >= 300:
                    canal_sonidos.play(sonido_botones)
                    mostrar = 2
                    player.vida = 1
                    player.monedas -= 300
                elif menu_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = 0
                else:
                    pass
    #INFORMACION
    if mostrar == 4:
        musica_en_juego.play(-1)
        info_img.mostrar_imagen(ventana_principal)
        menu_btn.mostrar_imagen(ventana_principal)

        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                run = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if menu_btn.rectangulo.collidepoint(lista_click):
                    canal_sonidos.play(sonido_botones)
                    mostrar = 0
                
    reloj.tick(FPS)
    pygame.display.flip()
    pygame.mixer.music.stop()

pygame.quit()
'''