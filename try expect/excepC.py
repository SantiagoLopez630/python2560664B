def try_syntax(numerator, denominator): #función llamada try_syntax que toma dos argumentos numéricos
    try: #esta linea ejcuta un try que va intentar hejecutar un bloque de codigo si es correcta
        print(f'In the try block: {numerator}/{denominator}') #imprime en una cadena una variable sin necesidad de las comas
        result = numerator / denominator #la variable result es igual a la division entre un numerador y denominador
    except ZeroDivisionError as zde:#si no se cumple el try se ejecuta un except que ejecuta un bloque de codigo si un error aparece en este caso, Zero division error que se va a interpretar con la palabra reservada zde
        print(zde) #imprime zde
    else: #este else continua inmediatamente despues del else
        print('The result is:', result) #se imripime el resultado de la operacion 
        return result # retorna el  resultado 
    finally: # se ejecuta siempre la parte del codigo que se encuentre dentro de el al final del codigo
        print('Exiting') #imprime "Exiting"
        #return "Fallo por zero" #muestra en la consola fallo por zero
#print(try_syntax(12, 4)) 
print(try_syntax(11, 0)) ## en esta parte  se le dan los valores a  numerador y al denominador a la función