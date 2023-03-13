"""
Solicite al usuario una cantidad numérica que expresa segundos (medida de
tiempo). Exprésela (conviértala) en horas minutos y segundos. Según el caso
"""

monto=int(input('Digite una cantidad: '))

if monto%24==0:
    cant=monto/24
    print('Equivaldria a ',cant,' horas')
else:
    cant=monto//24
    monto-=24*cant
    monto*=60
    print('Equivaldria a ',cant,'horas')
    if monto>=60:
        cant=monto//60
        monto-=60*cant
        monto*=60
        print('Equivaldria a ',cant,'minutos')
        if monto>=60:
            cant=monto//60
            monto-=60*cant
            print('Equivaldria a ',cant,'segundos')
