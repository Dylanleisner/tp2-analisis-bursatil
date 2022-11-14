""" >>>> NO TOCAR ESTE CÓDIGO >>>> """

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def str2datetime(date, fmt="%Y-%m-%d"):
    """Convierte una cadena (o secuencia de cadenas) a tipo datetime (o secuencia de datetimes).

    ENTRADAS:
        date (str ó secuencia de str): fechas a convertir.
        fmt (str, opcional): formato de fecha (ver documentación de biblioteca datetime).
    SALIDAS:
        output (datetime ó secuencia de datetime): fechas convertidas a datetime.
    EJEMPLOS:
    >>>> date = str2datetime('2022-10-24')
    >>>> print(date.year, date.month, date.day)

    >>>> date = str2datetime(['2022-10-24', '2022-10-23', '2022-10-22'])
    >>>> print(len(date))"""
    if isinstance(date, str):
        return datetime.strptime(date, fmt)
    elif isinstance(date, (list, np.ndarray)):
        output = []
        for d in date:
            output.append(datetime.strptime(d, fmt))
        if isinstance(date, np.ndarray):
            output = np.array(output)
        return output


def datetime2str(date, fmt="%Y-%m-%d"):
    """Convierte un datetime (o secuencia de datetimes) a tipo str (o secuencia de str).

    ENTRADAS:
        date (datetime ó secuencia de datetime): fechas a convertir.
        fmt (str, opcional): formato de fecha (ver documentación de biblioteca datetime).
    SALIDAS:
        output (str ó secuencia de str): fechas convertidas a cadenas.
    EJEMPLOS:
    >>>> date_str = '2022-10-24'
    >>>> date = str2datetime(date_str)
    >>>> print(datetime2str(date) == date_str)"""
    if isinstance(date, datetime):
        return date.strftime(fmt)
    elif isinstance(date, (list, np.ndarray)):
        output = []
        for d in date:
            output.append(d.strftime(fmt))
        if isinstance(date, np.ndarray):
            output = np.array(output)
        return output


""" >>>> DEFINAN SUS FUNCIONES A PARTIR DE AQUÍ >>>> """


""" >>>> ESCRIBAN SU CÓDIGO A PARTIR DE AQUÍ >>>> """


def read_file(archi):
    '''
    Esta funcion devuelve un diccionarios con la informacion brindada del archivo bolsa.csv en donde las llaves son los nombres de la columna del archivo y los valores son los datos de cada columna
    '''
    dic_bolsa = {}
    dic_bolsa2 = {}
    with open(archi, 'r', encoding='utf-8') as file:
        titulos = file.readline().strip().split(',')
        for i in titulos:
            dic_bolsa[i] = []
        for x in file:
            info = x.strip().split(',')
            for key, val in zip(titulos, info):
                if key != "Date":
                    dic_bolsa[key].append(float(val))
                else:
                    dic_bolsa[key].append(str2datetime(val))
    return dic_bolsa


diccionario = read_file('bolsa.csv')


def monthly_average(accion, diccionario):
    '''
    Esta funcion devuelve dos datos. Por un lado las fechas del primer dia de cada mes y por el otro el promedio del precio de cada accion.
    '''

    lista_precios_mes = {}
    for i in range(len(diccionario['Date'])):
        fecha_i = diccionario['Date'][i]
        precio_i = diccionario[accion][i]
        clave = datetime(fecha_i.year, fecha_i.month, 1)
        if clave not in lista_precios_mes:
            lista_precios_mes[clave] = [precio_i]
        else:
            lista_precios_mes[clave].append(precio_i)

    lista_fechas = list(lista_precios_mes.keys())
    lista_precios_promedios_mes = []

    for precios_mes in lista_precios_mes.values():
        lista_precios_promedios_mes.append(sum(precios_mes) / len(precios_mes))

    return lista_fechas, lista_precios_promedios_mes

with open("monthly_average_SATL.csv", 'w', encoding = 'utf-8') as my_file:
    '''
    Esta funcion genera un archivo o si ya existe lo sobre escribe con los datos de la funcion anterior.

    '''
    lista_fechas, lista_precios_promedio = monthly_average('SATL', diccionario)
    for i in range(len(lista_fechas)):
        my_file.write(f"{lista_precios_promedio[i]},{lista_fechas[i]}\n")


def max_gain(accion, diccionario, fecha_venta):
    '''
    Esta funcion busca la fecha de compra donde se hubiera generado la mayor ganancia, devuelve la misma con su retorno de inversion

    '''
  
    indice_de_fecha_de_venta = diccionario['Date'].index(fecha_venta)
    precio_de_venta = diccionario[accion][indice_de_fecha_de_venta]

    fecha_de_ganancia_maxima = diccionario['Date'][0]
    ganancia_maxima = float('-inf')

    for i in range(len(diccionario['Date'])):
        fecha_i = diccionario['Date'][i]
        if (fecha_i >= fecha_venta):
            break
        precio_de_compra_i = diccionario[accion][i]
        ganancia_en_fecha_i = (precio_de_venta - precio_de_compra_i) / precio_de_compra_i
        if (ganancia_en_fecha_i > ganancia_maxima):
            ganancia_maxima = ganancia_en_fecha_i
            fecha_de_ganancia_maxima = fecha_i
    return fecha_de_ganancia_maxima, ganancia_maxima


def report_max_gains(diccionario, fecha_de_venta):
    '''
    Esta funcion genera un archivo que se escribe un informe relacionado a la mayor ganancia de todas las acciones.

    '''
    with open('resumen_mejor_compra.txt', 'w') as my_file:
        for key in diccionario.keys():
            if key == 'Date':
                continue
            fecha_de_compra, ganancia = max_gain(key, diccionario, fecha_de_venta)
            my_file.write(f'{key} genera una ganancia de {ganancia*100}% habiendo comprando en {fecha_de_compra} y vendiendose en {fecha_de_venta}\n')

report_max_gains(diccionario, datetime(2022,6,6))

def plot_price(accion, diccionario, start="2022-01-01", end="2022-06-01"):
    '''
    Esta funcion genera un grafico de lineas sobre una accion en donde representa las fechas y su precio.

    '''
    fechas = diccionario['Date']
    precios = diccionario[accion]
    
    plt.figure()
    plt.plot(fechas, precios, color='g')
    plt.xlim(str2datetime(start), str2datetime(end))
    plt.savefig(f'price_{accion}.png')

plot_price('SATL',diccionario)

def monthly_average_bar_plot(accion, diccionario):
    '''
    Esta funcion genera un grafico de barras con el precio promedio de la accion mes a mes.

    '''
    fechas, precios_promedios = monthly_average(accion, diccionario)

    plt.figure()
    plt.title(f'Precio Promedio por Mes de {accion}')
    plt.bar(fechas, precios_promedios, 20)
    plt.savefig(f'monthly_average_bar_plot_{accion}.png')

monthly_average_bar_plot('SATL', diccionario)

def plot_max_gains(diccionario, fecha_de_venta):
    '''
    Esta funcion genera un grafico de barras donde cada una representa la ganancia de la ganancia de la mejor inversion de su respectiva accion

    '''
    ganancias = {}
    for key in diccionario.keys():
        if key == 'Date':
            continue
        _, ganancia = max_gain(key, diccionario, fecha_de_venta)
        ganancias[key] = ganancia

    plt.figure()
    plt.bar(ganancias.keys(), ganancias.values())
    plt.savefig('max_gains.png')

plot_max_gains(diccionario, datetime(2022,6,6))