import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple
class Maze():
    """Class that initiates a 13 by 13 graph/grid."""
    def __init__(self, obstacles:List[Tuple[int, int]] = [], size = 13):
        self.size = size
        # graph creation - taking width and height as parameters
        self.grid = nx.grid_2d_graph(size,size)
        self.obstacles = obstacles
        self.remove_nodes()
        # Creates a node value of visits for all nodes, and sets this to 0 as a start
        nx.set_node_attributes(self.grid, 0, "visits")
        #print(list(G.nodes))
        # List of nodes to be removed from graph
        
        self.positions = self.set_positions()
        self.visited = self.set_visited()

    def set_size(self, size):
        self.grid = nx.grid_2d_graph(size,size)
        self.positions = self.set_positions()

    def get_graph(self) -> nx.graph:
        return self.grid

    def print_nodes(self):
        print(list(self.grid.nodes))
    
    def print_node_visits(self, node):
        print("Test")
        print(self.grid.nodes[node]["visits"])

    def set_obstacles(self, tuples):
        # the list of nodes that should be deleted 
        # passed as list of tuples where each tuple represents a node by x, y coordinates. Eg. [(0,0),(1,1)]
        self.obstacles = tuples

    def print_obstacles(self):
        print(self.obstacles)

    def remove_nodes(self):
        for obstacle in self.obstacles:
            print(obstacle)
            self.grid.remove_node(obstacle)

    def set_positions(self):
        positions = {}
        for i in range(self.size):
            for j in range(self.size):
                if (i,j) in self.grid.nodes:
                    positions[(i,j)] = (5*i,5*(self.size-j))
        return positions

    def set_visited(self) -> {}:
        visited = {}
        for n in self.grid:
            visited[n] = 0
        return visited
    
    def update_visit(self, n):
        self.visited[n] += 1
    
    def get_visited(self) -> {}:
        return self.visited
    
    def check_visited(self, node) -> 0:
        if node in list(self.visited.keys()):
            return self.visited[node]
