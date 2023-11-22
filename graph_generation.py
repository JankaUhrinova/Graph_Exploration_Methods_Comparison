"""
This module generates random new instances of a graph and stores them as a csv file
"""

import csv
import random
from maze import Maze
import networkx as nx

class Main():
    def __init__(self, number_of_graphs = 10, dimensions = (13,13)):
        self.number_of_graphs = number_of_graphs
        self.dimensions = dimensions
        self.mazes = self.generate_mazes()
        self.print_mazes()
    
    def generate_mazes(self) -> []:
        mazes = []
        for i in range(self.number_of_graphs):
            feasible = False
            while(not feasible):
                maze = self.generate_maze()
                feasible = self.is_possible(maze)
            mazes.append(maze.obstacles)
        return mazes
    
    def generate_maze(self) -> None:
        num_obstacles = random.randint(1, 30)
        obstacles = []
        for i in range(num_obstacles):
            x = random.randint(0, self.dimensions[0] - 1)
            y = random.randint(0, self.dimensions[1] - 1)
            while((x,y) in obstacles):
                x = random.randint(0, self.dimensions[0] - 1)
                y = random.randint(0, self.dimensions[1] - 1)
            if (x == 0 and y == 0) or (x == self.dimensions[0] - 1 and y == self.dimensions[1] - 1):
                pass
            obstacles.append((x,y))
        maze = Maze(obstacles)
        maze.remove_nodes()
        return maze
    
    def is_possible(self, maze) -> False:
        if len(list(nx.dfs_preorder_nodes(maze.grid))) == self.dimensions[0] * self.dimensions[1] - len(maze.obstacles):
            return True
        return False
    
    def print_mazes(self):
        print(self.mazes)

"""    def create_csv(self, filename):
        with open(filename, 'w') as f:
            write = csv.writer(f)
            write"""

        

if __name__ == "__main__":
    main = Main()