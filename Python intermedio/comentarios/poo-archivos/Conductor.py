class Conductor: #Se define al clase conductor 
    def __init__(self,nombre,documento): #Se crea el metodo constructor de la clasde con sus respectivos atributos
        self.__nombre=nombre #se guarda el valor del atributo nombre que se instancia a traves de un objeto
        self.__documento=documento #se guarda el valor del atributo documento que se instancia a traves de un objeto

    def getNombre(self): #Se crea el metodo getNombre que retornara el valor del nombre
        return self.__nombre # retorna el valor de nombre 
    def getDocumento(self): #Se crea el metodo getDocumento que retornara el valor del documento
        return self.__documento # Retorna el valor del documento 
        