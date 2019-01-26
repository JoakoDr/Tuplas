# Ejercicio 3
# Autor: Joaquin Diaz
# Fecha: 26 de Enero 2019


import os


def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    print("Selecciona una opción")
    print("\t1 - Estimado tuplas")
    print("\t2 - Origen y n")
    print("\t3 - Modificar")
    print("\t9 - salir")


while True:
    # Mostramos el menu
    menu()

    # solicituamos una opción al usuario
    opcionMenu = input("Inserta una opcion :")

    if opcionMenu == "1":
        nom1 = input("Escribe el nombre 1: ")
        nom2 = input("Escribe el nombre 2: ")
        nom3 = input("Escribe el nombre 3: ")
        tupla = [nom1,nom2,nom3]
        nombre1 = tupla[0]
        print("Estimado "+nombre1+",vote por mi")
        nombre2 = tupla[1]
        print("Estimado " + nombre2 + ",vote por mi")
        nombre3 = tupla[2]
        print("Estimado " + nombre3 + ",vote por mi")
    elif opcionMenu == "2":
        nom1 = input("Escribe el nombre 1: ")
        nom2 = input("Escribe el nombre 2: ")
        nom3 = input("Escribe el nombre 3: ")
        tupla = [nom1, nom2, nom3]
        print(tupla)
        origen = input("Origen: ")
        elemtupl=tupla[int(origen)]
        destino = input("Nº de repeticiones: ")
        for i in range(int(destino)):
             print(elemtupl)

    elif opcionMenu == "3":
        nom1 = input("Escribe el nombre 1: ")
        genero1 = input("Escribe el genero 1: ")
        nom2 = input("Escribe el nombre 2: ")
        genero2 = input("Escribe el genero 2: ")
        nom3 = input("Escribe el nombre 3: ")
        genero3 = input("Escribe el genero 3: ")
        tupla = [(nom1, genero1), (nom2,genero2), (nom3,genero3)]
        origen = input("Origen: ")
        elemtupl = tupla[int(origen)]
        destino = input("Nº de repeticiones: ")
        for i in range(int(destino)):
            print(elemtupl)
        print(tupla)


    elif opcionMenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")