"""
Escribir un algoritmo que pida un valor entero que equivale a una cantidad de
DINERO y calcule a cuantos billetes de 50.000, 20.000, 10.000, 5.000, 2.000, y
1.000 equivalen. Si el usuario digita 282000 el programa debe responder cinco
billetes de 50.000, un billete de veinte mil, un billete de diez mil, un billete de
dos mil.
"""
monto=int(input('Digite una cantidad de dinero'))

if monto%50000==0:
    cant=monto/50000
    print('Equivaldria a ',cant,'billetes de 50.000')
else:
    cant=monto//50000
    monto-=50000*cant
    print('Equivaldria a ',cant,'billetes de 50.000')
    if monto>=20000:
        cant=monto//20000
        monto-=20000*cant
        print('Equivaldria a ',cant,'billetes de 20.000')
        if monto>=10000:
            cant=monto//10000
            monto-=10000*cant
            print('Equivaldria a ',cant,'billetes de 10.000')
            if monto>=5000:
                cant=monto//5000
                monto-=5000*cant
                print('Equivaldria a ',cant,'billetes de 5.000')
            if monto>=2000:
                cant=monto//2000
                monto-=2000*cant
                print('Equivaldria a ',cant,'billetes de 2.000')
