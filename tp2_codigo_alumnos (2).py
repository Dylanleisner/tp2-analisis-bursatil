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
    Esta funcion devuelve un diccionario con los valores del archivo bolsa.csv La key
    '''
    dic_bolsa = {}
    dic_bolsa2={}
    with open(archi, 'r', encoding = 'utf-8') as file:
        titulos = file.readline().strip().split(',')
        for i in titulos:
            dic_bolsa[i] = []
        for x in file:
            info = x.strip().split(',')
            for key, val in zip(titulos, info):
                if key!="Date":
                    dic_bolsa[key].append(float(val))
                else:
                    dic_bolsa[key].append(val)
    return dic_bolsa

diccionario = read_file('bolsa.csv')   
# print(diccionario)
lista = []
meses =[]
lista11 = []
def monthly(accion, diccionario):
 lista_fechas = str2datetime(diccionario["Date"])
 for index, fechas in enumerate(lista_fechas):
    #  print(index, fechas)
     mes = fechas.month
     for x in str(mes):
         meses_totales = meses.append(x)
         print(meses_totales)
    
    #  if mes == 10:
    #     lista.append(diccionario[accion][index])
    #     promedio = sum(lista)/len(lista)
    #     print(promedio)
    #  elif mes == 11:
    #         lista11.append(diccionario[accion][index])
    #         promedio11 = sum(lista11)/len(lista11)
    #         return promedio11
    #  elif mes == 12:
    #         lista11.append(diccionario[accion][index])
    #         promedio11 = sum(lista11)/len(lista11)
    #         return promedio11


    

accion = "SATL"
print(monthly(accion, diccionario))




