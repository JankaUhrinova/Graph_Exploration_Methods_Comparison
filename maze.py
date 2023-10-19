import networkx as nx
import matplotlib.pyplot as plt

class Maze():
    """Class that initiates a 13 by 13 graph/grid."""
    def __init__(self, obstacles = [()]):
        # graph creation - taking width and height as parameters
        self.grid = nx.grid_2d_graph(13,13)
        #print(list(G.nodes))
        # List of nodes to be removed from graph
        self.obstacles = obstacles
        self.positions = {}
        self.set_positions()

    def get_graph(self) -> nx.graph:
        return self.grid

    def print_nodes(self):
        print(list(self.grid.nodes))

    def set_obstacles(self, tuples):
        # the list of nodes that should be deleted 
        # passed as list of tuples where each tuple represents a node by x, y coordinates. Eg. [(0,0),(1,1)]
        self.obstacles = tuples

    def print_obstacles(self):
        print(self.obstacles)

    def remove_nodes(self):
        for obstacle in self.obstacles:
            self.grid.remove_node(obstacle)

    def set_positions(self):
        # graph visualisation
        for i in range(13):
            for j in range(13):
                if (i,j) in self.grid.nodes:
                    self.positions[(i,j)] = (5*i,5*(13-j))
        #return nx.draw(self.grid, positions)