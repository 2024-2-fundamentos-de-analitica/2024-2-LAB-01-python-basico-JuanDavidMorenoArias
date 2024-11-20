"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open('files/input/data.csv','r') as file:
        # Creacion de un diccionario para los resultados
        maximos = {}
        minimos = {}
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
                # el valor es el segundo elemento
                valor = int(codigo[1])

                # con dos diccionarios, organizo mayores y menores por codigo
                if clave not in minimos:
                    minimos[clave] = valor
                if valor < minimos[clave]:
                    minimos[clave] = valor

                if clave not in maximos:
                    maximos[clave] = valor
                if valor > maximos[clave]:
                    maximos[clave] = valor
            

        # Se ordena el diccionario por orden de los items 
        sorted_dict = dict(sorted(maximos.items()))

        # agrego los resultados por tuplas con clave, mayor, menor
        resultados = []
        for clave in sorted_dict.keys():
            resultados.append(tuple((clave,minimos[clave],maximos[clave])))

        # se retorna la lista con los resultados
        return resultados

