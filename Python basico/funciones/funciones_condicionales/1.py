"""
Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número
exceda los límites emita un mensaje y finalice el programa
"""
a=int(input('ingrese un numero '))
def verificarNumero(a):
    if 10>a:
        print('el numero tiene 1 cifras')
    elif 100>a:
        print('el numero tiene 2 cifras')
    elif 1000>a:
        print('el numero tiene 3 cifras')
    elif 10000>a:
        print('el numero tiene 4 cifras')
    else :
        print("")

verificarNumero(a)