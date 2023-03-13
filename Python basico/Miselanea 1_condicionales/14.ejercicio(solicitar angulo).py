"""
Solicite un Angulo al usuario en grados. Diga en que cuadrante está. Diga
además en que vuelta está sabiendo que cada 360 grados se completa una
vuelta a la circunferencia. Además diga el resultado en radianes.
"""

from math import pi, trunc

angulo1 = int(input("Ingrese el ángulo en grados:  "))


vuelta = trunc(angulo1/360)
angulo1 -=(vuelta*360)
radianes = angulo1*pi/180
if angulo1 >0 and angulo1<=90:
    print("Está en el cuadrante #: 1 y esta en la vuelta # ",vuelta+1," a la circunferencia y en radianes es: ",radianes)
elif angulo1 >90 and angulo1<=180:
    print("Está en el cuadrante #: 2 y esta en la vuelta # ",vuelta+1," a la circunferencia y en radianes es: ",radianes)
elif angulo1>180 and angulo1<=270:
    print("Está en el cuadrante #: 3 y esta en la vuelta # ",vuelta+1," a la circunferencia y en radianes es: ",radianes)
else:
    if angulo1==0:
        print("Está en el cuadrante #: 4 y esta en la vuelta # ",vuelta," a la circunferencia y en radianes es: ",radianes)
    else:
        print("Está en el cuadrante #: 4 y esta en la vuelta # ",vuelta+1," a la circunferencia y en radianes es: ",radianes)