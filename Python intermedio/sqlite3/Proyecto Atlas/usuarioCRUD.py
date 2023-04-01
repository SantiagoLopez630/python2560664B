from Usuario import *
import sqlite3 

lista=[]
with sqlite3.connect('pythonsqlite/pythondb.db')as con:
    micursor=con.cursor()
    new_sql="SELECT *  from persona"
    #print(micursor.execute(new_sql).fetchall())
    lista=micursor.execute(new_sql).fetchall()

personas=[]
for fila in lista:
    id=fila[0]
    nombre=fila[1]
    apellido=fila[2]
    mail=fila[3]
    ob=Persona(id,nombre,apellido,mail)
    personas.append(ob)

print(personas)

for p in personas:
    print(p.getNombreCompleto())
con=sqlite3.connect('sqlitepython/conpython.db') 
micursor=con.cursor()
     
def insertar(conexion,tabla,id,dato,id):
    
    
def modificar(conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id='{id}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion exitosa !!!!!')
  
def eliminar(conexion,tabla,campo,dato):
    micursor=conexion.cursor()
    sentencia=f"DELETE FROM {tabla}  WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion exitosa !!!!!')