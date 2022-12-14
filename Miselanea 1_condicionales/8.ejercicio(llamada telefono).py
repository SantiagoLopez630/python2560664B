"""
Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo
los cálculos así:
Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan
200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que
permita calcular el costo de una llamada dados los minutos de duración.
"""

a=int(input('Cuantos minutos duró la llamada? '))

if 3>=a:
    a=a*200
    print('Su llamada costará: ', a)
else :
    a=(3*200)+((a-3)*50)
    print('Su llamada costará: ', a)