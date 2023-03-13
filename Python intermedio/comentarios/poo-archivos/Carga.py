from Vehiculo import * # Del modulo vehiculo se importa todo representao con el *
class Carga(Vehiculo): # se crea la clase carga que trae por herencia a la clase vehiculo que se importa por el modulo
    def __init__(self,placa,conductor,capacidad,ejes): #Se define el constructor de la clase carga con sus respectivos atributos
        Vehiculo.__init__(self,placa,conductor) # se trae por herencia los atributos del constructor de la clase vehiculo
        self.__capacidad=capacidad #se guarda el valor del atributo capacidad que se instancia a traves de un objeto 
        self.__ejes=ejes #se guarda el valor del atributo ejes que se instancia a traves de un objeto
    def getCapacidad(self): #Se crea el metodo getCapacidad que retornara el valor de capacidad
        return self.__capacidad #retorna el valor de capacidad
    def getEjes(self): #Se crea el metodo getEjes que retornara el valor de ejes
        return self.__ejes #retorna el valor de ejes