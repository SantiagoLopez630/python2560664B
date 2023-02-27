values = (1, 0) #la variable 'values' guarda una tupla que contiene dos elementos
#x,y=19,30 # se puede nguardar dos variables
#print(divmod(10,3)) #imprime el residuo y el cociente 
try: #esta linea ejcuta un try que va intentar hejecutar un bloque de codigo si es correcta
    q, r = divmod(*values) #muestra las variables 
    #print(f'q=',q) #imprime en una cadena una variable sin necesidad de las comas
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e: #si no se cumple el try se ejecuta un except que ejecuta un bloque de codigo si un error aparece en este caso, Zero division error y Type error 
    print(type(e), e) #imprime el tipo de la variable e