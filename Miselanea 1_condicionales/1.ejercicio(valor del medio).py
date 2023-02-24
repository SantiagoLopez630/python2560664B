"""
Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
valor del medio es 11. No use operadores lógicos

"""

a,b,c=input('ingrese tres numeros separados por una coma').split(",")
a=int(a)
b=int(b)
c=int(c)

list=[a,b,c]
i=len(list)
valorM=i//2
print(i)
if len(list)%2==0:
    print('Por favor ingrese tres numeros')
else:
    print(list[valorM])
