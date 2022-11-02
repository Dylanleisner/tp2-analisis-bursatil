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
                dic_bolsa[key].append(val)
    return dic_bolsa

diccionario = read_file('bolsa.csv')   
print(diccionario)
def monthly(accion, diccionario):
    

# def monthly_average(diccionario, accion):
#     for x in diccionario:
#         if


#  fechas, promedios_mes = monthly_average("SATL", diccionario)


# QUE tinee que devolver el dic 
# Como uso lo que ponen en el tp
 