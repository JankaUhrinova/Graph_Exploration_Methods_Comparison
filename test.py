from maze import Maze
from tester import Tester
from original_solver import OriginalSolver
from dfs_solver import DFSSolver
from A_star_1 import A_solver_1
from A_star_2 import A_solver_2
from graph_generation import Generator
from main import Main
import networkx as nx
import matplotlib.pyplot as plt


maze = Maze(size = 10, obstacles = [(7, 6), (1, 1), (9, 0), (5, 5), (9, 2), (0, 4), (5, 2), (6, 7), (4, 4), (5, 6), (1, 3), (2, 9), (3, 4), (3, 7), (8, 5), (2, 8), (5, 1), (2, 2), (9, 3)])
# nx.draw(maze.grid)

# nx.draw(maze.grid, pos=maze.set_positions())
# plt.show()
original_solver = OriginalSolver(maze = maze)
dfs_solver = DFSSolver(maze = maze)
A_1_solver = A_solver_1(maze = maze)
A_2_solver = A_solver_2(maze = maze)
tester = Tester()

# main = Main(maze_size= 9)
# main.maze = maze

# main.draw_graph()


tester.run_test(A_1_solver)


print(tester.get_trace())
print(tester.get_turns())

