"""
Solicite una fecha al usuario. en formato día, mes y año. Dígale cuanto tiempo
ha pasado desde esa fecha hasta hoy o cuanto falta para llegar a esa fecha si es
posterior
"""

dia,mes,año=input('digite una fecha dia/mes/año ejemplo(12/8/22) separados por un "/" ').split("/")
dia=int(dia)
mes=int(mes)
año=int(año)

if año > 22:
    print('La fecha ', dia,"/",mes,"/",año, 'es mayor a la fecha de hoy')
    if 27>dia:
        dia=(dia-27)*-1
    else:
        dia-=27
    if 9>mes:
        mes=(mes-9)*-1
    else:
        mes-=9
    if 22>año:
        año=(año-22)*-1
    else:
        año-=22

    print('y han faltan, ' , dia,"dias, ",mes,"meses, ",año,"años" )

elif 22 > año:
    print('La fecha ', dia,"/",mes,"/",año, 'es menor a la fecha de hoy')
    
    dia=(dia+27)
    mes=(mes+9)
    if 22>año:
        año=(año-22)
    else:
        año-=22

    print('y han pasado, ' , dia,"dias, ",mes,"meses, ",año,"años" )

else :
    print('La fecha ', dia,"/",mes,"/",año, 'es igual a la fecha de hoy')