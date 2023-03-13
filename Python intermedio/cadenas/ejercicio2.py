#Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. Cual es el valor numerico de acuerdo a los códigos del alfabeto

cadena=input('ingrese una palabra: ')

def contarABC (cadena):
    y=0
    for i in cadena:
        print('El codigo de la letra', i , ' es:' , ord(i))
        y=y+ord(i)
    print('La suma total de todos los codigos ASCII es', y)

contarABC(cadena)

