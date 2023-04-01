import sqlite3 # se importa el modulo de sqlite3
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db') #se instancia el objeto "con" que traera el metodo connect que a su vez traerá como parametro una ruta absoluta
con=sqlite3.connect('sqlitepython/conpython.db') #se instancia el objeto "con" que traera el metodo connect que a su vez traerá como parametro una ruta relativa
print(type(con)) # imprime el tipo de dato del objeto con
micursor=con.cursor() #Se instancia un objeto "micursor" que será igual a la intancia del objeto con con el metodo de cursor (que permite leer las sentcias SQL)
print(type(micursor)) # imprime el tipo de dato del objeto con
sentencia="SELECT * from alumno;" #Se crea la variable sentencia con la consulta SQL que traera todo de la tabla alumno 

micursor.execute(sentencia) #se ejecuta la base de datos guardada en mi cursor pasandole como parametro la sentencia que traera la tabla
for fila in micursor.fetchall(): # se itera las filas de la tabla y se utiliza el fetchall para traer todos los elementos
    print(fila[0]) #se imprime el valor de la fila en la pocision 0
    print(fila[1]) #se imprime el valor de la fila en la pocision 1
    print(fila[2]) #se imprime el valor de la fila en la pocision 2
    print(fila[3]) #se imprime el valor de la fila en la pocision 3
    print('-'*50) #Se imprime un guion 50 veces