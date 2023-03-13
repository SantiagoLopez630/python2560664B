class Vehiculo: #Se define al clase vehiculo
    def __init__(self,placa,conductor): #Se define el metodo constructotr con sus respectivos atributos
        self.__placa=placa #se guarda el valor del atributo placa que se instancia a traves de un objeto
        self.__conductor=conductor #se guarda el valor del atributo conductor que se instancia a traves de un objeto
    def getConductor(self): #Se crea el metodo getConductor que retornara el valor del nombre del conductor 
        return self.__conductor #se guarda el valor del atributo conductor que se instancia a traves de un objeto
    def getPlaca(self): #Se crea el metodo getPlaca que retornara el valor de la placa 
        return self.__placa #se guarda el valor del atributo placa que se instancia a traves de un objeto