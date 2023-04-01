import sqlite3 # se importa el modulo de sqlite3

with sqlite3.connect('sqlitepython/conpython.db')as con: #se instancia el objeto "con" que traera el metodo connect que a su vez traerá como parametro una ruta relativa todo esto dentro de un with que funcionara como en los archivos y funcionara solo en un bloque de codigo
    micursor=con.cursor() #Se instancia un objeto "micursor" que será igual a la intancia del objeto con con el metodo de cursor (que permite leer las sentencias SQL)
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;" #Se crea la variable sentencia con la consulta SQL que traera id, nombre y apellido de la tabla alumno solo si el id es mayo o igual que 400
    #print(micursor.execute(sentencia).fetchall())

def miselect(conexion,tabla,campo,operador,dato): # se define una funcion para crear sentencias de consulta, donde los parametros serviran para crear la sentencia
    micursor=conexion.cursor() #Se instancia un objeto "micursor" que será igual a la intancia del objeto con con el metodo de cursor (que permite leer las sentencias SQL)
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'" #Se crea la variable sentencia con la consulta SQL que traera toso de la tabla que el usuario llame con los campos datos y operador que le requira
    print(sentencia) #Se imprime la sentencia 
    print(micursor.execute(sentencia).fetchall()) #Se imprime la jecucion se la sentencia y traera todos lo valores con el fetch all

miselect(con,'alumno','email','=','dbrabon2@irs.gov') # se le pasan los parametros a la funcion para llenar la sentencia 
