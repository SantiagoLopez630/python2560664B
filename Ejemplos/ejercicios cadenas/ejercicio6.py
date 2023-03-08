#Determinar en que tiempo esta conjugado un verbo

verbo = input("Introduce un verbo en infinitivo: ")

# Lista de terminaciones para cada tiempo
presente_terminaciones = ['o', 'as', 'a', 'amos', 'áis', 'an']
preterito_imperfecto_terminaciones = ['aba', 'abas', 'aba', 'ábamos', 'abais', 'aban']
futuro_terminaciones = ['é', 'ás', 'á', 'emos', 'éis', 'án']

# Comprobamos si el verbo está conjugado en presente
if verbo.endswith(tuple(presente_terminaciones)):
    print(f"El verbo '{verbo}' está conjugado en presente.")
# Comprobamos si el verbo está conjugado en pretérito imperfecto
elif verbo.endswith(tuple(preterito_imperfecto_terminaciones)):
    print(f"El verbo '{verbo}' está conjugado en pretérito imperfecto.")
# Comprobamos si el verbo está conjugado en futuro
elif verbo.endswith(tuple(futuro_terminaciones)):
    print(f"El verbo '{verbo}' está conjugado en futuro.")
# Si no se encuentra en ninguno de los tiempos anteriores, el verbo no está conjugado
else:
    print(f"El verbo '{verbo}' no está conjugado.")
