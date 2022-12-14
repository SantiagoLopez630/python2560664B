"""
Ejercicio 3
Una grúa sube en forma vertical un bloque hasta una altura de 4 m, a velocidad constante y en un tiempo de 10 s.
La potencia disipada para realizar ese trabajo es de 2000 W.

¿Cuál es el peso del bloque?

"""

import math
def calcularEjercicio():
    print('Ejercicio 3\n Una grúa sube en forma vertical un bloque hasta una altura de 4 m, a velocidad constante y en un tiempo de 10 s.La potencia disipada para realizar ese trabajo es de 2000 W. ¿Cuál es el peso del bloque?\n')
    rta=int(input('Ingrese el peso del bloque'))
    #conversión unidades
    w= (2000*10)
    f= w//4

    if f  == rta:
        print('Muy bien :), has acertado. La respuesta correcta es ',f)
    else :
        intento=input('La respuesta es incorrecta :( . Desea volver a intertarlo? s/n \n')
        if intento == 's' :
            try :
                calcularEjercicio()
            except ValueError:
                print('Solo se aceptan valores numericos')
            except :
                print('error')

try :
    calcularEjercicio()
except ValueError:
    print('Solo se aceptan valores numericos')
except :
    print('error')