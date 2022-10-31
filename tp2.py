def read_file(archi):
    dic_bolsa = {}
    with open(archi, 'r', encoding = 'utf-8') as file:
        for elementos in file:
            h, a, o, i, l = elementos.strip('\n').split(',')
            dic_bolsa[h] = a, o, i, l
            print(dic_bolsa)

diccionario = read_file('bolsa.csv')   
archi = 'bolsa.csv'
print(diccionario)

def monthly_average(accion = 'SATL', diccionario):
 fechas, promedios_mes = monthly_average("SATL", diccionario)

 