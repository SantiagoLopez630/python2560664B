"""
Escribe un programa que pida tres números y que escriba si son los tres
iguales, si hay dos iguales o si son los tres distintos
"""

a,b,c=input('ingrese tres numeros separados por una coma ').split(",")
a=int(a)
b=int(b)
c=int(c)

list=[a,b,c]
if a==b==c:
    print('los tres son iguales')
elif a==b or a==c or b==c:
    print('dos numeros son iguales')
elif a!=b!=c:
    print('los tres son diferentes')
else :
    print('los numeros ingresados no entran sobre la escala definida')