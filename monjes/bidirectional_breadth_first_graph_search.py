from collections import deque
from typing import Any, Deque, Dict, Optional, Tuple

from Problem import Problem
from Node import Node


def bidirectional_breadth_first_graph_search(problem: Problem) -> tuple[Optional[Node], dict]:
    if problem.initial_state == problem.goal_state:
        return Node(problem.initial_state), {"nodes_expanded": 0, "max_space": 1}

    start_node = Node(problem.initial_state)
    goal_node = Node(problem.goal_state)

    frontier_start: Deque[Node] = deque([start_node])
    frontier_goal: Deque[Node] = deque([goal_node])

    visited_start: Dict[Any, Node] = {start_node.state: start_node}
    visited_goal: Dict[Any, Node] = {goal_node.state: goal_node}

    counters = {"nodes_expanded": 0, "max_space": 2}

    while frontier_start and frontier_goal:
        counters["max_space"] = max(
            counters["max_space"],
            len(visited_start) + len(visited_goal)
        )

        if len(frontier_start) <= len(frontier_goal):
            meeting = _expand_one_level(problem, frontier_start, visited_start, visited_goal, counters)
            if meeting is not None:
                meeting_from_start, meeting_from_goal = meeting
                return _merge_paths(problem, meeting_from_start, meeting_from_goal), counters
        else:
            meeting = _expand_one_level(problem, frontier_goal, visited_goal, visited_start, counters)
            if meeting is not None:
                meeting_from_goal, meeting_from_start = meeting
                return _merge_paths(problem, meeting_from_start, meeting_from_goal), counters

    return None, counters


def _expand_one_level(
    problem: Problem,
    frontier: Deque[Node],
    own_visited: Dict[Any, Node],
    other_visited: Dict[Any, Node],
    counters: dict
) -> Optional[Tuple[Node, Node]]:
    level_size = len(frontier)

    for _ in range(level_size):
        current = frontier.popleft()
        counters["nodes_expanded"] += 1

        for child in current.expand(problem):
            if child.state in own_visited:
                continue

            own_visited[child.state] = child

            if child.state in other_visited:
                return child, other_visited[child.state]

            frontier.append(child)

    return None


def _merge_paths(problem: Problem, meeting_from_start: Node, meeting_from_goal: Node) -> Node:
    forward_path = meeting_from_start.path()
    backward_path = meeting_from_goal.path()
    backward_path.reverse()
    current = forward_path[-1]

    for node in backward_path[1:]:
        current = Node(
            state=node.state,
            parent=current,
            action=node.action,
            path_cost=current.path_cost + 1
        )

    return current