"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    with open('files/input/data.csv','r') as file:
        # Creacion de un diccionario para los resultados
        registros = {}
        # Se itera linea por linea del archivo
        for line in file:
            # se separa los elementos de la linea por espacio
            linea_extraida = line.split()
            # se extrael el quinto elemento, los codigos
            codigos = linea_extraida[4]
            # se separan los codigos por :
            codigos = codigos.split(',')

            # por cada codigo en la lista de codigos
            for codigo in codigos:
                # separo la clave del valor
                codigo = codigo.split(":")
                # clave es el primer elemento
                clave = codigo[0]

                # se agrega la clave a los registros con 0 registros 
                if clave not in registros:
                    registros[clave] = 0
                # se agrega un registro por aparecion
                registros[clave] += 1

            # Se ordena el diccionario por orden de los items 
            sorted_dict = dict(sorted(registros.items()))

        # Se retorna el diccionario ya organizado
        return sorted_dict

print(pregunta_09())            


