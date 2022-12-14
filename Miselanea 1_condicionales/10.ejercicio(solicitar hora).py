"""
Solicite al usuario la hora en formato hh:mm:ss (hora militar, 24 horas). El
programa debe responder que hora será un segundo después. Ej: ingreso
11:59:59, el programa responde 12:00:00.
"""

h,m,s=input('ingrese horas en formato hh:mm:ss separados por ":" ').split(":")
h=int(h)
m=int(m)
s=int(s)

if h>24:
    print('la hora ingresada debe ser en formato 24 horas')
else:
    if 59 > s:
        print('La hora ingresada mas un segundo despues es: ', h,m,s+1)
    else :
        s=00
        print('La hora ingresada mas un segundo despues es: ', h,":0",m+1,":0",s)