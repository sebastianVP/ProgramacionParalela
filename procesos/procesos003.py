#procesos daemon
import multiprocessing
import time
import numpy as np

def fibonacci(lista_valores: list,valor_comparativo: float=np.inf)->None:
    """
    Calcula la Sucesion de Fibonacci hasta que el valor calculado sea mayor o igual al valor con el que
    se le compara
    Parámetros
    -----------
    param: list: lista_valores: Lista inicial con valores
    -----------
    param : float: valor_comparativo: Valor comparativo que sirve para frenar la ejecución del codigo
    -----------
    Salida
    -----------
    return : NoneType:None
    """
    valor_fibo=0.0
    while valor_fibo< valor_comparativo:
        valor_fibo = lista_valores[-1] + lista_valores[-2]
        lista_valores.append(valor_fibo)
        print(f"Valor mas reciente de la sucecion de Fibonacci:{valor_fibo}")
        time.sleep(0.5)

if __name__=="__main__":
    #Establecer metodo
    multiprocessing.set_start_method("spawn")
    # Definir valores para funcion
    valores_fibonacci = [0,1]
    # Declarar e inicializar el proceso
    p = multiprocessing.Process(target= fibonacci,args=(valores_fibonacci,np.inf),daemon=True)
    p.start()
    # Dormir  5 segundos
    time.sleep(5)
    print("Programa finalizado")

"""
NOTA:
* Los procesos daemon se cierran tan pronto el programa se ha terminado de ejecutar
esto puede llevar a una perdida de informacion si dicho proceso no habia terminao su ejecucion
"""