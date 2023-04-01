# Hacer un programa que me reste dos fechas una la actual y otra una que el usuario ingrese por pantalla


import datetime

fecha_actual = datetime.datetime.now()

fecha_ingresada = input("Ingresa una fecha en formato dd/mm/yyyy: ")

fecha_ingresada = datetime.datetime.strptime(fecha_ingresada, "%d/%m/%Y")

diferencia = fecha_actual - fecha_ingresada

print(f"La diferencia entre las dos fechas es de {diferencia.days} días.")
