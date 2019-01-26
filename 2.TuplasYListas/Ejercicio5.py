# Ejercicio 5
# Autor: Joaquin Diaz
# Fecha: 26 de Enero 2019




nom1 = input("Escribe el nombre 1: ")
telefono1 = input("Escribe el telefono 1: ")
nom2 = input("Escribe el nombre 2: ")
telefono2 = input("Escribe el telefono 2: ")
nom3 = input("Escribe el nombre 3: ")
telefono3 = input("Escribe el telefono 3: ")
#Guardo la tupla  que insertas por consola
tupla = [(nom1, telefono1), (nom2, telefono2), (nom3, telefono3)]
print(tupla)
cadena = input("Cadena a buscar:")
if not cadena.find(nom1):
    print(tupla[0])
if not cadena.find(nom2):
        print(tupla[1])
if not cadena.find(nom3):
            print(tupla[2])
