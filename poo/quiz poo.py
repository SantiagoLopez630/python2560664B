
class registrar:
    def __init__(self,idregistro, nombre, edad, cont, user, password):

        self.__idregistro=idregistro
        self.__nombre=nombre
        self.__edad=edad
        self.__cont=cont
        self.__user=user
        self.__password=password

    def actualizarRegistro(self, idregistro, nombre, edad, cont, user, password):

        self.__idregistro=idregistro
        self.__nombre=nombre
        self.__edad=edad
        self.__cont=cont
        self.__user=user
        self.__password=password        

    def eliminarRegistro(self):
        del self.__idregistro, self.__nombre, self.__edad, self.__cont, self.__user, self.__password

    def consultarRegistro(self):
        return self.__idregistro, self.__nombre, self.__edad, self.__cont, self.__user, self.__password

class estudiante(registrar):
    def __init__(self,idEstudiante, nombre, edad, carrera, correo, tel, metodoPago):
        super().__init__(nombre, edad)

        self.__idEstudiante=idEstudiante
        self.__carrera=carrera
        self.__correo=correo
        self.__tel=tel
        self.__metodoPago=metodoPago

    def actualizarEstudiante(self,idEstudiante, nombre, edad, carrera, correo, tel, metodoPago):
        super().__init__(nombre, edad)

        self.__idEstudiante=idEstudiante
        self.__carrera=carrera
        self.__correo=correo
        self.__tel=tel
        self.__metodoPago=metodoPago
    
    def eliminarEstudiante(self):
        del self.__idEstudiante, self.__nombre, self.__edad, self.__carrera, self.__correo, self.__tel, self.__metodoPago
    def consultarEstudiante(self):
        return self.__idEstudiante, self.__nombre, self.__edad, self.__carrera, self.__correo, self.__tel, self.__metodoPago
             
class instructor(registrar):
    def __init__(self,idInstructor, nombre, edad, correo, des, disp, esp):
        super().__init__(nombre, edad)
        self.__idInstructor=idInstructor
        self.__nombre=nombre
        self.__edad=edad
        self.__correo=correo
        self.__des=des
        self.__disp=disp
        self.__esp=esp

    def actualizarInstructor(self,idInstructor, nombre, edad, correo, des, disp, esp):
        super().__init__(nombre, edad)
        self.__idInstructor=idInstructor
        self.__nombre=nombre
        self.__edad=edad
        self.__correo=correo
        self.__des=des
        self.__disp=disp
        self.__esp=esp

    def eliminarInstructor(self):
        del self.__idInstructor, self.__nombre, self.__edad, self.__correo, self.__des, self.__tel, self.__disp, self.__esp
    def consultarInstructor(self):
        return self.__idInstructor, self.__nombre, self.__edad, self.__correo, self.__des, self.__tel, self.__disp, self.__esp
        
    
class carrera:
    def __init__(self,idCarrera, nom, des, cred, sem, asig):
        self.__idCarrera=idCarrera
        self.__nom=nom
        self.__des=des
        self.__cred=cred
        self.__sem=sem
        self.__asig=asig

    def actualizarCarrera(self, idCarrera, nom, des, cred, sem, asig):
        self.__idCarrera=idCarrera
        self.__nom=nom
        self.__des=des
        self.__cred=cred
        self.__sem=sem
        self.__asig=asig

    def eliminarCarrera(self):
        del self.__idCarrera, self.__nom, self.__des, self.__cred, self.__sem, self.__asig

    def consultarCarrera(self):
        return self.__nom, self.__idCarrera, self.__cred, self.__des, self.__sem, self.__asig

class inscripcion:
    def __init__(self,idInscripcion, fechains, fechaini, fechafin):

        self.__idInscripcion=idInscripcion
        self.__fechains=fechains
        self.__fechaini=fechaini
        self.__fechafin=fechafin
        self.__datosEstudiante=estudiante.consultarEstudiante()

    def actualizarInscripcion(self, idInscripcion, fechains, fechaini, fechafin):
        self.__idInscripcion=idInscripcion
        self.__fechains=fechains
        self.__fechaini=fechaini
        self.__fechafin=fechafin
        self.__datosEstudiante=estudiante.consultarEstudiante()

    def eliminarInscripcion(self):
        del self.__idInscripcion, self.__fechains, self.__fechaini, self.__fechafin, self.__datosEstudiante

    def consultarInscripcion(self):
        return self.__idInscripcion, self.__fechains, self.__fechaini, self.__fechafin, self.__datosEstudiante



class asignatura:
    def __init__(self,idAsignatura, nombre, des, ins, carrera, salon, dur, horario):

        self.__idAsignatura=idAsignatura
        self.__nombre=nombre
        self.__des=des
        self.__ins=ins
        self.__carrera=carrera
        self.__salon=salon
        self.__dur=dur
        self.__horario=horario

    def actualizarAsignatura(self, idAsignatura, nombre, des, ins, carrera, salon, dur, horario):
        self.__idAsignatura=idAsignatura
        self.__nombre=nombre
        self.__des=des
        self.__ins=ins
        self.__carrera=carrera
        self.__salon=salon
        self.__dur=dur
        self.__horario=horario
        self.__instructor=instructor.consultarRegistro()

    def eliminarAsignatura(self):
        del self.__idAsignatura, self.__nombre, self.__des, self.__ins, self.__carrera, self.__salon, self.__dur, self.__horario, self.__instructor

    def consultarAsignatura(self):
        return self.__idAsignatura, self.__nombre, self.__des, self.__ins, self.__carrera, self.__salon, self.__dur, self.__horario, self.__instructor

class procesarMatricula:
    def __init__(self,idmatricula, fechains, fechaini, fechafin, datosEstudiante):

        self.__idmatricula=idmatricula
        self.__fechains=fechains
        self.__fechaini=fechaini
        self.__fechafin=fechafin
        self.__datosEstudiante=datosEstudiante

    def getMatricula(self):
        return self.__idmatricula, self.__fechains, self.__fechaini, self.__fechafin, self.__datosEstudiante
    
    def procesarPago(self):
        return estudiante.consultarEstudiante()
    
ob1=registrar(1025523127, 'daniel', 23, 3153458097, 'danielfelipe90', 'holaQuerty123#')
print(ob1.consultarRegistro())
ob2=estudiante(1025523127, '', '','derecho', 'dafel@gmail.com', 3153458097, 'efectivo' )
print(ob2.consultarEstudiante())