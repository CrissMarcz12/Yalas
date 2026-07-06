from datetime import datetime


def agregar_partida(partidas, nombre, nivel, movimientos, tipo, resultado):
    # Crea un registro con la informacion de la partida
    partida = {
        "nombre": nombre,

        # Guarda la fecha y hora en que termino la partida
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),

        "nivel": nivel,
        "movimientos": movimientos,
        "tipo": tipo,
        "resultado": resultado,
    }

    # Agrega la partida al historial
    partidas.append(partida)

def mostrar_historial(partidas):
    # Verifica si existen partidas registradas
    if len(partidas) == 0:
        print("Todavia no hay partidas registradas.")
        print()
        return

    # Muestra el encabezado del historial
    print("===== HISTORIAL DE JUEGOS =====")
    print("Nombre".ljust(12), "Fecha y hora".ljust(18), "Nivel".ljust(6),
          "Resultado".ljust(11), "Tipo".ljust(12), "Mov")

    # Recorre todas las partidas y muestra su informacion
    for p in partidas:
        print(str(p["nombre"]).ljust(12),
              str(p["fecha"]).ljust(18),
              str(p["nivel"]).ljust(6),
              str(p["resultado"]).ljust(11),
              str(p["tipo"]).ljust(12),
              str(p["movimientos"]))

    # Deja una linea en blanco al finalizar
    print()
