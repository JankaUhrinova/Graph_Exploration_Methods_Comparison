import networkx as nx
import matplotlib.pyplot as plt

class Maze():
    """Class that initiates a 13 by 13 graph/grid."""
    def __init__(self, obstacles = [()]):
        # graph creation - taking width and height as parameters
        self.grid = nx.grid_2d_graph(13,13)
        self.obstacles = obstacles
        self.remove_nodes()
        # Creates a node value of visits for all nodes, and sets this to 0 as a start
        nx.set_node_attributes(self.grid, 0, "visits")
        #print(list(G.nodes))
        # List of nodes to be removed from graph
        
        self.positions = self.set_positions()
        self.visited = self.set_visited()


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
            self.grid.remove_node(obstacle)

    def set_positions(self):
        positions = {}
        for i in range(13):
            for j in range(13):
                if (i,j) in self.grid.nodes:
                    positions[(i,j)] = (5*i,5*(13-j))
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
