def archivoEncontrado():

    try:
        archivo1 = open('c:/archivoAdso.txt')

    except FileNotFoundError:

        print('No se encontro el archivo')


archivoEncontrado()