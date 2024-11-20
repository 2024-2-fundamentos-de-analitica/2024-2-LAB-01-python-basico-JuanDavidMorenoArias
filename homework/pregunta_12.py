"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open('files\\input\\data.csv','r') as file:
                # Creacion de un diccionario para los resultados
                sumas = {}
                # Se itera linea por linea del archivo
                for line in file:
                    # se separa los elementos de la linea por espacio
                    linea_extraida = line.split()
                    # letra
                    letra = linea_extraida[0]
                    # codigos
                    codigos = linea_extraida[4].split(',')

                    if letra not in sumas:
                            sumas[letra] = 0

                    for codigo in codigos:
                        partido = codigo.split(':')
                        valor = int(partido[1])

                        sumas[letra] += valor

                return dict(sorted(sumas.items()))    


            