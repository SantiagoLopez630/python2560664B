import sqlite3
con=sqlite3.connect('Perseo (1).db')
micursor=con.cursor()

def insertar(tabla,idre,canhab,numpersonas,fechaini,fechafin,idusuario,idhabi):
    sentencia=f"INSERT INTO {tabla} VALUES ('{idre}','{canhab}','{numpersonas}','{fechaini}','{fechafin}','{idusuario}','{idhabi}')"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

insertar('tb_reserva',6,6,6,'30-03-2023','10-04-2023',121212,106)