import csv
from funciones import *




if __name__ == "__main__":

    transiciones_apagado = leer_csv(CSV_APAGADO)
    transiciones_encendido = leer_csv(CSV_ENCENDIDO)

    print(len(transiciones_apagado))

        
        
