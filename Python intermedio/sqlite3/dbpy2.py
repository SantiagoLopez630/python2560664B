def modificar(conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id='{id}'"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación exitosa')

<