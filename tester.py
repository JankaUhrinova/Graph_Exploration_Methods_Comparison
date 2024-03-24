from base_solver import BaseSolver
from maze import Position
from typing import List

class Tester():

    def __init__(self) -> None:
        self.turns = 0
        self.trace = []

    def run_test(self, solver: BaseSolver) -> None:
            self.turns = 0
            self.trace = solver.solve()
            self.turns = len(self.trace)


    def get_turns(self) -> int:
        return self.turns
    
    def get_trace(self) -> List[Position]:
        return self.trace

    
        