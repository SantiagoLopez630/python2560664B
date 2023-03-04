class A1: #se crea clase Aprendiz, que funciona parecido a una función
    def __init__(self): #se crea el el metodo constructor siempre va a pasar por ahí cada vez que se instancia una objeto, para declarar el constructor se pone el init y el self
        pass #la palabra reservada pass es un marcador de posición que evita que el programa emita un mensaje de error
    def saludo(self): #se crea el metodo saludo
        print('Hola desde A1') #Se imprime la cadena Hola desde A1

class A2: #Se crea la clase A2
    def __init__(self): #se crea el el metodo constructor siempre va a pasar por ahí cada vez que se instancia una objeto, para declarar el constructor se pone el init y el self
        pass #la palabra reservada pass es un marcador de posición que evita que el programa emita un mensaje de error
    def saludo(self): #se crea el metodo saludo
        print('Hola desde A2') #Se imprime la cadena Hola desde A2


class B(A2,A1): #Se crea la clase A2 la cual es subclase
    def __init__(self): #se crea el el metodo constructor siempre va a pasar por ahí cada vez que se instancia una objeto, para declarar el constructor se pone el init y el self
        pass #la palabra reservada pass es un marcador de posición que evita que el programa emita un mensaje de error
    def saludo(self): #se crea el metodo saludo
        print('Hola desde B') #Se imprime la cadena Hola desde B
    def __str__(self): #el metodo str convierte el objeto para que sea una cadena legible
        return 'Soy un objeto de la clase B' #retorna Soy un objeto de la clase B
obj=B() #Se crea un obj que llama la clase B
print(obj.__str__()) # imprime la cadena que se instancia a traves del objeto a traves del metodo str
#obj.saludo() #se llama el metodo saludo a travs del objeto
#obj.saludo() 


# cad="sena" # cad= sera igual a una cadena
# lista=[1,2,3] #lista sera igual a una lista de 1 al 3
# print(cad.__str__()) #convierte la cadena en str y lo imprime
# print(lista.__str__()) #convierte la cadena en str y lo imprime