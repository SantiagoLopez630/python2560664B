class Persona: #se crea clase persona, que funciona parecido a una función
    def __init__(self,nombre): #se crea el el metodo constructor siempre va a pasar por ahí cada vez que se ejecuta el codigo para declarar el constructor se pone el init y el self, posteriormente se le pone un atributo nombre a la clase
        self.__nombre=nombre #el atributo nombre se va a guardar en la variable nombre 
        print('Activando constructor') #imprime activando constructor en pantalla

    def getNombre(self): #se crea el metodo get que traera los datos de la clase
        return self.__nombre # pide que retorne el nombre y '__' nos sirve para indicar es de tipo privado
    
    def setNombre(self, nombre): #se crea el metodo set que cambiara los datos de la clase y pide el nuevo dato que se cambiara en este caso nombre
        self.__nombre=nombre # el atributo nombre se va a guardar en la variable nombre 

    def metodo(self): #es crea un metodo self para indicar que es un metodo de la clase
        print('Soy un método') #imprime una cadena

class Aprendiz(Persona):
    def __init__(self,nombre,documento,ficha):
        Persona.__init__(self,nombre,documento)
        self.__ficha=ficha
    def getFicha(self):
        return self.__ficha
    def completo(self):
        print(self.getNombre())
        print(self.getdocumento())
        print(self.getFicha())
        return " "


apre=Aprendiz('Santiago',1025523127,2560664)
print(apre.completo())
ob=Persona('Ana') #llama la clase y le asigna el atributo un dato y todo eso lo guarda en una variable 
print(ob.getNombre()) #imripime la variable y llama el metodo get de la clase para traer el nombre
ob.setNombre('Maria') #llama la clase y el atributo le cambia el valor del dato y todo eso lo guarda en una variable 
print(ob.getNombre()) #imprime la variable y llama el metodo get de la clase para traer el nombre
#ob.metodo() 
#print(type(ob)) # muestra el tipo de dato de la variable ob