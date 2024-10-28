import threading
import matplotlib.pyplot as plt
import time

#Definir clase
class Empresa:
    """
    Clase que genera el comportamiento de ventas y costos
    """
    def __init__(self,inicial:float=1000.0)-> None:
        """
        Constructor.
        Parametros
        -----------
        param: float:inicial: Dinero inicial que tiene la empresa(por defecto , 1000 esta configurados)
        -----------
        Salida
        -----------
        return : NoneType
        """
        # Inicializando variables
        self.inicial = inicial # Dinero inicial
        self.historial  = [] # historial de ventas y costos

    def ventas(self)-> None:
        """
        Funcion de ventas
        """
        # 1 millon de ventas cada una a 10 soles
        ingreso= 10
        for i in range(1000000):
            self.inicial+=ingreso
            self.historial.append(1)
        # mensaje
        print("Ventas ha finalizado")

    def costos(self)->None:
        """
        Funcion de costos
        """
        # Similar a 1000000
        costo= 10
        for i in range(1000000):
            self.inicial-=costo
            self.historial.append(-1)
        #Mensaje
        print("Costos ha finalizado")

# INSTANCIAMOS LA CLASE
emp= Empresa()
# hilos
threading.Thread(target=emp.ventas).start()
threading.Thread(target=emp.costos).start()
time.sleep(1)
# CALCULAR EL VALOR ESPERANDO
inicial = 1000
ingreso = 10
costo = 10
simulaciones =1000000 
valor_esperado= inicial + ingreso*simulaciones-costo*simulaciones# 1000 unidades

print("valor_esperado =", valor_esperado)
print("valor_final=",emp.inicial)

# COMPETENCIA POR INTÉRPRETE GLOBAL
plt.figure(figsize=(12,6))
plt.plot(emp.historial)
plt.title("Competencia por el Intérprete Global")
plt.show()

# Recordatorio
"""
* Los hilos son utiles para problemas de Entrada/Salida. Por otro lado, cuando nuestro código requiere de eficiencia computacional
  eso puede ocasionar un problema donde cada hilo lucha por obtener el Bloque del Intérprete global.
* Cada hilo dentro de un proceso comparte el mismo espacio de memoria, lo que significa que pueden acceder y modificar las mismas variables y datos. Sin el uso adecuado de técnicas de sincronizacion, nuestro código puede obtener
  resultados no concluyentes. Las técnicas de sincronizacion las desarrollaremos luego.


"""