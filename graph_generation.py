"""
This module generates random new instances of a graph and stores them as a csv file
"""

import csv
import random
from maze import Maze
import networkx as nx

class Generator():
    def __init__(self, number_of_graphs = 10, size = 13):
        self.number_of_graphs = number_of_graphs
        self.size = size
        self.mazes = self.generate_mazes()
        self.print_mazes()
        self.create_csv('mazes.csv')
    
    def generate_mazes(self):
        mazes = []
        for i in range(self.number_of_graphs):
            feasible = False
            while(not feasible):
                maze = self.generate_maze()
                feasible = nx.is_connected(maze.grid)
            mazes.append(maze.obstacles)
        return mazes
    
    def generate_maze(self) -> None:
        num_obstacles = random.randint(1,int((self.size**2)*0.7))
        obstacles = []
        for i in range(num_obstacles):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            while((x,y) in obstacles):
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
            if (x == 0 and y == 0) or (x == 0 and y == self.size - 1):
                continue
            obstacles.append((x,y))
        maze = Maze(self.size, obstacles)
        return maze
    
    def print_mazes(self):
        print(self.mazes)

    def create_csv(self, filename):
        with open(filename, 'w') as f:
            write = csv.writer(f)
            for maze in self.mazes:
                write.writerow([f'{x[0]} {x[1]}' for x in maze])

        

if __name__ == "__main__":
    size = int(input("What is the size of the mazes you want to generate? "))
    main = Generator(size = size)