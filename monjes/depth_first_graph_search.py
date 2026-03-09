from Problem import Problem
from Node import Node
from collections import deque
from typing import Optional

def depth_first_graph_search(problem: Problem) -> tuple[Optional[Node], dict]:
    root = Node(state=problem.initial_state)
    frontier = [root]  # LIFO
    explored = set()

    nodes_expanded = 0
    max_space = 1  # empieza con el nodo raíz en frontera

    while frontier:
        node = frontier.pop()
        nodes_expanded += 1

        if problem.goal_test(node.state):
            return node, {
                "nodes_expanded": nodes_expanded,
                "max_space": max_space,
            }

        state_key = tuple(map(tuple, node.state)) if isinstance(node.state, list) else node.state
        explored.add(state_key)

        for child in node.expand(problem):
            child_key = tuple(map(tuple, child.state)) if isinstance(child.state, list) else child.state
            if child_key not in explored and child not in frontier:
                frontier.append(child)

        max_space = max(max_space, len(frontier) + len(explored))

    return None, {"nodes_expanded": nodes_expanded, "max_space": max_space}