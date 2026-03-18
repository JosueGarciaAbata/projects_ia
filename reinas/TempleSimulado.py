import math
import random
import time
from reinas.LocalNQueensProblem import LocalNQueensProblem
from reinas.Node import Node

def temple_simulado(problem: LocalNQueensProblem) -> Node:
    """
    Simulated Annealing (temple simulado).

    Funcionamiento:
    1. Empieza desde un estado inicial.
    2. En cada iteración se elige un vecino aleatorio.
    3. Si el vecino es mejor, se acepta.
    4. Si es peor, puede aceptarse con cierta probabilidad
       que depende de la temperatura.
    5. Con el tiempo la temperatura baja, reduciendo la
       probabilidad de aceptar estados peores.

    Esto permite escapar de óptimos locales al inicio de la
    búsqueda, pero se vuelve más selectivo conforme avanza.
    """

    current = Node(state=problem.initial_state)
    schedule = exp_schedule(k=20, lam=0.005, limit=1000)

    for t in range(1, 1001):
        T = schedule(t)

        if T == 0:
            return current

        # Elegir un vecino aleatorio del estado actual
        neighbors = current.expand(problem)
        next_choice = random.choice(neighbors)

        # Diferencia de calidad entre el vecino y el estado actual
        delta_e = problem.value(next_choice.state) - problem.value(current.state)

         # Si el vecino mejora el estado actual, se acepta
        if delta_e > 0:
            current = next_choice
        else:
            # Si es peor, se acepta con probabilidad e^(ΔE / T)
            prob_e = math.exp(delta_e / T)

            # Generar un número aleatorio entre 0 y 1. Si es menor que prob_e, se acepta el vecino peor.
            if random.random() < prob_e:
                current = next_choice

    return current


def exp_schedule(k=20, lam=0.005, limit=1000):
    """
    Función de enfriamiento exponencial.

    Calcula la temperatura del algoritmo en la iteración t.
    A medida que t aumenta, la temperatura disminuye.

    T(t) = k * e^(-λt)

    k → temperatura inicial
    λ (lambda) → velocidad de enfriamiento
    t → número de iteración
    """

    return lambda t: (k * math.exp(-lam * t) if t < limit else 0)


def temple_simulado_with_metrics(problem: LocalNQueensProblem):
    current = Node(state=problem.initial_state)
    schedule = exp_schedule(k=20, lam=0.005, limit=1000)
    generated_nodes = 0
    start_time = time.perf_counter()

    for t in range(1, 1001):
        T = schedule(t)

        if T == 0:
            execution_time = time.perf_counter() - start_time
            return current, generated_nodes, execution_time

        neighbors = current.expand(problem)
        generated_nodes += len(neighbors)
        next_choice = random.choice(neighbors)

        # Recordemos: menos conflictos el valor es mas alto; mas conflictos el valor es mas bajo.
        delta_e = problem.value(next_choice.state) - problem.value(current.state)

        if delta_e > 0:
            print("Vecino mejor aceptado: ", next_choice.state, "con conflictos:", problem.conflicts(next_choice.state))
            current = next_choice
        else:
            prob_e = math.exp(delta_e / T)

            if random.random() < prob_e:
                print(f"Vecino peor aceptado: {next_choice.state} con {problem.conflicts(next_choice.state)} conflictos. Probabilidad de aceptación: {prob_e:.4f}")
                current = next_choice

    execution_time = time.perf_counter() - start_time
    return current, generated_nodes, execution_time