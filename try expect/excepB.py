values = (1, 0) #la variable 'values' guarda una tupla que contiene dos elementos
#x,y=19,30 
#print(divmod(10,3))
try:
    q, r = divmod(*values)
    #print('q=',q)
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)