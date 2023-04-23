# Simulación del termostato
import random

# Definir los estados
OFF = 0
ON = 1

# Temperatura deseada por el usuario
temp_deseada = 22

# Temperatura inicial de la habitación
temp_actual = random.randint(16,25)
print("temperatura inicial: " + str(temp_actual))
print()
# Definir límites de temperatura
temp_min = 16
temp_max = 25

# Definir la política óptima
if temp_actual < temp_deseada:
    politica_optima = ON
else:
    politica_optima = OFF

# Definir la duración de la simulación en intervalos de 30 minutos
duracion_simulacion = 20

# Iniciar la simulación
i = 0
while True:
    print("Hora: " + str(i*30) + " minutos")
    print("ciclo: " + str(i))
    i += 1
    probabilidad = random.random()
    # Calcular la temperatura después de media hora
    if politica_optima == ON:
        #si estamos en 16 grados (temperatura minima)
        if temp_actual == temp_min:
            #50% sube .5 grados
            if probabilidad <= 0.5:
                temp_nueva = temp_actual + 0.5
            #20% sube 1 grado
            elif probabilidad <=0.7:
                temp_nueva = temp_min + 1
            #30% no cambia
            else:
                temp_nueva = temp_actual
        elif temp_actual == temp_max:
            #10% baja
            if probabilidad <= 0.1:
                temp_nueva = temp_max - 0.5
            #90% se queda igual
            else:
                temp_nueva = temp_max
        elif temp_actual == 24.5:
            #20% se queda igual
            if probabilidad <= 0.2:
                temp_nueva = temp_actual
            #10% baja .5 grados
            elif probabilidad <=0.3:
                temp_nueva = temp_actual - 0.5
            #70% sube .5 grados
            else:
                temp_nueva = temp_actual +0.5
        else:
            #10% baja .5 grados
            if probabilidad <= 0.1:
                temp_nueva = temp_actual - 0.5
            #20% no cambia
            elif probabilidad <= 0.3:
                temp_nueva = temp_actual
            #20% sube 1 grado
            elif probabilidad <= 0.5:
                temp_nueva = temp_actual + 1
            #50% sube .5 grados
            else:
                temp_nueva = temp_actual + 0.5
    else:
        if temp_actual == temp_min:
            #90% se queda igual
            if probabilidad <= 0.9:
                temp_nueva = temp_min
            #10% sube .5 grados
            else:
                temp_nueva = temp_actual + 0.5

        elif temp_actual == temp_max:
            #30% se queda igual
            if probabilidad <= 0.3:
                temp_nueva = temp_max
            #70% se queda igual
            else:
                temp_nueva = temp_max - 0.5
        else:
            #70% baja .5 grados
            if probabilidad <= 0.7:
                temp_nueva = temp_actual -0.5
            #10% sube .5 grados
            elif probabilidad <= 0.8:
                temp_nueva = temp_actual + 0.5
            #20% se queda igual
            else:
                temp_nueva = temp_actual
    
        
    # Actualizar la temperatura actual
    temp_actual = temp_nueva
    
    # comprobar si se sobrepaso la temperatura deseada
    if temp_nueva > temp_deseada:
        politica_optima = OFF

    #comprobar si estoy por debajo de la temperatura deseada
    if temp_nueva < temp_deseada:
        politica_optima = ON

    # Imprimir los resultados
    print("Temperatura actual: " + str(temp_actual))
    print("Política óptima: " + str(politica_optima))
    print()

    # Verificar si se alcanzó la temperatura deseada
    if temp_nueva == temp_deseada:
        print("temperatura deseada alcanzada")
        break

