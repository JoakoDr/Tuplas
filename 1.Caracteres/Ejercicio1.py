# Ejercicio 1
# Autor: Joaquin Diaz
# Fecha: 26 de Enero 2019


import os


def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Introducir caracter en cadena.")
    print("\t2 - Reemplazar espacios por caracter")
    print("\t3 - Digitos por caracter")
    print("\t4 - Inserta caracter cada tres digitos")
    print("\t9 - salir")


while True:
    # Mostramos el menu
    menu()

    # solicituamos una opción al usuario
    opcionMenu = input("Inserta una opcion :")

    if opcionMenu == "1":

        cadena = input("Cadena:")
        caracter = input("Carácter:")
        print(caracter.join(cadena))
    elif opcionMenu == "2":
        cad = input("Cadena:")
        caracter = input("Caracter:")
        print(cad.replace(" ", caracter))

    elif opcionMenu == "3":
        cadena = input("Cadena:")
        caracter = input("Carácter:")
        for i in range(10):
            cadena = cadena.replace(str(i), caracter)
        print(cadena)
    elif opcionMenu == "4":
        cad = input("Número:")
        car = input("Caracter:")
        cont = 0
        cad2 = ""
        for c in cad:
            if cont != 0 and cont % 3 == 0:
                cad2 = cad2 + car
            cad2 = cad2 + c
            cont = cont + 1
        print(cad2)
    elif opcionMenu == "9":
        print("Adios!!!")
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")