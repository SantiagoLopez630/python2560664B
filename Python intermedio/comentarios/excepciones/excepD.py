def edad(): # esta parte una funcion con la variable edad 
    try: # esencial para que se ejecuten las exepciones 
        tuedad=int(input("introduce tu edad")) # en esta parte se crea una variable 'tuedad' para que en ella se pueda ingresar una edad por teclado 
        print(f'tu edad es  {tuedad}') # se utiliza la f para unir escritura y los valores  ene este caso imprime la edad que se ingreso 
        #print('Tu edad es ',tuedad)
    except ValueError as e:# en esta parte esta la exepcion de que si ingresa un valor que no sea un numero se ejecuta la expecion  ValueError
        print(e) # 'e' es el nombre que toma   el error ValueError
        print("La edad debe ser un valor numerico...") # en esta parte se imprime un enunciado para el usuario 
        edad()# en esta parte se llama la funcion 
    
edad() #en esta parte se llama la funcion