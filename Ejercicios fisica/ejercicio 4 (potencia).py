"""
Ejercicio 4
Un automóvil circula por la carretera a una velocidad constante de 120 Km/h. 
Sabiendo que la fuerza de rozamiento con la carretera es de 200 N y la fricción con el aire supone 820 N, 
¿Qué potencia debe desarrolar el automóvil para poder mantener la velocidad constante? Da el resultado en CV.

"""

import math
def calcularEjercicio():
    print('Ejercicio 4\n Un automóvil circula por la carretera a una velocidad constante de 120 Km/h. Sabiendo que la fuerza de rozamiento con la carretera es de 200 N y la fricción con el aire supone 820 N, ¿Qué potencia debe desarrolar el automóvil para poder mantener la velocidad constante? Da el resultado en CV.\n')
    rta=int(input('Ingrese la potencia del automovil'))
    #conversión unidades
    f= 200+820
    v= (120*1000)/3600
    p = f*v
    cv=p/735

    if f  == rta:
        print('Muy bien :), has acertado. La respuesta correcta es ',cv)
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