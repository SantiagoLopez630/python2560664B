def multiple(valor, multiple):

    """

    Funcion para calcular si el numero es multiplo

    utilizando el modulo de la division

    """

    return True if valor % multiple == 0 else False

 

# lista que contendra los valores multiples


multiples_5=[]

 

# bucle del 1 al 100

for i in range(1, 101):

    if multiple(i, 5):

        multiples_5.append(i)


print ("\nLos multiples de 5 son:", multiples_5)