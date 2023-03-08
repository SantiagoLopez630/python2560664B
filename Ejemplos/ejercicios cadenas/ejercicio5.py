#Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula

import pyphen, re

def VerificarPalabra(cadena):


        print(cadena)

        lista = cadena.split('-')
        palabra= ''.join(lista)
        cont=cadena.count('-')

        for p in lista:
                if re.search(r'[À-ÿ]', p):
                        pos=lista.index(p)
                        break
                else :
                        pos=-1


        match pos :

                case 0:
                        if cont==1:
                                print('Su palabra ',palabra, ' es grave')
                        
                        elif cont==2:
                                print('Su palabra ',palabra, ' es esdrujula')
                        
                        else:
                                print('Su palabra ',palabra, ' es sobre esdrujula')

                case 1:
                        if cont==1:
                                print('Su palabra ',palabra, ' es aguda')
                        
                        elif cont==2:
                                print('Su palabra ',palabra, ' es grave')
                        
                        else:
                                print('Su palabra ',palabra, ' es esdrujula')

                case 2:
                        if cont==2:
                                print('Su palabra ',palabra, ' es aguda')
                        
                        else:
                                print('Su palabra ',palabra, ' es grave')

                case 3:
                        print('Su palabra ',palabra, ' es sobre esdrujula')

                case -1:
                        if palabra.endswith('n') or palabra.endswith('s') or palabra.endswith('a') or palabra.endswith('e') or palabra.endswith('i') or palabra.endswith('o') or palabra.endswith('u'):
                                print('Su palabra ',palabra, ' es grave')
                        else :
                                print('Su palabra ',palabra, ' es aguda')



a = pyphen.Pyphen(lang='es')
cadena=a.inserted(input('Ingrese una palabra: ').lower())
VerificarPalabra(cadena)