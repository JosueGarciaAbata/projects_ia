from reinas.LocalNQueensProblem import LocalNQueensProblem
from reinas.HillClimbing import hill_climbing_with_metrics
from reinas.HillClimbingStochastic import hill_climbing_with_metrics as hill_climbing_stochastic_with_metrics
from reinas.TempleSimulado import temple_simulado_with_metrics


def print_board(state: list[int]) -> None:
    n = len(state)
    horizontal_border = "+" + "-+" * n

    print(horizontal_border)
    for row in range(n):
        row_cells = []
        for col in range(n):
            row_cells.append("Q" if state[col] == row else ".")
        print("|" + "|".join(row_cells) + "|")
        print(horizontal_border)

if __name__ == "__main__":

    problem = LocalNQueensProblem(n=8)
    result_node, generated_nodes, execution_time = temple_simulado_with_metrics(problem)
    # result_node, generated_nodes, execution_time = hill_climbing_with_metrics(problem)
    # result_node, generated_nodes, execution_time = hill_climbing_stochastic_with_metrics(problem)

    print("Estado inicial (vector):", problem.initial_state)
    print("Tablero inicial:")
    print_board(problem.initial_state)

    print("Estado final (vector):", result_node.state)
    print("Tablero final:")
    print_board(result_node.state)

    print("Conflictos finales:", problem.conflicts(result_node.state))
    print("Vecinos generados:", generated_nodes)
    print("Tiempo de ejecución:", execution_time, "segundos")