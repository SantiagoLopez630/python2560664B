#Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez
cadena=input('ingrese una cadena: ')
abecedario='abcdefghijklmnopqrstvwxyz'
def contarABC (cadena):
    x=0
    z=0
    a=''
    for i in cadena:
        y=cadena.count(i)
        if y>1 and z==0 or a==i: 
            z+=1
            a=a+i

        else:
            if i in abecedario:
                x+=1
    print(x)

contarABC(cadena)

