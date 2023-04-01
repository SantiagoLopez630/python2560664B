import sqlite3 # se importa el modulo de sqlite3
with sqlite3.connect('sqlitepython/conpython.db')as con: #se instancia el objeto "con" que traera el metodo connect que a su vez traerá como parametro una ruta relativa todo esto dentro de un with que funcionara como en los archivos y funcionara solo en un bloque de codigo
    micursor=con.cursor() #Se instancia un objeto "micursor" que será igual a la intancia del objeto con con el metodo de cursor (que permite leer las sentencias SQL)
    sentencia="SELECT nombre,apellido FROM alumno;" #Se crea la variable sentencia con la consulta SQL que traera todo de la tabla alumno 

    print(micursor.execute(sentencia).fetchmany(10)) # se imprime los valores de la tabla traidos con el exucute, y traera 10 valores con el fetchmany

#print()

