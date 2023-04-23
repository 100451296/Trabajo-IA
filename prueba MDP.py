import random
def frange(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step
# Definir los estados
states = list(frange(16, 25, 0.5))

# Definir las acciones
actions = [0, 1]  # 0 es apagar el termostato y 1 es encender el termostato

# Temperatura deseada por el usuario
temp_deseada = 22

# Definir límites de temperatura
temp_min = 16
temp_max = 25

# Definir la función de recompensa
def reward_function(state):
    if state == temp_deseada:
        return 0
    else:
        return -1

# Definir la función de transición
#esto cambiarlo para que utilice las tablas que tenemos en vez de crearlas de cero
def transition_function(state, action):
    if action == 0:  # apagar el termostato
        if state == temp_min:
            return [(temp_min, 1.0)]
        else:
            return [(state - 0.5, 0.7), (state, 0.2), (state + 0.5, 0.1)]
    else:  # encender el termostato
        if state == temp_max:
            return [(temp_max, 1.0)]
        elif state == 24.5:
            return [(state - 0.5 ,0.1), (state, 0.2), (state + 0.5, 0.7)]
        else:
            return [(state - 0.5, 0.1), (state, 0.3), (state + 0.5, 0.6)]

# Definir la política óptima utilizando la ecuación de Bellman
def optimal_policy(state, value_function):
    q_values = []
    for action in actions:
        transitions = transition_function(state, action)
        q_value = sum([transition[1] * (reward_function(transition[0]) + value_function[states.index(transition[0])]) for transition in transitions])
        q_values.append(q_value)
    
    print(q_values)
    return actions[q_values.index(max(q_values))]

# Inicializar la función de valor
value_function = [0] * len(states)

# Iniciar la simulación
temp_actual = states[random.randint(0,len(states)-1)]
print("temperatura inicial: " + str(temp_actual))
i = 0
while True:
    state_index = states.index(temp_actual)
    action = optimal_policy(temp_actual, value_function)
    if temp_actual < 16:
        temp_actual = 16
    if temp_actual > 25:
        temp_actual = 25
    transitions = transition_function(temp_actual, action)
    prob, next_state = zip(*transitions)
    next_state_index = random.randrange(len(prob), len(states))
    reward = reward_function(states[next_state_index])
    value_function[state_index] = reward + max([transition[1] * value_function[states.index(transition[0])] for transition in transitions])
    temp_actual = states[next_state_index]

    # Imprimir por pantalla los resultados
    print("Intervalo de tiempo: ", i+1)
    print("Estado actual: ", temp_actual)
    #print("Valor de la función de valor: ", value_function)
    print("Política óptima: ", action)
    i += 1
    if temp_actual == temp_deseada:
        print("temperatura deseada alcanzada")
        break

