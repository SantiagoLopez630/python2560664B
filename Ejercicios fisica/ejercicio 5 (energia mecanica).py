"""
Ejercicio 5
Un cilindro de 100 gramos se desliza sobre una rampa partiendo del reposo en la posición A a 12 metros de altura 
hasta el punto B a 10 metros, para luego caer a nivel del piso en el punto C.
¿Cuánto es la energía mecánica del cilindro en el punto B?
"""

import math
def calcularEjercicio():
    print('Ejercicio 5\n Un cilindro de 100 gramos se desliza sobre una rampa partiendo del reposo en la posición A a 12 metros de altura hasta el punto B a 10 metros, para luego caer a nivel del piso en el punto C. ¿Cuánto es la energía mecánica del cilindro en el punto B?\n')
    rta=int(input('Ingrese la energia mecanica'))
    #conversión unidades
    Em=0.100*9.8*12

    if Em  == rta:
        print('Muy bien :), has acertado. La respuesta correcta es ',Em)
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