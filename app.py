# leer datos del archivo xls
import pandas as pd


def leer_datos(archivo):
    df = pd.read_excel(archivo)
    return df


def comparar_columna(datos):
    # recorrer todas las filas de la columna 'Email'
    data_filter = []
    for i in range(len(datos)):
        # extraer los valores que no se repiten
        if datos.iloc[i]['Email'] not in datos.iloc[:i]['Email'].values:
            data_filter.append(datos.iloc[i])
    return data_filter


datos = leer_datos('datos.xls')
datos_filtrados = comparar_columna(datos)
print(datos_filtrados)
