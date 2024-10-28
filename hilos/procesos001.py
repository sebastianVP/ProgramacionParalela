# -*- coding: utf-8 -*-
# importando librerias
import multiprocessing

# DEFINIR FUNCION
def suma_cuadrados(limite_inferior:int,limite_superior:int)-> None:
    """
    Funcion que calcula la suma de los cuadrados en el limite indicado

    Parámetros
    ----------
    param: int :  limite_inferior de nuestro rango
    -----------
    param: int :  limite_superiorde nuestro rango
    -----------
    Salidas
    return: NoneType: None

    """
    # Calcular
    valor = 0
    for i in range(limite_inferior,limite_superior+1):
        valor += i**2
    print(f"Suma de los cuadrados en el rango de {limite_inferior} y {limite_superior} = {valor}")

if __name__== "__main__":
    # muestra el numero de procesadores
    print("Numero de procesadores:",multiprocessing.cpu_count())
    # Establecer metodo
    multiprocessing.set_start_method("spawn")
    # Existen 3 metodos para inicializar un proceso
    # 1. spawn :Crea un nuevo hijo. Es el mas utilizado y el estndar en la mayoria de los escenarios.
    # 2. fork: Crea un hijo idéntico al padre. Es usado en sistemas UNIX.
    # 3. forkserver: UTILIZA UN PROCESO  de servidor para crear nuevos procesos.
    limites_inferiores=[0,100,200,300,400,500,600, 700,800]
    limites_superiores=[100,200,300,400,500,600, 700,800,900]
    for i in range(len(limites_inferiores)):
        p=multiprocessing.Process(target=suma_cuadrados,args=(limites_inferiores[i],limites_superiores[i]))
        p.start()
    """"
    Recordatorios:
    - Los procesos son especialmente útiles en tareas que requieren eficiencia comiacional.
    - Un procesos es una instancia idependiente del interprete de Python
      que se ejecutara en su propio espacio de memoria.
    - A diferencia de los hilos, los procesos no estan afectados por el Bloqueo del Interprete Global(GIL), LO QUE PERMITE UNA 
      ejecucion verdaderamente paralela.
    - El limite de los procesos que deberiamos correr, se deberia de limitar al numero de núcleos 
      que tiene nuestra computadora(Si se inicializa mas procesos o muchos, nuestro sistema operativo puede empezar a destruir algunos Procesos 
      para preservar el funcionamiento del sistema).
    - 
    """


