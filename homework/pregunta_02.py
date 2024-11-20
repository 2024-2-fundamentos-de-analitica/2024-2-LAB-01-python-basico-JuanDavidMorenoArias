"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    # Abre el archivo .csv en modo lectura
    with open('files\\input\\data.csv','r') as file:
        # Creacion de un diccionario para los resultados
        results = {}
        # Se itera linea por linea del archivo
        for line in file:
            # se separa los elementos de la linea por espacio
            letra = line.split()
            # se extrae el primer elemento de la linea
            letra = letra[0]
            # Se agregan los elementos al diccionario por aparicion
            if letra not in results:
                results[letra] = 0
            results[letra] += 1
        # Se ordena el diccionario por orden de los items
        sorted_dict = dict(sorted(results.items()))
        # se retornan los resultados
        return list(sorted_dict.items())
    







