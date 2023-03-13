class Curso: #se crea clase Curso, que funciona parecido a una función
    def __init__(self,titulo): #se crea el el metodo constructor siempre va a pasar por ahí cada vez que se instancia una objeto, para declarar el constructor se pone el init y el self, posteriormente se le pone un atributo titulo
        self.__titulo=titulo # se recibe el valor de titulo a traves del contructor y se guarda 

    def getTitulo(self): #se crea el metodo get que traera los datos de la clase curso, el atributo Titulo
        return self.__titulo # retorna el titulo que se introduccio en el constructor, y '__' nos sirve para indicar es de tipo privado

class Aprendiz: #se crea clase Aprendiz, que funciona parecido a una función
    def __init__(self,nombre): #se crea el el metodo constructor siempre va a pasar por ahí cada vez que se instancia una objeto, para declarar el constructor se pone el init y el self, posteriormente se le pone un atributo NOMBRE
        self.__nombre=nombre #se recibe el valor de nombre a traves del contructor y se guarda, pero nunca se utiliza
        self.__cursos=[] #se recibe el valor de cursos a traves del contructor y se guarda en una lista

    def agregarCurso(self,nombreCursito): #se crea el metodo para agregar curso, tiene como parametros nombreCursito y la palabra reservada self que indica que es de esta clase
        cursito=Curso(nombreCursito) # se instancia un objeto cursito el cual llamara la clase curso con el parametro de nombreCursito que en este caso traera el titulo
        self.__cursos.append(cursito) #se recibe el valor de cursito y se utiliza el metodo append de una lista para añadirlo a la lista cursos

    def getCursos(self): #se crea el metodo get que traera los datos de la clase Aprendiz, la lista cursos
        return self.__cursos #retoran la lista 
    
ap=Aprendiz('Sofia') #se instancia un objeto de la clase Aprendiz y le asigna el parametro 
ap.agregarCurso('Python Basico') #Se llama el metodo agregarCurso con su respectivo parametro a traves del objeto ap
ap.agregarCurso('Python Intermedio') #Se llama el metodo agregarCurso con su respectivo parametro a traves del objeto ap

for c in ap.getCursos(): #Itera la lista que se retorna a traves del metodo get cursos y se imprime
    print(c.getTitulo())

