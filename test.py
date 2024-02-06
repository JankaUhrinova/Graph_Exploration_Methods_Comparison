from maze import Maze
from tester import Tester
from base_test import BaseAlgorithm
from graph_generation import Generator

algorithm = BaseAlgorithm()
maze = Maze([(3, 6),(1, 10),(7, 9),(3, 0),(4, 2),(2, 8),(6, 5),(3, 2),(6, 12),(5, 5),(1, 1),(0, 1)])
tester = Tester(maze, algorithm)

print(tester.get_results())

