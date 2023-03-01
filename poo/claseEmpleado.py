class empleado:
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getCargo(self):
        return self.__cargo
    def setCargo(self,cargo):
        self.__cargo=cargo

    def getSalario(self):
        return self.__salario
    def setSalario(self,salario):
        self.__salario=salario

    def calSalarioIPC(self, salario):
        if salario>1160000 and salario<0:
            salario_con_ipc = (salario*0.133)+salario
            return salario_con_ipc     
        else:
            salario_con_ipc = (salario*0.163)+salario  
            return salario_con_ipc
    
    def calSalarioHE(self, HE, salario):
        if HE<11 and HE>0 and salario>0:
            salario_con_HE = (HE*6042)+salario
            return salario_con_HE     
        else:
            print('La empresa no permite trabajar mas de 10 horas')

    def cantEmpleados(self):
        return empleado().count(self.__nombre)

emp1=empleado('Santiago','cantante',1600000)
print(emp1.salario)
print(emp1.calSalarioHE(5, 16000000))
