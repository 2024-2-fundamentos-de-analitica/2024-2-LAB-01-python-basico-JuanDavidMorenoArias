"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

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
            
            # solo se agrega una nueva letra si no estaba asociada antes.
            if letra not in results[numero]:
                results[numero] += letra

            # cada vez se reorganiza la lista asociada al numero
            results[numero] = sorted(results[numero])


            # Se ordena el diccionario por orden de las claves (numeros)
            sorted_dict = dict(sorted(results.items()))
            
        return list(sorted(sorted_dict.items()))
