"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files\\input\\data.csv','r') as file:
        # Creacion de un diccionario para los resultados
        maximos = {}
        minimos = {}
        # Se itera linea por linea del archivo
        for line in file:
            # se separa los elementos de la linea por espacio
            linea_extraida = line.split()
            # se extrael el primer elemento, la letra
            letra = linea_extraida[0]
            # se extrae el segundo elemento, el numero
            numero = int(linea_extraida[1])
            # con dos diccionarios, organizo mayores y menores por letra
            if letra not in minimos:
                minimos[letra] = numero
            if numero < minimos[letra]:
                minimos[letra] = numero

            if letra not in maximos:
                maximos[letra] = numero
            if numero > maximos[letra]:
                maximos[letra] = numero

        # Se ordena el diccionario por orden de los items 
        sorted_dict = dict(sorted(maximos.items()))

        # agrego los resultados por tuplas con letra, mayor, menor
        resultados = []
        for letra in sorted_dict.keys():
            resultados.append(tuple((letra,maximos[letra],minimos[letra])))

        # se retorna la lista con los resultados
        return resultados
 
