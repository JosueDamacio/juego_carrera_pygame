'''
cursor = conexion.execute("SELECT * FROM jugadores ORDER BY puntaje DESC")
for usuario in cursor:
    print(usuario) # va a mil por hora
    font_nombre_jugadores = pygame.font.SysFont("Arial",30)
    txt_nombre_jugadores = font_nombre_jugadores.render("{0}".format(usuario[1]),True,colores.GRAY11)
    ventana_principal.blit(txt_nombre_jugadores,(jugadores_left*2,jugadores_top + (2 * 25)))

    font_puntaje_jugadores = pygame.font.SysFont("Arial",30)
    txt_puntaje_jugadores = font_puntaje_jugadores.render("{0}".format(usuario[3]),True,colores.GRAY11)
    ventana_principal.blit(txt_puntaje_jugadores,(400,400))
'''
#SCOREBOARD
'''cursor = conexion.execute("SELECT * FROM jugadores ORDER BY puntaje DESC")
jugadores = cursor.fetchall()
cantidad_jugadores = len(jugadores) -70
#print(cantidad_jugadores)

for usuario in jugadores:
    font_nombre_jugadores = pygame.font.SysFont("Arial", 30)
    txt_nombre_jugadores = font_nombre_jugadores.render("{0}".format(usuario[1]), True, colores.WHITE)
    ventana_principal.blit(txt_nombre_jugadores, (jugadores_left * 2, jugadores_top + (cantidad_jugadores * 25)))

    font_puntaje_jugadores = pygame.font.SysFont("Arial", 30)
    txt_puntaje_jugadores = font_puntaje_jugadores.render("{0}".format(usuario[3]), True, colores.WHITE)
    ventana_principal.blit(txt_puntaje_jugadores,(400,400))'''

"""BASES A SEGUIR

crear un nuevo jugador al hacer click en login 

in game se ira guardando el puntaje y demas en los atributos

conseguir y guardar el id del usuario

hacer el update del usuario recien creado (al ir del game over al menú)
y ahí guardar los atributos de player en su orden correspondiente

select para ordenar y luego blitear en pantalla

"""

"""

"""