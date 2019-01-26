# Ejercicio 4
# Autor: Joaquin Diaz
# Fecha: 26 de Enero 2019




nom1 = input("Escribe el nombre 1: ")
apellido1 = input("Escribe el Apellido 1: ")
inicial1 = input("Escribe la Inicial 1: ")
nom2 = input("Escribe el nombre 2: ")
apellido2 = input("Escribe el Apellido 2: ")
inicial2 = input("Escribe la Inicial 2: ")
nom3 = input("Escribe el nombre 3: ")
apellido3 = input("Escribe el Apellido 3: ")
inicial3 = input("Escribe la Inicial 3: ")

tupla = [(apellido1, nom1 ,inicial1), (apellido2,nom2 ,inicial2), (apellido2,nom3,inicial2)]

input("Pulsa lo que sea para invertir de orden la list")

tupla = [(nom1, inicial1+".",apellido1), (nom2, inicial2+".",apellido2), (nom3, inicial3+".",apellido3)]
print(tupla)