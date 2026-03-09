from Node import Node

def depth_limited_search(problem, limit, counters: dict):
    def recursive_dls(node, limit):
        if problem.goal_test(node.state):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                counters["nodes_expanded"] += 1
                counters["max_depth_reached"] = max(counters["max_depth_reached"], child.depth)
                result = recursive_dls(child, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    root = Node(state=problem.initial_state)
    counters["nodes_expanded"] += 1
    return recursive_dls(root, limit)


def iterative_deepening_search(problem) -> tuple:
    counters = {"nodes_expanded": 0, "max_depth_reached": 0, "iterations": 0}

    depth = 0
    while True:
        counters["iterations"] += 1
        result = depth_limited_search(problem, depth, counters)
        if result != 'cutoff':
            return result, {
                **counters,
            }
        depth += 1