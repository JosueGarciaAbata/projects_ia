
from reinas.LocalNQueensProblem import LocalNQueensProblem
from reinas.HillClimbing import hill_climbing
from reinas.Node import Node
from reinas.HillClimbingStochastic import hill_climbing as hill_climbing_stochastic
from reinas.TempleSimulado import temple_simulado


def print_board(state: list[int]) -> None:
    n = len(state)
    horizontal_border = "+" + "---+" * n

    print(horizontal_border)
    for row in range(n):
        row_cells = []
        for col in range(n):
            row_cells.append(" Q " if state[col] == row else " . ")
        print("|" + "|".join(row_cells) + "|")
        print(horizontal_border)

if __name__ == "__main__":
    
    problem = LocalNQueensProblem(n=8)
    # result_node: Node = hill_climbing(problem)
    # result_node: Node = hill_climbing_stochastic(problem)
    result_node: Node = temple_simulado(problem)

    print("Estado inicial (vector):", problem.initial_state)
    print("Tablero inicial:")
    print_board(problem.initial_state)

    print("Estado final (vector):", result_node.state)
    print("Tablero final:")
    print_board(result_node.state)

    print("Conflictos en el estado final:", problem.conflicts(result_node.state))

    pass