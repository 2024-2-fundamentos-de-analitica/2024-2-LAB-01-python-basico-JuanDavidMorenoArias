"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    # Abre el archivo .csv en modo lectura
    with open('files/input/data.csv','r') as file:
        # Creacion de un diccionario para los resultados
        results = {}
        # Se itera linea por linea del archivo
        for line in file:
            # se separa los elementos de la linea por espacio
            linea_extraida = line.split()
            # se extrae la letra, el primer elemento de la linea
            letra = linea_extraida[0]
            # se extrae el numero, el segundo elemento de la linea
            numero = linea_extraida[1]
            # se convierte el numero hecho string a entero
            numero = int(numero)

            # Se agregan los elementos al diccionario con su lista que contiene las letras asociadas
            if numero not in results:
                results[numero] = list()
            results[numero] += letra

            # Se ordena el diccionario por orden de las claves (numeros)
            sorted_dict = dict(sorted(results.items()))
            
        return list(sorted(sorted_dict.items()))
    


