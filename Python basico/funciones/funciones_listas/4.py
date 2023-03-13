import random


tam=random.randint(10, 25)
vec=[]

def calcularNum(vec, tam):
    cont=0
    prom=0
    suma1=0
    for i in range(tam):
        vec.insert(i,round(random.randint(0, 100)))
    print(vec)

    for i in range(len(vec)):
        cont=cont+1
        suma1=suma1+vec[i]
        prom=suma1/cont

    print('La suma de los numeros de la lista ',vec,' es: ',suma1)
    print('El promedio de los numeros de la lista ',vec,' es: ',prom)

calcularNum(vec, tam)