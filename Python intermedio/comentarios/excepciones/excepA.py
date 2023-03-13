try:        # esta linea ejcuta un try que va intentar hejecutar un bloque de codigo si es correcta
    #print(1/1))       
    raise SyntaxError     #la palabra reservada raise simula un error como si en verdad hubiese ocurrido
except SyntaxError:       #si no se cumple el try se ejecuta un except que ejecuta un bloque de codigo si un error aparece en este caso, Syntax Error  
    print('Cierra el parentesis') #imprime la cadena de texto si el except se ejecuta