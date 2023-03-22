#Hacer un programa en python que me diga cuantos dias han pasado desde los atentados del 11 de septiembre hasta la actualidad

from datetime import datetime, date, time
import datetime as d

fecha = date.today()
fechaHora = datetime.combine(fecha, time.min)

sept11 = d.datetime(2001, 9, 11)
dias = (fechaHora-sept11).days

print("La cantidad de días entre el 11 de septiembre de 2001 y la fecha actual es:", dias)