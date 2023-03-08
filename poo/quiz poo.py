class carrera:
    def __init__(self,idCarrera, nom, des, cred, sem, asig):
        self.__idCarrera=idCarrera
        self.__nom=nom
        self.__des=des
        self.__cred=cred
        self.__sem=sem
        self.__asig=asig

    def consultarCarrera(self):
        return self.__nom, self.__idCarrera, self.__cred, self.__des, self.__sem, self.__asig

    def actualizarCarrera(self):
        while True:
            op=int(input('Ingrese que desea actualizar de la carrera \n 1- id de la carrera \n 2- Nombre \n 3- Descripción \n 4- Creditos \n 5- Semestres \n 6- Asignaturas' ))
            match op :

                    case 1:
                            nue=input('Digite el nuevo id de la carrera: ')
                            self.__idCarrera=nue
                            print('El id de la carrera ha sido actualizado correctamente a: ',nue)

                    case 2:
                            nue=input('Digite el nuevo nombre de la carrera: ')
                            self.__nom=nue
                            print('El nombre de la carrera ha sido actualizado correctamente a: ',nue)

                    case 3:
                            nue=input('Digite la nueva descripción de la carrera: ')
                            self.__des=nue
                            print('La descripción de la carrera ha sido actualizada correctamente a: ',nue)
                    case 4:
                            nue=input('Digite el numero de creditos de la carrera al que desea actualizar: ')
                            self.__cred=nue
                            print('El numero de creditos de la carrera ha sido actualizado correctamente a: ',nue)

                    case 5:
                            nue=input('Digite el numero de semestres de la carrera al que desea actualizar: ')
                            self.__sem=nue
                            print('El numero de semestres de la carrera ha sido actualizado correctamente a: ',nue)
                    case 6:
                            nue=input('Digite el numero de semestres de la carrera al que desea actualizar: ')
                            self.__sem=nue
                            print('El numero de semestres de la carrera ha sido actualizado correctamente a: ',nue)

    def eliminarCarrera(self):
        return self.__nom, self.__idCarrera, self.__cred, self.__des, self.__sem, self.__asig
    
    def crearCarrera(self):
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
    def __init__(self,idInstructor, nombre, des, disp, esp):

        self.__idInstructor=idInstructor
        self.__nombre=nombre
        self.__des=des
        self.__disp=disp
        self.__esp=esp

    def getInstructor(self):
        return self.__idInstructor, self.__nombre, self.__des, self.__tel, self.__disp, self.__esp
    
class asignatura:
    def __init__(self,idInstructor, nombre, des, ins, carrera, salon, dur, horario):

        self.__idInstructor=idInstructor
        self.__nombre=nombre
        self.__des=des
        self.__ins=ins
        self.__carrera=carrera
        self.__salon=salon
        self.__dur=dur
        self.__horario=horario

    def getAsignatura(self):
        return self.__idInstructor, self.__nombre, self.__des, self.__ins, self.__carrera, self.__salon, self.__dur, self.__horario

class inscripcion:
    def __init__(self,idInscripcion, fechains, fechaini, fechafin, datosEstudiante):

        self.__idInscripcion=idInscripcion
        self.__fechains=fechains
        self.__fechaini=fechaini
        self.__fechafin=fechafin
        self.__datosEstudiante=datosEstudiante

    def getInscripcion(self):
        return self.__idInscripcion, self.__fechains, self.__fechaini, self.__fechafin, self.__datosEstudiante
    
class registrar:
    def __init__(self,idregistro, nombre, edad, cont, user, password):

        self.__idregistro=idregistro
        self.__nombre=nombre
        self.__edad=edad
        self.__cont=cont
        self.__user=user
        self.__password=password

    def getRegistro(self):
        return self.__idregistro, self.__nombre, self.__edad, self.__cont, self.__user, self.__password
    
class procesarMatricula:
    def __init__(self,idmatricula, fechains, fechaini, fechafin, datosEstudiante):

        self.__idmatricula=idmatricula
        self.__fechains=fechains
        self.__fechaini=fechaini
        self.__fechafin=fechafin
        self.__datosEstudiante=datosEstudiante

    def getMatricula(self):
        return self.__idmatricula, self.__fechains, self.__fechaini, self.__fechafin, self.__datosEstudiante