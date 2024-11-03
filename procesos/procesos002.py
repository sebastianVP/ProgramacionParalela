import multiprocessing
import time
# NECESITAMOS UNA LIBRERIA MAS
import os



# Crear documento
archivo = "archivo.txt" #Documento donde los procesos guardarn informacion
# DEBEMOS ASEGURAR QUE SOLO SE CREE UNA VEZ
if not os.path.isfile(archivo):
    documento = open(archivo,"w")

# Definir funcion

def guardar_datos(datos: str,nombre_archivo: str)->None:
    """
    Abre un archivo y agrega datos
    Parametros
    ---------
    param: str: dataos: Datos que se agregaran e imprimiran por consola
    ----------
    param: str: nombre_archivo: Nombre del archivo donde se agregarn los datos o informacion
    ----------
    Salida
    ----------
    return : NoneType: None
    """
    # Agregar el contenido, la a significa que quieres agregar 
    # nueva informacion al documento al final
    with open(archivo,"a") as documento_func:
        documento_func.write(datos)
        documento_func.write("\n")
        documento_func.close()
    print(f"Finalizando con datos: {datos}")



if __name__=="__main__":
    # Establecer metodo
    multiprocessing.set_start_method("spawn")
    # Inicializar 4 Procesos
    for i in range(4):
        p = multiprocessing.Process(target=guardar_datos,name=f"Proceso_{i}",args=(f"Proceso_{i}",archivo))
        p.start()

    """
    NOTA: AL COMIENZO SOLO HAY EVIDENCIA DE UN PROCESO
    1. Cada proceso realiza una clonacion de recursos para ejecutarse de manera correcta,
    es importante estructurar nuestro codigo de tal manera que no se tengan problemas en la clonacion
    de recurso.
    2. Es importante utilizar sincronizadores los cuales se veran mas adelante para que no exista perdida
    de informacion.
    """


