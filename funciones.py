import csv
import os
import random as rnd

PATH = os.getcwd()
CSV_ENCENDIDO = PATH + "/ENCENDIDO.csv"
CSV_APAGADO = PATH + "/APAGADO.csv"
CSV_PATH = PATH + "/Transiciones"
INPUTS_PATH = PATH + "/inputs"

COSTE_APAGAR = 750
COSTE_ENCENDIDO = 1500

COSTES = [COSTE_ENCENDIDO, COSTE_APAGAR]

MARGEN = 0.001

INDICES = dict()

TRANSICIONES_INDEX = dict()
APAGADO_KEY = "APAGADO.csv"
ENCENDIDO_KEY = "ENCENDIDO.csv"

INDICES_ACCIONES = dict()

def trasiciones_list():
    """Una lista con todas las matrices de transicion para cada accion"""
    transiciones = []
    i = 0
    for raiz, directorios, archivos in os.walk(CSV_PATH):
        for nombre_archivo in archivos:
            ruta_completa = os.path.join(raiz, nombre_archivo)
            transiciones.append(leer_csv(ruta_completa))
            TRANSICIONES_INDEX[nombre_archivo] = i
            i += 1

    for key in TRANSICIONES_INDEX.keys():
        INDICES_ACCIONES[TRANSICIONES_INDEX[key]] = key.split(".")[0]
    return transiciones

def leer_csv(path: str) -> list:
    """Lee un archivo csv y devuelve una matriz con su contenido"""
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
        INDICES[i-1] = key

    return matriz

def bellman(v_valores, transiciones):
    """Calcula los v_valores mediante Bellman"""
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
    """Calcula los v_valores iterando hasta que la diferencia sea menor al margen. Llama a bellman en cada iteracion"""
    anterior = 100
    acciones = list()

    while abs(sum(v_valores) - anterior) > MARGEN:
        anterior = sum(v_valores)
        acciones = bellman(v_valores, transiciones)

    return acciones

def init_valores():
    """Inicializa la lista de valores a 0"""
    valores = list()
    for estado in range(len(INDICES)):
        valores.append(0)
    return valores 

def espaciado(len, num_espacios=5):
    """Devuelve un string de num_espacios caracteres, rellena con espacios lo que falte a partir de la longitud de la cadena"""
    espacio = ""
    
    for i in range(num_espacios - len):
        espacio += " "

    return espacio

def result(acciones, valores):
    """Muestra con consola los resultados obtenidos"""
    print("******************************************************")
    print(" V VALORES PARA CADA ESTADO")
    print("******************************************************")
    
    for key in INDICES.keys():
        print("    ", INDICES[key],espaciado(len(INDICES[key])),  "|", valores[key])

    print("\n")
    print("*******************************************************")
    print(" POLITICA OPTIMA PARA CADA ESTADO")
    print("*******************************************************")

    for key in INDICES.keys():
        print("    ", INDICES[key],espaciado(len(INDICES[key])),  "|", INDICES_ACCIONES[acciones[key]])

    print("\n")

def test(acciones, iter=1):
    """Muestra la politica optima para iter estados al azar"""
    print("*******************************************************")
    print(" TEST", f"({iter} iteraciones)")
    print("*******************************************************")

    for _ in range(iter):
        estado = rnd.randint(0, len(INDICES)-1)
        accion = INDICES_ACCIONES[acciones[estado]]

        if accion == "ENCENDIDO":
            print("Temperatura actual:", INDICES[estado], "\033[92mSe tomará la acción ->", accion, "\033[0m")
        else:
            print("Temperatura actual:", INDICES[estado], "\033[91mSe tomará la acción ->", accion, "\033[0m")

    print()

    

if __name__  == "__main__":
    transiciones = trasiciones_list()

    print(TRANSICIONES_INDEX)