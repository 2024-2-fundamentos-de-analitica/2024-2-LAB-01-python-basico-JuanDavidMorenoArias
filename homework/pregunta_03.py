"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

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
            # Se agregan los elementos al diccionario con su suma progresiva
            if letra not in results:
                results[letra] = 0
            results[letra] += numero
        # Se ordena el diccionario por orden de los items
        sorted_dict = dict(sorted(results.items()))
        # se retornan los resultados
        return list(sorted_dict.items())
