from Carga import * # Del modulo cargar se importa todo representao con el *
from Conductor import * # Del modulo cargar se importa todo representao con el *
# c1=Conductor('Luis',12345) #Se instancia un objeto c1 que llama la clase conductor importada a traves del modulo y la pasa paramaetros
# carga1=Carga('aaa-123',c1,5,2) #Se instancia un objeto carga1 que llama la clase carga importada a traves del modulo y la pasa paramaetros
# print(carga1) #se imprime el objeto carga 1
nomConductor=input('Ingrese nombre del conductor') #se pide una entrada por teclado al usuario a traves del input y se guarda en nomConductor
docConductor=int(input('Ingrese documento del conductor')) #se pide una entrada por teclado al usuario a traves del input, se convierte en entero y se guarda en domConductor
placa=input('ingrese placa') ##se pide una entrada por teclado al usuario a traves del input y se guarda en nomConductorse pide una entrada por teclado al usuario a traves del input y se guarda en placa
capacidad=input('ingrese capacidad en toneladas') #se pide una entrada por teclado al usuario a traves del input y se guarda en capacidad
ejes=input('ingrese numero de ejes') #se pide una entrada por teclado al usuario a traves del input y se guarda en ejes
c1=Conductor(nomConductor,docConductor) #Se instancia un objeto c1 que llama la clase conductor importada a traves del modulo y la pasa parametros de las variables que guardamos anteriormente
obCarga=Carga(placa,c1,capacidad,ejes) #Se instancia un objeto obCarga que llama la clase carga importada a traves del modulo y la pasa parametros
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento()) #Se crea una variable cadConductor el cual instancia el objeto obCarga y le pide traer el metodo getConductor getNombre que traera el nombre del conductor, luego se concatena con la comma con la conversion a string del objeto obCarga y le pide traer el metodo getConductor getDocumento que traera el documento del conductor

cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes()) #Se crea una variable cadCarga el cual instancia el objeto obCarga y le pide traer el metodo getPlaca que traera la placa del vehiculo, luego se concatena con la comma con cadConductor, y por ultimo se concatena la conversion a string del objeto obCarga y le pide traer el metodo getConductor getCapacidad que traera capacidad y getEjes que traera el numero de ejes 

with open('poo-archivos/listado.txt','a') as flujo: #La palabra reservada with sirve para manejar archivos dentro de un bloque de codigo que se encuentra identado dentro de esta, con la función open se abre el archivo listado, y la 'a' expresa que sera actualizado y todo esto sera guardado con la palabra flujo
    flujo.write(cadCarga+'\n') #la variable flujo se que contine el archivo se le llama el metodo write que va imprimir cadCarga con un salto de linea al final de este