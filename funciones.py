import csv
import os

PATH = os.getcwd()
CSV_ENCENDIDO = PATH + "/ENCENDIDO.csv"
CSV_APAGADO = PATH + "/APAGADO.csv"

COSTE_APAGAR = 1
COSTE_ENCENDIDO = 2

INDICES = {
    "16" : 0,
    "16.5" : 1,
    "17" : 2,
    "17.5" : 3,
    "18" : 4,
    "18.5" : 5,
    "19" : 6,
    "19.5" : 7,
    "20" : 8,
    "20.5" : 9,
    "21" : 10,
    "21.5" : 11,
    "22" : 12,
    "22.5" : 13,
    "23" : 14,
    "23.5" : 15,
    "24" : 16,
    "24.5" : 17,
    "25" : 18,
}

def leer_csv(path: str) -> list:
     # Abre el archivo csv
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        # Crea una lista vacía para almacenar los datos
        data = []
        
        # Lee cada fila del archivo csv y agrega los valores a la lista de datos
        for row in reader:
            data.append(row)
            
    # Convierte los valores de cadena a flotantes
    for i in range(1, len(data)):
        for j in range(1, len(data[i])):
            data[i][j] = float(data[i][j])
            
    # Crea una matriz a partir de los datos
    matriz = []
    for i in range(1, len(data)):
        matriz.append(data[i][1:])


    return matriz



if __name__  == "__main__":
    a=leer_csv(CSV_APAGADO)
    print("matriz apagado:")
    print(a)
    print()
    b=leer_csv(CSV_ENCENDIDO)
    print("matriz encendido:")
    print(b)
    print()
    pass
