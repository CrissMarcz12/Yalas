# main.py
# Archivo principal del juego "Desatasca el Auto".
# Aqui esta el menu y llama a los dos modulos: tablero e historial.

import tablero
import historial


def mostrar_menu():
    # Muestra el menu principal del juego
    print("===== DESATASCA EL AUTO - MENU PRINCIPAL =====")
    print("Libera el auto X moviendo los demas vehiculos.")
    print("Usa las letras para seleccionar un vehiculo.")
    print("Direcciones: U=Arriba, D=Abajo, L=Izquierda, R=Derecha.")
    print("Escribe SALIR en cualquier momento para abandonar la partida.")
    print("----------------------------------------------")
    print("1. Iniciar nuevo juego")
    print("2. Resolver automaticamente")
    print("3. Ver historial de juegos")
    print("4. Salir")
    print("==============================================")


def leer_opcion():
    # Lee la opcion que ingresa el usuario y verifica que sea valida
    while True:
        entrada = input("Ingrese una opcion: ")

        # isdigit() verifica que solo se hayan ingresado numeros
        if entrada.isdigit():
            numero = int(entrada)

            # Solo se aceptan numeros enteros positivos
            if numero >= 1:
                return numero

        # Si el dato no es valido, se vuelve a pedir
        print("Opcion invalida, ingrese un numero valido.")


def juego_manual(partidas):
    # Ejecuta el modo manual, donde el jugador resuelve los niveles
    nombre = input("Ingrese su nombre: ")
    total_movimientos = 0
    nivel = 1
    abandono = False

    # Se juegan los dos niveles de manera consecutiva
    while nivel <= 2:
        print("Cargando nivel", nivel, "...")
        cochera = tablero.cargar_nivel(nivel)
        completado = False

        # El ciclo continua hasta completar el nivel
        while not completado:
            tablero.mostrar_tablero(cochera)

            # Se pide el auto que el usuario desea mover
            letra = input("Seleccione auto (o escriba SALIR para abandonar): ").upper()
            if letra == "SALIR":
                abandono = True
                break

            # Validamos que el auto exista en el tablero
            if len(tablero.buscar_vehiculo(cochera, letra)) == 0:
                print("Ese auto no existe, intente de nuevo.")
                continue

            # Se solicita la direccion del movimiento
            direccion = input("Mover (U/D/L/R): ").upper()

            # Se verifica que la direccion ingresada sea valida
            if direccion != "U" and direccion != "D" and direccion != "L" and direccion != "R":
                print("Direccion invalida.")
                continue

            # Se pide la cantidad de espacios que se movera el vehiculo
            espacios = input("Mover cuantos espacios (1/2/todos): ").strip().lower()

            # Si escribe "todos", el auto avanzara hasta donde sea posible
            if espacios == "todos":
                cantidad = "todos"
            elif espacios.isdigit() and int(espacios) >= 1:
                cantidad = int(espacios)
            else:
                print("Cantidad invalida.")
                continue

            # Se intenta mover el vehiculo
            movidos = tablero.mover_vehiculo(cochera, letra, direccion, cantidad)

            # Si no se movio, el movimiento no era valido
            if movidos == 0:
                print("Movimiento invalido, ese auto no se puede mover ahi.")
            else:
                # Se cuenta un movimiento realizado por el jugador
                total_movimientos = total_movimientos + 1

                # Se verifica si el auto principal ya llego a la salida
                if tablero.hay_victoria(cochera):
                    tablero.mostrar_tablero(cochera)
                    print("Auto liberado. Nivel", nivel, "completado!")
                    completado = True

        # Si el jugador abandono, termina el juego
        if abandono:
            break

        # Pasa al siguiente nivel
        nivel = nivel + 1

    # Guardamos el resultado de la partida en el historial
    if abandono:
        historial.agregar_partida(partidas, nombre, nivel, total_movimientos, "Manual", "Abandono")
        print("Abandonaste la partida.")
    else:
        historial.agregar_partida(partidas, nombre, 2, total_movimientos, "Manual", "Gano")
        print("Felicidades", nombre + "! Completaste los dos niveles.")
    print()

def juego_automatico(partidas):
    # Ejecuta el modo automatico, donde el programa resuelve los niveles
    # utilizando una secuencia de movimientos ya definida
    nombre = input("Ingrese su nombre: ")
    total_movimientos = 0

    # Recorre los dos niveles del juego
    for nivel in (1, 2):
        print("Cargando nivel", nivel, "...")
        cochera = tablero.cargar_nivel(nivel)

        # Muestra el tablero inicial
        tablero.mostrar_tablero(cochera)
        print("Resolviendo automaticamente...")

        # Obtiene la lista de movimientos para resolver el nivel
        solucion = tablero.obtener_solucion(nivel)
        numero = 1

        # Ejecuta cada movimiento de la solucion
        for (letra, direccion, cantidad) in solucion:
            tablero.mover_vehiculo(cochera, letra, direccion, cantidad)
            total_movimientos = total_movimientos + 1

            # Muestra el movimiento realizado y el estado actualizado del tablero
            print("Movimiento", numero, ": mover", letra, "hacia", tablero.nombre_direccion(direccion))
            tablero.mostrar_tablero(cochera)
            numero = numero + 1

        # Indica que el nivel fue completado
        print("Auto liberado. Nivel", nivel, "completado!")
        print()

    # Guarda la partida resuelta automaticamente en el historial
    historial.agregar_partida(partidas, nombre, 2, total_movimientos, "Automatico", "Gano")
    print("El juego fue resuelto automaticamente.")
    print()


def main():
    # Lista donde se almacenan las partidas durante la ejecucion del programa
    partidas = []   # el historial se guarda en memoria mientras corre el programa

    # El menu se repite hasta que el usuario decida salir
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        # Ejecuta la opcion seleccionada por el usuario
        if opcion == 1:
            juego_manual(partidas)
        elif opcion == 2:
            juego_automatico(partidas)
        elif opcion == 3:
            historial.mostrar_historial(partidas)
        elif opcion == 4:
            print("Saliendo del juego. Hasta luego!")
            break
        else:
            # Se muestra si la opcion ingresada no existe en el menu
            print("Esa opcion no existe en el menu.")


# Inicia la ejecucion del programa
main()
