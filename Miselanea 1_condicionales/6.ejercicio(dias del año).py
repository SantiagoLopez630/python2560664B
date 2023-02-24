"""
Pida un numero al usuario que representa días del año. Diga a que mes del año
corresponde así. Si el número es menor o igual a 31 indica que esta en enero,
Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días.
"""

a=int(input('ingrese el numero dia '))

if 32>a:
    print('Está en enero')
elif 60>a:
    print('Está en febrero')
elif 91>a:
    print('Está en marzo')
elif 121>a:
    print('Está en abril')
elif 152>a :
    print('Está en mayo')
elif 182>a :
    print('Está en junio')
elif 213>a :
    print('Está en julio')
elif 244>a :
    print('Está en agosto')
elif 274>a :
    print('Está en septiembre')
elif 305>a :
    print('Está en octubre')
elif 335>a :
    print('Está en noviembre')
elif 366>a :
    print('Está en diciembre')
else: 
    print('Ingrese un dia inferior o igual a los 365 dias del año')