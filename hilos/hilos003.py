# import librerias
import threading
import time

# funciones
def func1(segundos:float)->None:
    """
    Funcion que ejecutara el primer hilo.
    
    Parámetros
    ----------
    param: float:segundos: Segundos
    ----------
    Salida
    ----------
    return: NoneType: None.
    """
    # Ejecutar
    while True:
        print("Hilo No. 1")
        time.sleep(segundos)

def func2(segundos:float)-> None:
    """
    Funcion que ejecutará el segundo hilo

    Parámetros
    ----------
    param: float: segundos: Segundos que nuestro programa dormirá entre cada iteracion
    ----------
    Saluda
    ----------
    return:NoneType: None
    """
    while True:
        print("Hilo No. 2")
        time.sleep(segundos)

#hilos
t1= threading.Thread(target=func1,args=[1],daemon=True)
t2= threading.Thread(target=func2,args=[1],daemon=True)
# Inicializar hilos
t1.start()
t2.start()
#Dormir
time.sleep(8)
print("Finalizar Programa")