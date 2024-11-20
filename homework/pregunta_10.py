"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    with open('files/input/data.csv','r') as file:
        # Creacion de un diccionario para los resultados
        lista_de_tuplas = []
        # Se itera linea por linea del archivo
        for line in file:
            # se separa los elementos de la linea por espacio
            linea_extraida = line.split()
            # se extrae la letra de la columna uno
            letra = linea_extraida[0]
            # se extrae la cantidad de elementos en la columna 4
            elementos_columna_4 = len(linea_extraida[3].split(','))
            # se extrae la cantidad de elementos en la columna 5
            elementos_columna_5 = len(linea_extraida[4].split(','))

            # se agrega cada tupla a la lista de tuplas
            lista_de_tuplas.append(tuple((letra,elementos_columna_4,elementos_columna_5)))

            # se retorna el resultado
        return lista_de_tuplas