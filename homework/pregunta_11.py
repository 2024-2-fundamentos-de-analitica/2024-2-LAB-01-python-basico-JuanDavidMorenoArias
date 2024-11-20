"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open('files\\input\\data.csv','r') as file:
            # Creacion de un diccionario para los resultados
            sumas = {}
            # Se itera linea por linea del archivo
            for line in file:
                # se separa los elementos de la linea por espacio
                linea_extraida = line.split()
                # se extrael el quinto elemento, los codigos
                letras = linea_extraida[3].split(',')

                numero = int(linea_extraida[1])

                for letra in letras:
                    if letra not in sumas:
                          sumas[letra] = 0
                    sumas[letra] += numero
            # Se ordena el diccionario por orden de los items 
            sorted_dict = dict(sorted(sumas.items()))    

            return sorted_dict
