from maze import Maze
from tester import Tester
from original_solver import OriginalSolver
from dfs_solver import DFSSolver
from graph_generation import Generator


maze = Maze(size = 13, obstacles = [(3, 6),(1, 10),(7, 9),(3, 0),(4, 2),(2, 8),(6, 5),(3, 2),(6, 12),(5, 5),(1, 1),(0, 1)])
original_solver = OriginalSolver(maze = maze)
dfs_solver = DFSSolver(maze = maze)
tester = Tester()

tester.run_test(dfs_solver)

print(tester.get_trace())

