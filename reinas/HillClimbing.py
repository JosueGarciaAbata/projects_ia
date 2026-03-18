import time

from reinas.LocalNQueensProblem import LocalNQueensProblem
from reinas.Node import Node

def hill_climbing(problem: LocalNQueensProblem) -> Node:
  """
    Hill Climbing determinista.

    Funcionamiento:
    1. Empieza desde un estado inicial del tablero.
    2. Genera todos los vecinos posibles (moviendo una reina).
    3. Elige el vecino con menos conflictos.
    4. Si ese vecino mejora al estado actual, se mueve a él.
    5. Si ningún vecino es mejor, el algoritmo se detiene.

    Nota:
    El algoritmo puede terminar en un óptimo local si no existe
    un vecino que mejore el estado actual.
    """

  current = Node(state=problem.initial_state)
  while True:
    best_neighbor = current

    # Explorar todos los vecinos del estado actual
    for action in problem.actions(current.state):
      neighbor = current.child_node(problem, action)

      # Si el vecino es mejor que el mejor vecino encontrado hasta ahora, lo guardamos.
      if problem.conflicts(neighbor.state) < problem.conflicts(best_neighbor.state):
        best_neighbor = neighbor

    # Solo conviene avanzar si el vecino es mejor que el estado actual.
    if problem.conflicts(best_neighbor.state) >= problem.conflicts(current.state):
      return current

    # Avanzamos al mejor vecino encontrado
    current = best_neighbor


def hill_climbing_with_metrics(problem: LocalNQueensProblem):

    current = Node(state=problem.initial_state)
    generated_nodes = 0

    start_time = time.perf_counter()

    while True:
        best_neighbor = current

        for action in problem.actions(current.state):
            neighbor = current.child_node(problem, action)
            generated_nodes += 1

            if problem.conflicts(neighbor.state) < problem.conflicts(best_neighbor.state):
                print(f"Mejor vecino encontrado: {neighbor.state} con {problem.conflicts(neighbor.state)} conflictos.")
                best_neighbor = neighbor

        if problem.conflicts(best_neighbor.state) >= problem.conflicts(current.state):

            end_time = time.perf_counter()
            execution_time = end_time - start_time

            print("Terminando con el vecino: ", best_neighbor.state, "con conflictos:", problem.conflicts(best_neighbor.state))
            return current, generated_nodes, execution_time

        current = best_neighbor