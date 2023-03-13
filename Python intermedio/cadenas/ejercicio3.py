#cuantas veces se repite un caracter dado

cadena=input('ingrese una cadena: ')

def contarABC (cadena):
    for i in cadena:
        print('La letra', i , ' se repite' , cadena.count(i), 'veces.')
        
contarABC(cadena)

