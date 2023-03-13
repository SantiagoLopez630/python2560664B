"""
Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig.
manera:
Si trabaja 40 horas o menos se le paga $2600 por hora
Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40
horas y $5000 por cada hora extra
"""

a=int(input('Cuantas horas trabajó esta semana? '))

def verificarSalario(a):
    if 41>a:
        a=a*2600
        print('Su salario esta semana será de: ', a)
    else :
        a=(40*2600)+((a-40)*5000)
        print('Su salario esta semana será de: ', a)

verificarSalario(a)