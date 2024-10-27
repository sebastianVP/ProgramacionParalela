# importamos librerias
import threading
import time
# Definimos funciones

def func1(segundos: float)-> None:
    """
    funcion que ejecutara el primer hilo

    Parametros
    -------------
    param: float: segundos: Segundosn que nuestro programa dormira entre cada iteracion
    -------------
    Salida
    -------------
    return: NoneType: None
    """
    while True:
        print("Hilo No. 1")
        time.sleep(segundos)

def func2(segundos: float)-> None:
    """
    funcion que ejecutara el primer hilo

    Parametros
    -------------
    param: float: segundos: Segundosn que nuestro programa dormira entre cada iteracion
    -------------
    Salida
    -------------
    return: NoneType: None
    """
    while True:
        print("Hilo No. 2")
        time.sleep(segundos)


#hilo
t1= threading.Thread(target=func1,args=[3],name="ID:1")# kwargs("seconds":3)
t2= threading.Thread(target=func2,args=[3],name="ID:2")
#inicializar hijo
t1.start()
t2.start()

# los hilos se ejecutan dentro de un proceso, y dentro de un proceso puedes tener uno o mas hilos en ejecucion
# cada hilo dentro de un proceso comparte el mismo espacio en memoria, lo que significa que pueden acceder y modificar las mismas variables y datos
"""
La concurrencia es un concepto en programación que se refiere a la capacidad de ejecutar múltiples tareas de 
forma que parezcan ocurrir al mismo tiempo. A diferencia del paralelismo, donde dos o más tareas se ejecutan 
literalmente al mismo tiempo en distintos núcleos del procesador, en la concurrencia el sistema interrumpe y 
reanuda tareas de manera rápida, creando la ilusión de simultaneidad. Esto permite que varias tareas 
 de forma independiente sin necesidad de que terminen antes de que otras puedan comenzar.

Ejemplo de Concurrencia vs. Paralelismo

Imagina que tienes varias tareas (como cocinar, lavar la ropa y limpiar la casa). En un sistema concurrente, 
cambiarías de tarea rápidamente: comienzas a cocinar, luego lavas algo de ropa, y más tarde limpias un poco 
antes de regresar a la cocina. Esto da la sensación de que todas las tareas avanzan. En el paralelismo, cada 
tarea sería realizada por una persona diferente, logrando que las tareas realmente se ejecuten al mismo tiempo.
""" 