# Ejercicio 6
# Autor: Joaquin Diaz
# Fecha: 26 de Enero 2019


import sys

def e2(dicc = {}):
    diccionario = {}
    if (len(dicc)):
        diccionario = dicc
    nombre = input("Inserte nombre: ")
    if nombre in diccionario:
            print("Numero actual:",diccionario[nombre])
            val = input("Desea modificarlo? y/n: ")
            if val == "y":
                numero = input( "Inserte nuevo numero: ")
                diccionario[nombre] = numero
                print("Numero actualizado!")
                return e2(diccionario)
            if val == "n":
                return e2(diccionario)
    elif nombre == "*":
        sys.exit()

    else:
            numero = input("Inserte numero: ")
            diccionario.update({nombre : numero})
            print("Agregado a la agenda!")
            return e2(diccionario)

e2()