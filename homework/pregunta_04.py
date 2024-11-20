"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    with open('files\\input\\data.csv','r') as file:
        # Creacion de un diccionario para los resultados
        results = {}
        # Se itera linea por linea del archivo
        for line in file:
            # se separa los elementos de la linea por espacio
            linea_extraida = line.split()
            # se extrae el elemento correspondiente a la fecha
            fecha = linea_extraida[2]
            # se separa la fecha por año-mes-dia
            fecha = fecha.split('-')
            # se extrae el mes de la linea separada
            mes = fecha[1]
            # si el mes no se encuentra en el diccionario, se agrega con 0 resgistros
            if mes not in results:
                results[mes] = 0
            # se agrega un registro al mes
            results[mes] += 1
        # Se ordena el diccionario por orden de los items (numero del mes)
        sorted_dict = dict(sorted(results.items()))
        # se retornan los resultados
        return list(sorted_dict.items())
    

