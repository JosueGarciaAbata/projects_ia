from monjes_cavernicolas_problema import MonjesCavernicolasProblema
from Problem import Problem

from depth_first_graph_search import depth_first_graph_search
from breadth_first_graph_search import breadth_first_graph_search
from bidirectional_breadth_first_graph_search import bidirectional_breadth_first_graph_search
from iterative_deepening_search import iterative_deepening_search

if __name__ == "__main__":

  problem: Problem = MonjesCavernicolasProblema()
  #goal_node, metrics = breadth_first_graph_search(problem)
  #goal_node, metrics = depth_first_graph_search(problem)
  #goal_node, metrics = iterative_deepening_search(problem)
  goal_node, metrics = bidirectional_breadth_first_graph_search(problem)

  if goal_node is None:
    print("No se encontró solución.")
  else:

    plan = goal_node.solution()
    print("\nPlan encontrado:")

    states: list = [n.state for n in goal_node.path()]

    print("Estado inicial: ", problem.initial_state)
    print("Estado objetivo: ", problem.goal_state)
    print("\nPlan de acciones:", plan)

    print("\nCamino recorrido:")
    for i, state in enumerate(states):
      print(f"  Paso {i + 1}: {state}")

    print ("Profundidad del nodo objetivo: ", goal_node.depth)
    print("Coste del camino: ", goal_node.path_cost)
    print("\nMétricas de búsqueda:", metrics)