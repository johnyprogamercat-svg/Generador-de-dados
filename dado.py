import time
import random
print("Bienvenido al juego de dado.")
Respuesta = input("Escribe Y para iniciar: ")
if "Y" in Respuesta:
    Cantcara = input("¿De cuántas caras es tu dado?: ")
    Cara_de_dado = str(random.randint(1,int(Cantcara)))
    print("Lanzando dado...")
    time.sleep(1)
    print("Ya está cayendo...")
    time.sleep(1)
    print("El dado ha caído en la cara " + str(Cara_de_dado))
