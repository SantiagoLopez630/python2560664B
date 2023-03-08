#importar el módulo de encriptación 
import cryptography 
 
#abrir el archivo a desencriptar 
with open('reto-230209-164119.txt', 'rb') as f: 
    data = f.read() 
 
#clave de desencriptación 
clave = b'my_secret_password' 
 
#desencriptar el archivo 
desencriptado = cryptography.fernet.Fernet(clave).decrypt(data) 
 
#guardar el archivo desencriptado 
with open('reto-230209-164119.txt', 'wb') as f: 
    f.write(desencriptado)
