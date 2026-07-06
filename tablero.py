

def cargar_nivel(numero):
    # Carga el tablero correspondiente al nivel seleccionado
    if numero == 1:
        # Diseño del nivel 1
        diseno = [
            "########",
            "#AB CFG#",
            "#AB CFG#",
            "#XX CFG ",
            "# EEE  #",
            "#DD    #",
            "#      #",
            "########",
        ]
    elif numero == 2:
        # Diseño del nivel 2
        diseno = [
            "######",
            "#A   #",
            "#A P #",
            "#XXPB ",
            "#   B#",
            "######",
        ]
    else:
        # Si el nivel no existe, se crea un tablero vacio
        diseno = []

    # Convierte cada fila del diseño en una lista de caracteres
    tablero = []
    for fila in diseno:
        tablero.append(list(fila))

    # Devuelve el tablero listo para ser utilizado
    return tablero


def mostrar_tablero(tablero):
    # Recorre cada fila del tablero y la muestra en pantalla
    for fila in tablero:
        # Une los caracteres de la fila para imprimirla como una sola linea
        print("".join(fila))

    # Deja una linea en blanco para mejorar la visualizacion
    print()


def buscar_vehiculo(tablero, letra):
    # Busca todas las posiciones donde se encuentra el vehiculo indicado
    celdas = []

    # Recorre todas las filas y columnas del tablero
    for f in range(len(tablero)):
        for c in range(len(tablero[f])):

            # Si encuentra la letra del vehiculo, guarda su posicion
            if tablero[f][c] == letra:
                celdas.append((f, c))

    # Devuelve la lista con las posiciones del vehiculo
    return celdas


def es_horizontal(celdas):
    # Verifica si el vehiculo esta colocado de forma horizontal
    primera_fila = celdas[0][0]

    # Compara la fila de cada celda con la primera
    for (f, c) in celdas:
        if f != primera_fila:
            return False

    # Si todas las celdas estan en la misma fila, es horizontal
    return True


def mover_un_paso(tablero, letra, direccion):
    # Busca la posicion actual del vehiculo que se desea mover
    celdas = buscar_vehiculo(tablero, letra)

    # Si el vehiculo no existe, el movimiento no se puede realizar
    if len(celdas) == 0:
        return False 

    # Define el desplazamiento segun la direccion elegida
    if direccion == "U":
        df, dc = -1, 0
    elif direccion == "D":
        df, dc = 1, 0
    elif direccion == "L":
        df, dc = 0, -1
    elif direccion == "R":
        df, dc = 0, 1
    else:
        return False

    # Evita mover un vehiculo horizontal en direccion vertical
    if es_horizontal(celdas) and (direccion == "U" or direccion == "D"):
        return False

    # Evita mover un vehiculo vertical en direccion horizontal
    if (not es_horizontal(celdas)) and (direccion == "L" or direccion == "R"):
        return False

    # Calcula las nuevas posiciones que tendra el vehiculo
    nuevas = []
    for (f, c) in celdas:
        nuevas.append((f + df, c + dc))

    # Verifica que las nuevas posiciones sean validas
    for (f, c) in nuevas:
        if f < 0 or f >= len(tablero):
            return False
        if c < 0 or c >= len(tablero[f]):
            return False

        # Comprueba que el espacio este libre o pertenezca al mismo vehiculo
        contenido = tablero[f][c]
        if contenido != " " and contenido != letra:
            return False

    # Borra la posicion anterior del vehiculo
    for (f, c) in celdas:
        tablero[f][c] = " "

    # Coloca el vehiculo en su nueva posicion
    for (f, c) in nuevas:
        tablero[f][c] = letra

    # Indica que el movimiento fue realizado correctamente
    return True


def mover_vehiculo(tablero, letra, direccion, cantidad):
    # Mueve un vehiculo la cantidad de espacios indicada
    movidos = 0

    # Si se eligio "todos", mueve el vehiculo hasta que ya no pueda avanzar
    if cantidad == "todos":
        while mover_un_paso(tablero, letra, direccion):
            movidos = movidos + 1
    else:
        # Mueve el vehiculo la cantidad de veces indicada por el usuario
        for i in range(cantidad):
            if mover_un_paso(tablero, letra, direccion):
                movidos = movidos + 1
            else:
                # Si ya no puede moverse, termina el ciclo
                break

    # Devuelve la cantidad de movimientos realizados
    return movidos

def hay_victoria(tablero):
    # Verifica si el auto principal (X) llego a la salida
    celdas = buscar_vehiculo(tablero, "X")

    # Obtiene la ultima columna del tablero
    ultima_columna = len(tablero[0]) - 1

    # Revisa si alguna parte del auto X llego a la salida
    for (f, c) in celdas:
        if c == ultima_columna:
            return True

    # Si no llego a la salida, el juego continua
    return False


def nombre_direccion(direccion):
    # Convierte la letra de la direccion en un texto entendible
    if direccion == "U":
        return "arriba"
    if direccion == "D":
        return "abajo"
    if direccion == "L":
        return "la izquierda"
    if direccion == "R":
        return "la derecha"

    # Si la direccion no es valida, devuelve una cadena vacia
    return ""


def obtener_solucion(nivel):
    # Devuelve la secuencia de movimientos para resolver cada nivel
    if nivel == 1:
        # Solucion predefinida para el nivel 1
        return [("E", "L", 1), ("C", "D", 3), ("F", "D", 3),
                ("G", "D", 3), ("X", "R", "todos")]

    if nivel == 2:
        # Solucion predefinida para el nivel 2
        return [("P", "U", 1), ("B", "U", 2), ("X", "R", "todos")]

    # Si el nivel no existe, devuelve una lista vacia
    return []
