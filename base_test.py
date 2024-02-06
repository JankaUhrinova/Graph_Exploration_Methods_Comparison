from operator import itemgetter

from maze import Maze

class BaseAlgorithm():
    def __init_(self):
        self.queue = []

    def next_step(self, maze: Maze, position):
        x_pos, y_pos = position
        neighbors = []

        # to choose which node should be visited first, the base algorithm chooses the least visited neighbor
        # the ties are broken in following order: down, left, right, up
        # the neighbors are represented by a list in a following format:
        # [number of times the neighbor was visited, index representing direction (for breaking ties), coordinates of a neighbor]
        # always check, if the neighbor exists first

        node = (x_pos + 1, y_pos) #going down
        if maze.grid.has_node(node): 
            num_visited = maze.check_visited(node)
            neighbors.append([num_visited, 0, node])

        node = (x_pos, y_pos - 1) #going left
        if maze.grid.has_node(node): 
            num_visited = maze.check_visited(node)
            neighbors.append([num_visited, 1, node])
        
        node = (x_pos, y_pos + 1) #going right
        if maze.grid.has_node(node): 
            num_visited = maze.check_visited(node)
            neighbors.append([num_visited, 2, node])

        node = (x_pos - 1, y_pos) #going up
        if maze.grid.has_node(node): 
            num_visited = maze.check_visited(node)
            neighbors.append([num_visited, 3, node])

        priority = sorted(neighbors, key = itemgetter(0, 1))
        print(x_pos, y_pos)
        print(priority)
        return priority[0][2] #return next position




        