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


maze = Maze(size = 10, obstacles = [(5,0), (7, 0),(8, 0),(0, 1),(1, 1),(2, 1),(3, 1),(5, 1),(7, 1),(8, 1),(1, 2),(3, 2), (5, 2),
                                 (7, 2), (8, 2),(3, 3),(5, 3),(7, 3),(8, 3),(1, 4),(3, 4),(5, 4),(7, 4),(8, 4),
                                 (1, 5),(3, 5), (5, 5), (7, 5), (8, 5),(1, 6),(3, 6),(5, 6),(6,6), (7, 6),(8, 6), (1,7), (8, 7),
                                 (0, 8), (1, 8),(2, 8),(3, 8),(4, 8),(5, 8), (6, 8), (8, 8), (8,9)])
# nx.draw(maze.grid)

# nx.draw(maze.grid, pos=maze.set_positions())
# plt.show()
# original_solver = OriginalSolver(maze = maze)
dfs_solver = DFSSolver(maze = maze)
A_1_solver = A_solver_1(maze = maze)
A_2_solver = A_solver_2(maze = maze)
tester = Tester()

# main = Main(maze_size= 9)
# main.maze = maze

# main.draw_graph()


tester.run_test(A_2_solver)


print(tester.get_trace())
print(tester.get_turns())

