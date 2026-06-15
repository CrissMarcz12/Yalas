

def cargar_nivel(numero):
    if numero == 1:
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
        diseno = [
            "######",
            "#A   #",
            "#A P #",
            "#XXPB ",
            "#   B#",
            "######",
        ]
    else:
        diseno = []

    tablero = []
    for fila in diseno:
        tablero.append(list(fila))
    return tablero


def mostrar_tablero(tablero):
    for fila in tablero:
        print("".join(fila))
    print()


def buscar_vehiculo(tablero, letra):
    celdas = []
    for f in range(len(tablero)):
        for c in range(len(tablero[f])):
            if tablero[f][c] == letra:
                celdas.append((f, c))
    return celdas


def es_horizontal(celdas):
    primera_fila = celdas[0][0]
    for (f, c) in celdas:
        if f != primera_fila:
            return False
    return True


def mover_un_paso(tablero, letra, direccion):
    celdas = buscar_vehiculo(tablero, letra)
    if len(celdas) == 0:
        return False 

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

    if es_horizontal(celdas) and (direccion == "U" or direccion == "D"):
        return False
    if (not es_horizontal(celdas)) and (direccion == "L" or direccion == "R"):
        return False

    nuevas = []
    for (f, c) in celdas:
        nuevas.append((f + df, c + dc))

    for (f, c) in nuevas:
        if f < 0 or f >= len(tablero):
            return False
        if c < 0 or c >= len(tablero[f]):
            return False
        contenido = tablero[f][c]
        if contenido != " " and contenido != letra:
            return False

    for (f, c) in celdas:
        tablero[f][c] = " "
    for (f, c) in nuevas:
        tablero[f][c] = letra
    return True


def mover_vehiculo(tablero, letra, direccion, cantidad):
    movidos = 0
    if cantidad == "todos":
        while mover_un_paso(tablero, letra, direccion):
            movidos = movidos + 1
    else:
        for i in range(cantidad):
            if mover_un_paso(tablero, letra, direccion):
                movidos = movidos + 1
            else:
                break
    return movidos


def hay_victoria(tablero):
    celdas = buscar_vehiculo(tablero, "X")
    ultima_columna = len(tablero[0]) - 1
    for (f, c) in celdas:
        if c == ultima_columna:
            return True
    return False


def nombre_direccion(direccion):
    if direccion == "U":
        return "arriba"
    if direccion == "D":
        return "abajo"
    if direccion == "L":
        return "la izquierda"
    if direccion == "R":
        return "la derecha"
    return ""


def obtener_solucion(nivel):
    if nivel == 1:
        return [("E", "L", 1), ("C", "D", 3), ("F", "D", 3),
                ("G", "D", 3), ("X", "R", "todos")]
    if nivel == 2:
        return [("P", "U", 1), ("B", "U", 2), ("X", "R", "todos")]
    return []
