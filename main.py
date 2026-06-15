# main.py
# Archivo principal del juego "Desatasca el Auto".
# Aqui esta el menu y llama a los dos modulos: tablero e historial.

import tablero
import historial


def mostrar_menu():
    print("===== DESATASCA EL AUTO - MENU PRINCIPAL =====")
    print("1. Iniciar nuevo juego")
    print("2. Resolver automaticamente")
    print("3. Ver historial de juegos")
    print("4. Salir")
    print("==============================================")


def leer_opcion():
    # lee una opcion del menu y valida que sea un numero entero positivo
    while True:
        entrada = input("Ingrese una opcion: ")
        if entrada.isdigit():            # isdigit solo acepta enteros positivos
            numero = int(entrada)
            if numero >= 1:
                return numero
        print("Opcion invalida, ingrese un numero valido.")


def juego_manual(partidas):
    # modo en el que el jugador mueve los autos por su cuenta
    nombre = input("Ingrese su nombre: ")
    total_movimientos = 0
    nivel = 1
    abandono = False

    while nivel <= 2:
        print("Cargando nivel", nivel, "...")
        cochera = tablero.cargar_nivel(nivel)
        completado = False

        while not completado:
            tablero.mostrar_tablero(cochera)

            letra = input("Seleccione auto (o escriba SALIR para abandonar): ").upper()
            if letra == "SALIR":
                abandono = True
                break

            # validamos que el auto exista en el tablero
            if len(tablero.buscar_vehiculo(cochera, letra)) == 0:
                print("Ese auto no existe, intente de nuevo.")
                continue

            direccion = input("Mover (U/D/L/R): ").upper()
            if direccion != "U" and direccion != "D" and direccion != "L" and direccion != "R":
                print("Direccion invalida.")
                continue

            espacios = input("Mover cuantos espacios (1/2/todos): ").strip().lower()
            if espacios == "todos":
                cantidad = "todos"
            elif espacios.isdigit() and int(espacios) >= 1:
                cantidad = int(espacios)
            else:
                print("Cantidad invalida.")
                continue

            movidos = tablero.mover_vehiculo(cochera, letra, direccion, cantidad)
            if movidos == 0:
                print("Movimiento invalido, ese auto no se puede mover ahi.")
            else:
                total_movimientos = total_movimientos + 1
                if tablero.hay_victoria(cochera):
                    tablero.mostrar_tablero(cochera)
                    print("Auto liberado. Nivel", nivel, "completado!")
                    completado = True

        if abandono:
            break
        nivel = nivel + 1

    # guardamos el resultado de la partida en el historial
    if abandono:
        historial.agregar_partida(partidas, nombre, nivel, total_movimientos, "Manual", "Abandono")
        print("Abandonaste la partida.")
    else:
        historial.agregar_partida(partidas, nombre, 2, total_movimientos, "Manual", "Gano")
        print("Felicidades", nombre + "! Completaste los dos niveles.")
    print()


def juego_automatico(partidas):
    # modo en el que el programa resuelve los niveles solo, paso a paso
    nombre = input("Ingrese su nombre: ")
    total_movimientos = 0

    for nivel in (1, 2):
        print("Cargando nivel", nivel, "...")
        cochera = tablero.cargar_nivel(nivel)
        tablero.mostrar_tablero(cochera)
        print("Resolviendo automaticamente...")

        solucion = tablero.obtener_solucion(nivel)
        numero = 1
        for (letra, direccion, cantidad) in solucion:
            tablero.mover_vehiculo(cochera, letra, direccion, cantidad)
            total_movimientos = total_movimientos + 1
            print("Movimiento", numero, ": mover", letra, "hacia", tablero.nombre_direccion(direccion))
            tablero.mostrar_tablero(cochera)
            numero = numero + 1

        print("Auto liberado. Nivel", nivel, "completado!")
        print()

    historial.agregar_partida(partidas, nombre, 2, total_movimientos, "Automatico", "Gano")
    print("El juego fue resuelto automaticamente.")
    print()


def main():
    partidas = []   # el historial se guarda en memoria mientras corre el programa

    while True:
        mostrar_menu()
        opcion = leer_opcion()

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
            print("Esa opcion no existe en el menu.")


main()
