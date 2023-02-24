#Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última

def subcadenas(cadena):
    resultado = []
    for i in range(2, len(cadena) + 1):
        for j in range(len(cadena) - i + 1):
            resultado.append(cadena[j:j+i])
    return resultado


cadena=input('Ingrese una cadena: ')
resultado = subcadenas(cadena)
for subcadena in resultado:
    print(subcadena)