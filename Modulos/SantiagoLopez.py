#funciones para matrices

#llenar una lista con numeros random
from random import randint

def llenar(n):
    matriz = []

    for r in range(n):
        fila = []

        for c in range(n):
            fila.append(randint(1, 100))
            
            matriz.append(fila)
        
        return matriz

    resultado = llenar(5)

    print(resultado)

#leer una matriz y mostrar el ultimo elemento
def leer(matriz):
    matrizLong = len(matriz)

    for i in range(matrizLong):
        print(matriz[i][-1])

#imprimir filas 
def impFilas(matriz):
    matrizLong = len(matriz)

    for i in range(matrizLong):
        print(matriz[i])

#sumar por filas
def sumarFil(matriz):
    sumaFilas = []
    for i in matriz:
        sumaFilas.append(sum(i))

    print(sumaFilas)
    
#sumar por columnas
def sumarCol(matriz):
    suma = []
    for j in range(len(matriz[0])):
        sumaColumna = 0
        for i in range(len(matriz)):
            sumaColumna += matriz[i][j]

        suma.append(sumaColumna)

    print(suma)