# Ejercicio 2
# Autor: Joaquin Diaz
# Fecha: 26 de Enero 2019


import os


def menu():
    #Limpia la pantalla y muestra el menu
    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Encontrar cadena en subacdena")
    print("\t2 - Ordenar por orden alfabetico dos strings")
    print("\t9 - salir")


while True:
    # Mostramos el menu
    menu()

    # solicituamos una opción al usuario
    opcionMenu = input("Inserta una opcion :")

    if opcionMenu == "1":
        cadena1 = input("1º Cadena:")
        cadena2 = input("2º Cadena:")
        if cadena1.find(cadena2)> -1 :
            print("La 1 cadena contiene la segunda cadena")
        else:
            print("La cadena 1 no contiene la 2")
        if cadena2.find(cadena1) > -1 :
            print("La cadena 2 contiene la 1")
        elif cadena2.find(cadena1) == -1:
            print("La cadena 2 no contiene la 1")
    elif opcionMenu == "2":
        cadena1 = input("1º Palabra:")
        cadena2 = input("2º Palabra:")
        cadenas = [cadena1,cadena2]
        cadenas.sort()
        print(cadenas)

    elif opcionMenu == "9":
        print("Adios")
        break
    else:

        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")