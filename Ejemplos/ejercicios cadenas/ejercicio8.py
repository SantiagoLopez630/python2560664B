#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.

def cifrado_cesar(palabra, desplazamiento):
    # Convertir la palabra a mayúsculas
    palabra = palabra.upper()
    # Inicializar la palabra cifrada
    palabra_cifrada = ""
    # Iterar por cada letra de la palabra
    for letra in palabra:
        # Si la letra es una letra del alfabeto, cifrarla
        if letra.isalpha():
            # Convertir la letra a su valor numérico ASCII
            valor_ascii = ord(letra)
            # Calcular el valor ASCII de la letra cifrada
            valor_ascii_cifrado = (valor_ascii - 65 + desplazamiento) % 26 + 65
            # Convertir el valor ASCII cifrado a su letra correspondiente
            letra_cifrada = chr(valor_ascii_cifrado)
        # Si la letra no es una letra del alfabeto, dejarla sin cifrar
        else:
            letra_cifrada = letra
        # Añadir la letra cifrada a la palabra cifrada
        palabra_cifrada += letra_cifrada
    # Devolver la palabra cifrada
    return palabra_cifrada

palabra = input('Ingrese una palabra: ')
desplazamiento = int(input('Ingrese el numero de desplazamientos que desea hacer: '))
palabra_cifrada = cifrado_cesar(palabra, desplazamiento)
print(f"La palabra '{palabra}' cifrada con un desplazamiento de {desplazamiento} posiciones es: {palabra_cifrada}")