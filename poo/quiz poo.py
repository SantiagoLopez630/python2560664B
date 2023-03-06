class carrera:
    def __init__(self,idCarrera, nom, des, cred, sem, asig):
        self.__idCarrera=idCarrera
        self.__nom=nom
        self.__des=des
        self.__cred=cred
        self.__sem=sem
        self.__asig=asig

    def getCarrera(self):
        return self.__nom, self.__idCarrera, self.__cred, self.__des, self.__sem, self.__asig

class estudiante:
    def __init__(self,idEstudiante, nombre, carrera, correo, tel, metodoPago):

        self.__idEstudiante=idEstudiante
        self.__nombre=nombre
        self.__carrera=carrera
        self.__correo=correo
        self.__tel=tel
        self.__metodoPago=metodoPago

    def getEstudiante(self):
        return self.__idEstudiante, self.__nombre, self.__carrera, self.__correo, self.__tel, self.__metodoPago
    
class instructor:
    def __init__(self,idInstructor, nombre, des, disponibilidad, especialidad):

        self.__idInstructor=idInstructor
        self.__nombre=nombre
        self.__des=des
        self.__disponibilidad=disponibilidad
        self.__especialidad=especialidad

    def getInstructor(self):
        return self.__idInstructor, self.__nombre, self.__des, self.__tel, self.__disponibilidad, self.__especialidad
    
