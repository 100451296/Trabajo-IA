# Simulación del termostato
import random

# Definir los estados
OFF = 0
ON = 1

# Temperatura deseada por el usuario
temp_deseada = 22

# Temperatura inicial de la habitación
temp_actual = 20

# Definir límites de temperatura
temp_min = 16
temp_max = 25

# Definir la política óptima
if temp_actual < temp_deseada:
    politica_optima = ON
else:
    politica_optima = OFF

# Definir la duración de la simulación en intervalos de 30 minutos
duracion_simulacion = 6

# Iniciar la simulación
for i in range(duracion_simulacion):
    print("Hora: " + str(i*30) + " minutos")
    
    # Calcular la temperatura después de media hora
    if politica_optima == ON:
        probabilidad = random.random()
        if temp_actual == temp_min:
            if probabilidad <= 0.5:
                temp_nueva = temp_min
            else:
                temp_nueva = temp_min + 0.5
        elif temp_actual == temp_max:
            if probabilidad <= 0.1:
                temp_nueva = temp_max - 0.5
            else:
                temp_nueva = temp_max
        elif temp_actual == 24.5:
            if probabilidad <= 0.2:
                temp_nueva = temp_actual
            else:
                temp_nueva = temp_actual + 0.5
        else:
            if probabilidad <= 0.2:
                temp_nueva = temp_actual - 0.5
            elif probabilidad <= 0.4:
                temp_nueva = temp_actual
            elif probabilidad <= 0.6:
                temp_nueva = temp_actual + 0.5
            else:
                temp_nueva = temp_actual + 1
    else:
        probabilidad = random.random()
        if temp_actual == temp_min:
            temp_nueva = temp_min
        elif temp_actual == temp_max:
            if probabilidad <= 0.3:
                temp_nueva = temp_max
            else:
                temp_nueva = temp_max - 0.5
        else:
            if probabilidad <= 0.3:
                temp_nueva = temp_actual
            elif probabilidad <= 0.6:
                temp_nueva = temp_actual - 0.5
            else:
                temp_nueva = temp_actual + 0.5
    
        
    # Actualizar la temperatura actual
    if temp_nueva >= temp_min and temp_nueva <= temp_max:
        temp_actual = temp_nueva
    
    # comprobar si se sobrepaso la temperatura deseada
    if temp_nueva > temp_deseada:
        politica_optima = OFF

    # Imprimir los resultados
    print("Temperatura actual: " + str(temp_actual))
    print("Política óptima: " + str(politica_optima))
    print()

    # Verificar si se alcanzó la temperatura deseada
    if temp_nueva == temp_deseada:
        print("temperatura deseada alcanzada")
        break

