"""
En un juego de preguntas a las que se responde “Si” o “No” gana quien
responda correctamente las tres preguntas. Si se responde mal a cualquiera de
ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
1. Colon descubrió América?
2. La independencia de Colombia fue en el año 1810?
3. The Doors fue un grupo de rock Americano?
"""

a=input('Primera pregunta: \n Colon descubrió América? ')

if a == 'si' :
    print('muy bien, continuemos con la siguiente pregunta: ')
    b=input('Segunda pregunta: \n La independencia de Colombia fue en 1810? ')
    if b=='si':
        print('muy bien, continuemos con la siguiente pregunta: ')
        c=input('Tercera pregunta: \n The Doors fue un grupo de rock Americano? ')
        if c=='si':
            print('muy bien, has ganado el juego :) ')
else : 
    print('incorrecto')