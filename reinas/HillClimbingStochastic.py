import random
import time
from typing import List

from reinas.LocalNQueensProblem import LocalNQueensProblem
from reinas.Node import Node

def hill_climbing(problem: LocalNQueensProblem) -> Node:
    """
    Hill Climbing estocástico (con selección ponderada).

    Idea:
    - Parte de un estado inicial.
    - Genera todos los vecinos posibles.
    - Solo considera los vecinos que mejoran el estado actual.
    - Entre esos vecinos, elige uno aleatoriamente con probabilidad
      proporcional a cuánto mejora la solución.

    Termina cuando no existen vecinos mejores (óptimo local o solución).
    """

    # Nodo actual de la búsqueda
    current = Node(state=problem.initial_state)

    while True:
        candidates: List[Node] = []   # vecinos que mejoran el estado
        weights: List[int] = []      # cuánto mejora cada vecino

        # Valor del estado actual (en N-Reinas: value = -conflicts)
        current_value = problem.value(current.state)

        # Generar todos los vecinos del estado actual
        for action in problem.actions(current.state):
            neighbor = current.child_node(problem, action)

            # Mejora respecto al estado actual
            improvement = problem.value(neighbor.state) - current_value

            # Solo guardamos vecinos que mejoran la solución
            if improvement > 0:
                candidates.append(neighbor)
                weights.append(improvement)

        # Si no hay vecinos mejores, se alcanzó un óptimo local
        if not candidates:
            print("No se encontraron vecinos mejores. Terminando.")
            return current

        # Elegir un vecino al azar, favoreciendo los que mejoran más
        current = weighted_choice(candidates, weights)


def weighted_choice(candidates: List[Node], weights: List[int]) -> Node:
    """
    Selecciona un vecino aleatoriamente usando pesos.

    Vecinos con mayor mejora tienen mayor probabilidad de ser elegidos.
    """
    return random.choices(candidates, weights=weights, k=1)[0]

def hill_climbing_with_metrics(problem: LocalNQueensProblem):

    current = Node(state=problem.initial_state)

    generated_nodes = 0
    start_time = time.perf_counter()

    while True:
        candidates: List[Node] = []
        weights: List[int] = []

        current_value = problem.value(current.state)

        for action in problem.actions(current.state):
            neighbor = current.child_node(problem, action)
            generated_nodes += 1

            improvement = problem.value(neighbor.state) - current_value

            if improvement > 0:
                print(f"Vecino que mejora: {neighbor.state} con {problem.conflicts(neighbor.state)} conflictos.")
                candidates.append(neighbor)
                weights.append(improvement)

        if not candidates:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print("No se encontraron vecinos mejores. Terminando con el estado: ", current.state, "con conflictos:", problem.conflicts(current.state))
            return current, generated_nodes, execution_time

        current = weighted_choice(candidates, weights)