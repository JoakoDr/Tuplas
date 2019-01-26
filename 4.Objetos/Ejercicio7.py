# Ejercicio 7
# Autor: Joaquin Diaz
# Fecha: 26 de Enero 2019


class Corcho(object):
    bodega = "Juan"
    def __init__(self,bodega):
        self.bodega = bodega

    def getNombre(self):
        return  self.bodega

    def __str__(self):
        return "%s" %(self.bodega)



class Botella(Corcho):

    def __init__(self,corcho,nombre):
        self.corcho = corcho
        self.nombre = nombre

    def getNombre(self):
        return  self.nombre

    def __str__(self):
        return "%s" %(self.corcho.bodega)



class Sacacorchos(Botella):
    nombre = "Lucas"

    def __init__(self,corcho,botella,nombre):
        self.corcho = corcho
        self.botella = botella
        self.nombre = nombre

    def getNombre(self):
        return  self.corcho
    def getBotella(self):
        return self.botella
    def destapar(self,corcho,botella):
        print("El corcho "+ corcho.__str__()+" destapa la botella "+botella.getNombre()+" gracias a "+self.__str__())
    def limpiar(self,corcho):
        print("El corcho " + corcho.__str__() +" sale del sacacorchos "+self.__str__())

    def __str__(self):
        return "%s" %(self.nombre)



corcho = Corcho("Rueda")
botella = Botella(corcho,"Vino Blanco")
sacacorchos = Sacacorchos(corcho,botella,"Laura")

sacacorchos.destapar(corcho,botella)
sacacorchos.limpiar(corcho)