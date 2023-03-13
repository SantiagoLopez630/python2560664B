#De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.

import re
def contarCaracteres(palabra):

    vocales = ['a', 'e', 'i', 'o', 'u']
    cont=0
    contC=0
    cont_til=0
    cont_es=0

    for p in palabra:

        if p.lower() in vocales:
            cont += 1

        elif re.search(r'[À-ÿ]', p):
            cont_til=palabra.count(p)

        elif p.isalpha() and p.lower() not in vocales:
            contC += 1

        
        elif re.search(r'\W', p):
            cont_es=palabra.count(p)

    print('Su palabra ',palabra, ' \n tiene ',cont,'vocales\n' ' tiene ',contC,'consonantes\n' ' tiene ',cont_til,'tildes\n' ' tiene ',cont_es,'caracteres especiales\n')
        

palabra=input('Ingrese una palabra: ')
contarCaracteres(palabra)