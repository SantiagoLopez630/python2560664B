
"""
Genera una lista de los divisores de un número.
"""
numero=int(input('ingresa un numero al que quieras ver sus divisores '))
resultado = [i for i in range(1, numero + 1) if numero % i == 0]
print(resultado)