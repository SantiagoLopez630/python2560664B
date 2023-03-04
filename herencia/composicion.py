class Aprendiz: #se crea clase Aprendiz, que funciona parecido a una función
    def __init__(self,nombre): #se crea el el metodo constructor siempre va a pasar por ahí cada vez que se instancia una objeto, para declarar el constructor se pone el init y el self, posteriormente se le pone un atributo NOMBRE
        self.__nombre=nombre #se recibe el valor de nombre a traves del contructor y se guarda, pero nunca se utiliza
        self.__cursos=[] #se recibe el valor de cursos a traves del contructor y se guarda en una lista

    def agregarCurso(self,titulo): #se crea el metodo para agregar curso, tiene como parametros titulo y la palabra reservada self que indica que es de esta clase
        self.__cursos.append(titulo) #se recibe el valor de titulo y se utiliza el metodo append de una lista para añadirlo a la lista cursos

    def getCursos(self): #se crea el metodo get para traer la lista cursos
        return self.__cursos #Retorna la lista 

class Curso: #se crea clase Curso, que funciona parecido a una función
    def __init__(self,titulo): #se crea el el metodo constructor siempre va a pasar por ahí cada vez que se instancia una objeto, para declarar el constructor se pone el init y el self, posteriormente se le pone un atributo titulo
        self.__titulo=titulo #se recibe el valor de nombre a traves del contructor y se guarda

    def getTitulo(self): #se crea el metodo get para traer el parametro titulo de la clase curso
        return self.__titulo #se retorna el valor de titulo a traves del contructor y se guarda
    
a=Aprendiz('Martha') #se instancia un objeto de la clase Aprendiz y le asigna el parametro
c1=Curso('Python Intermedio') #se instancia un objeto de la clase curso y le asigna el parametro para guardarlo
c2=Curso('Python Basico') #se instancia un objeto de la clase curso y le asigna el parametro
c3=Curso('Introduccion a Java') #se instancia un objeto de la clase curso y le asigna el parametro

a.agregarCurso(c1) #Se llama el metodo agregarCurso con su respectivo parametro a traves del objeto a para añardirlo
a.agregarCurso(c2) #Se llama el metodo agregarCurso con su respectivo parametro a traves del objeto a para añardirlo
a.agregarCurso(c3) #Se llama el metodo agregarCurso con su respectivo parametro a traves del objeto a para añardirlo

print(a.getCursos()) #imprime la lista de los curso a los que esta el aprendiz


for curso in a.getCursos(): #recorre la lista de los cursos del aprendiz y los imprime 
    print(curso.getTitulo())