def divisores(numero):
    """
    Genera una lista de los divisores de un número.
    """
    resultado = [i for i in range(1, numero + 1) if numero % i == 0]

    return resultado

print(divisores(5))
print(divisores(10))
print(divisores(13))
print(divisores(17))