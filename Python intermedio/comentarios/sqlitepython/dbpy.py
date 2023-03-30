import sqlite3 # se importa el modulo de sqlite3
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db') #se instancia el objeto "con" que traera el metodo connect que a su vez traerá como parametro una ruta absoluta
con=sqlite3.connect('sqlitepython/conpython.db') #se instancia el objeto "con" que traera el metodo connect que a su vez traerá como parametro una ruta relativa
print(type(con)) # imprime el tipo de dato del objeto con
micursor=con.cursor() #Se instancia un objeto "micursor" que será igual a la intancia del objeto con con el metodo de cursor (que permite leer las sentcias SQL)
print(type(micursor)) # imprime el tipo de dato del objeto con
sentencia="SELECT * from alumno;" #Se crea la variable

micursor.execute(sentencia)
for fila in micursor.fetchall():
    print(fila[0])
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('-'*50)