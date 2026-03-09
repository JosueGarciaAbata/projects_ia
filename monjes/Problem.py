class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state) -> list:
        raise NotImplementedError("Subclasses must implement this method")

    def result(self, state, action) -> object:
        raise NotImplementedError("Subclasses must implement this method")

    def goal_test(self, state) -> bool:
        return state == self.goal_state

    def is_safe(self, state) -> bool:
        raise NotImplementedError("Subclasses must implement this method")

    def path_cost(self, cost_so_far, state1, action, state2) -> float:
        return cost_so_far + 1