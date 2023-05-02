import csv
import os

PATH = os.getcwd()
CSV_ENCENDIDO = PATH + "/ENCENDIDO.csv"
CSV_APAGADO = PATH + "/APAGADO.csv"

COSTE_APAGAR = 4000
COSTE_ENCENDIDO = 35

COSTES = [COSTE_APAGAR, COSTE_ENCENDIDO]

MARGEN = 0.001

INDICES = dict()

def leer_csv_en_directorio(directorio):
    transiciones_apagado = []
    transiciones_encendido = []
    for archivo in os.listdir(directorio):
        if archivo.endswith('.csv'):
            ruta = os.path.join(directorio, archivo)
            with open(ruta, 'r') as file:
                lector_csv = csv.reader(file)
                for fila in lector_csv:
                    if(archivo == "APAGADO.csv"):
                        transiciones_apagado.append(fila)
                    elif(archivo == "ENCENDIDO.csv"):
                        transiciones_encendido.append(fila)
    """
    print(transiciones_apagado)
    print("\n")
    print(transiciones_encendido)
    """
    print([transiciones_apagado, transiciones_encendido])

def leer_csv(path: str) -> list:
    global INDICES  # declarar que se utilizará la variable global
    
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
        
        # Agregar los índices correspondientes a la variable global INDICES
        key = str(data[i][0])
        INDICES[key] = i-1

    return matriz

def bellman(v_valores, transiciones):
    valores = list()
    valor = float()
    acumulacion = 0
    acciones_optimas = list()

    for accion in range(len(transiciones)):
        for estado in range(len(transiciones[accion])):
            for probabilidad in range(len(v_valores)):
                if probabilidad == 0:
                    acumulacion = 0
                    valor = 0
                    valor += COSTES[accion]
                    
                valor += transiciones[accion][estado][probabilidad] * v_valores[probabilidad]
                acumulacion += transiciones[accion][estado][probabilidad]

            if acumulacion == 0:
                valor = acumulacion
            if accion == 0:
                valores.append([valor])
            else:
                valores[estado].append(valor)
    
    for v in range(len(valores)):
        acciones_optimas.append(valores[v].index(min(valores[v])))
        v_valores[v] = min(valores[v])
        

    return acciones_optimas

def iter_bellman(v_valores, transiciones):

    anterior = 100
    acciones = list()

    while abs(sum(v_valores) - anterior) > MARGEN:
        anterior = sum(v_valores)
        acciones = bellman(v_valores, transiciones)

    return acciones

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
