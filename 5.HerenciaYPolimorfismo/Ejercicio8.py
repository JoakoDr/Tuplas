# Ejercicio 8
# Autor: Joaquin Diaz
# Fecha: 26 de Enero 2019


class Personaje(object):
    def __init__(self,vida,posicion,velocidad):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad

    def getVida(self):
        return  "La vida del personaje es %s" % (int(self.vida))
    def recibir_ataque(self,ataque):
        print("El personaje recibe un ataque de 100 HP")
        print(self.vida)
        if ataque > 100:
            self.vida = self.vida - 100
            print("HP del personaje:")
            print(self.vida)
    def mover(self,posicion,velocidad):
        if posicion == 0:
            print("Personaje voviendo a casa %s con una velocidad de %s" % (posicion, velocidad))
        else:
            print("Personaje moviendose a %s con una velocidad de %s" % (posicion,velocidad))


    def __str__(self):
        return "La vida del personaje es %s" %(self.vida)


class Soldado(Personaje):
    def __init__(self,ataque):
        self.ataque = ataque
    def atacar(self,personaje):
        print("El soldado ataca :")
        print(self.ataque)
    def __str__(self):
        return "El ataque del soldado es %s" %(self.ataque)


class Campesino(Personaje):
    def __init__(self, cosecha):
        self.cosecha = cosecha

    def cosechar(self):
        print("La cantidad cosechada por el campesino es %s" % (self.cosecha))

#Creacion de objetos de cada clase
personaje = Personaje(400,0,0)
soldado = Soldado(101)
campesino = Campesino(200)

#Metodos
soldado.atacar(personaje)
personaje.recibir_ataque(soldado.ataque)
personaje.getVida()
campesino.cosechar()
soldado.atacar(personaje)
personaje.recibir_ataque(soldado.ataque)
personaje.mover(10,100)
personaje.mover(0,150)