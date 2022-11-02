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
# print(diccionario)

def monthly(accion, diccionario):
    lista = []
    for index in diccionario['Date']:  
        if index[5] == '1' and index[6] == '0': 
            if accion in diccionario.keys():
                
                

            #  for x in diccionario["SATL"]:
            #   print(x) 
       
                 print(x) 
        
         
        
        for x in accion:
             

accion = "SATL"
print(monthly(accion, diccionario))



