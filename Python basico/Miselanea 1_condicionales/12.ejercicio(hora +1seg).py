"""
Solicite la hora en formato horas, minutos y segundos. Imprima en pantalla la
hora que será dentro de 1 segundo
"""

h,m,s=input('ingrese horas en formato hh:mm:ss separados por ":" ').split(":")
h=int(h)
m=int(m)
s=int(s)
if h>12:
    print('la hora ingresada debe ser en formato 12 horas')
else:
    if 59 > s:
        print('La hora ingresada mas un segundo despues es: ', h,m,s+1)
    else :
        s=00
        print('La hora ingresada mas un segundo despues es: ', h,":0",m+1,":0",s)