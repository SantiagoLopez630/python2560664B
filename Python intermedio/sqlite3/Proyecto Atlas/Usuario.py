class Usuario:

    def __init__(self,idUsuario,nombreUsuario,apellidoUsuario,rolUsuario,correoUsuario,contraseñaUsuario,numeroDocumentoUsuario,tipoDocumentoUsuario,estadoUsuario):
        self.__idUsuario=idUsuario
        self.__nombreUsuario=nombreUsuario
        self.__apellidoUsuario=apellidoUsuario
        self.__rolUsuario=rolUsuario
        self.__correoUsuario=correoUsuario
        self.__contraseñaUsuario=contraseñaUsuario
        self.__numeroDocumentoUsuario=numeroDocumentoUsuario
        self.__tipoDocumentoUsuario=tipoDocumentoUsuario
        self.__estadoUsuario=estadoUsuario

    def setId(self,idUsuario):
        self.__idUsuario=idUsuario
    
    def getId(self):
        return self.__idUsuario

    
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def getNombre(self):
        return self.__nombre