def read_file(archi):
    bolsa= []
    dic_bolsa = {}
    with open(archi, 'r', encoding = 'utf-8') as file:
        for elementos in file:
            lineas_bolsa = elementos.strip('\n').split(',')
            
        
archi = 'bolsa.csv'
print(read_file(archi))


def max_sueldo(la):
    dic = 0
    p =''
    with open(la, 'r', encoding = 'utf-8') as file:
        for x in file:
            linea= x.strip().split(',')
            print(linea)
            if float(linea[1]) > dic:
                dic = float(linea[1])
                p = linea[0]
    return [p,dic]