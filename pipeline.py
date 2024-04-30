from tester import Tester
from original_solver import OriginalSolver
from dfs_solver import DFSSolver
from A_star_1 import A_solver_1
from A_star_2 import A_solver_2
from graph_generation import Generator
import matplotlib.pyplot as plt
from graph_generation import Generator
import random
from copy import deepcopy

random.seed(47)

generator = Generator(number_of_graphs = 10, size = 30)
mazes = generator.get_maze_objects()
solvers_performance = {"Original": [],
                       "DFS": [],
                       "A_1": [],
                       "A_2": []}
solvers_traces = {"Original": [],
                       "DFS": [],
                       "A_1": [],
                       "A_2": []}

tester = Tester()

for i, maze in enumerate(mazes):
    original_solver = OriginalSolver(maze = deepcopy(maze))
    tester.run_test(original_solver)
    solvers_performance["Original"].append(tester.get_turns())
    solvers_traces["Original"].append(tester.get_trace())

    dfs_solver = DFSSolver(maze = deepcopy(maze))
    tester.run_test(dfs_solver)
    solvers_performance["DFS"].append(tester.get_turns())
    solvers_traces["DFS"].append(tester.get_trace())

    a_1_solver = A_solver_1(maze = deepcopy(maze))
    a_1_solver.solve()
    tester.run_test(a_1_solver)
    solvers_performance["A_1"].append(tester.get_turns())
    solvers_traces["A_1"].append(tester.get_trace())

    a_2_solver = A_solver_2(maze = deepcopy(maze))
    tester.run_test(a_2_solver)
    solvers_performance["A_2"].append(tester.get_turns())
    solvers_traces["A_2"].append(tester.get_trace())

    print(i, "/", len(mazes))


print(solvers_performance)
print()
print(solvers_traces["DFS"][2])
