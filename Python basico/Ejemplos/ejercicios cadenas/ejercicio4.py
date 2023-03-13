#Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas



def convertidorPalabras(palabra):


    palabra= palabra.upper()
    print(palabra)

    palabra= palabra.lower()
    print(palabra)

    palabra= palabra.capitalize()
    print(palabra)

    palabra= palabra.swapcase()
    print(palabra)

    palabra= palabra.title()
    print(palabra)
    
    cont=0
    n_palabra=''
    for letra in palabra:
        cont+=1
        if cont%2:
            n_palabra += letra.upper()

        else:
            n_palabra += letra.lower()
    print(n_palabra)

    cont=0
    n_palabra=''
    for letra in palabra:
        cont+=1
        if cont%2:
            n_palabra += letra.lower()

        else:
            n_palabra += letra.upper()
    print(n_palabra)





palabra = input('Ingrese una palabra: ')
convertidorPalabras(palabra)