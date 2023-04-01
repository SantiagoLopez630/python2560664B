def typeError():

    try:
        print(ord('伊'))
    except TypeError:
        print('Dato no identificado')


typeError()