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
lista12 = []
lista11 = []
lista10 = []
lista9 = []
lista8 = []
lista7 = []
lista6 = []
lista5 = []
lista4 = []
lista3 = []
lista2 = []
lista1 = []

meses =[]

def monthly(accion, diccionario):
 lista_fechas = str2datetime(diccionario["Date"])
 for index, fechas in enumerate(lista_fechas):
    #  print(index, fechas)
     mes = fechas.month
     if mes == 10:
        lista10.append(diccionario[accion][index])
        promedio10 = sum(lista10)/len(lista10)
        return promedio10, fechas
        
     elif mes == 11:
            lista11.append(diccionario[accion][index])
            promedio11 = sum(lista11)/len(lista11)
            return promedio11, fechas
     elif mes == 12:
            lista12.append(diccionario[accion][index])
            promedio12 = sum(lista12)/len(lista12)
            return promedio12, fechas
     elif mes == 9:
        lista9.append(diccionario[accion][index])
        promedio9 = sum(lista9)/len(lista9)
        return promedio10, fechas
     elif mes == 8:
            lista8.append(diccionario[accion][index])
            promedio8 = sum(lista8)/len(lista8)
            return promedio8, fechas
     elif mes == 7:
            lista12.append(diccionario[accion][index])
            promedio7 = sum(lista7)/len(lista7)
            return promedio7, fechas
     elif mes == 6:
        lista6.append(diccionario[accion][index])
        promedio6 = sum(lista6)/len(lista6)
        return promedio6, fechas
     elif mes == 5:
            lista5.append(diccionario[accion][index])
            promedio5 = sum(lista5)/len(lista5)
            return promedio5, fechas
     elif mes == 4:
            lista4.append(diccionario[accion][index])
            promedio4 = sum(lista4)/len(lista4)
            return promedio4, fechas
     elif mes == 3:
        lista3.append(diccionario[accion][index])
        promedio3 = sum(lista3)/len(lista3)
        return promedio3, fechas
     elif mes == 2:
            lista2.append(diccionario[accion][index])
            promedio2 = sum(lista2)/len(lista2)
            return promedio2, fechas
     elif mes == 1:
            lista1.append(diccionario[accion][index])
            promedio1 = sum(lista1)/len(lista1)
            return promedio1, fechas


accion = "SATL"
print(monthly(accion, diccionario))

with open('monthly_average_SATL.csv', 'r', encoding = 'utf-8') as file:
    n1= "".join(str(promedio1))
    n2= "".join(str(fechas))
    file.writelines(n1)
    file.writelines(n2)



