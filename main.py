import csv
from funciones import *




if __name__ == "__main__":

    
    transiciones = trasiciones_list()

    valores = init_valores()

    acciones = iter_bellman(valores, transiciones)

    result(acciones, valores)

    test(acciones, iter=10)