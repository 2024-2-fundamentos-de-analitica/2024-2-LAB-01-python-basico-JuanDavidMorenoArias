"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # creacion un contador para la suma
    sum = 0
    # Abre el archivo .csv en modo lectura
    with open('files\\input\\data.csv','r') as file:
        # itera linea por linea
        for line in file:
            # se separa las lineas por espacios
            number = line.split()
            # se extrae la segunda columna de cada linea
            number = number[1]
            # se convierte el numero de la segunda columna a entero
            number = int(number)
            # se suma el numero extraido al contador
            sum += number
    # finalmente, se retorna el resultado
    return sum
 

