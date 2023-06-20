import sqlite3

def guardar_progreso (player,conexion):
    player.calcula_score()
    try:
        jugador_datos = (player.nombre, player.final_score)
        conexion.execute("INSERT INTO jugadores (nombre_jugador, puntaje) VALUES (?, ?)", jugador_datos)
        conexion.commit()
        print("Jugador insertado exitosamente")
    except sqlite3.Error as error:
        print("Error al insertar el jugador:", error)