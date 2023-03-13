"""
Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores
"""

a=int(input('ingrese su nota '))

if 3>a:
    print('Insuficiente')
elif 5>a:
    print('Suficiente')
elif 7>a:
    print('Bien')
elif 10>=a:
    print('super bien')
elif 10==a :
    print("Excelente")
else: 
    print('Ingrese una nota dentro de la escala de valores')