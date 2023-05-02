import csv
from funciones import *




if __name__ == "__main__":

    """
    transiciones_apagado = leer_csv(CSV_APAGADO)
    transiciones_encendido = leer_csv(CSV_ENCENDIDO)

    transiciones = [transiciones_apagado, transiciones_encendido]
    
    
    print("Apagado:", transiciones_apagado, "\n\nEncendido:", transiciones_encendido)
    print("\n\n", INDICES)
    print("\n\n", "Indices:", len(INDICES), "\nMatriz:", len(transiciones_apagado))
    

    valores = list()
    for estado in range(len(transiciones[0])):
        valores.append(0)


    print(valores)
    acciones = iter_bellman(valores, transiciones)

    print("Valores:", valores, "\nAcciones:", acciones)
    """
   
    ruta_directorio = 'Transiciones'
    ruta_absoluta_directorio = os.path.abspath(ruta_directorio)
    leer_csv_en_directorio(ruta_absoluta_directorio)
