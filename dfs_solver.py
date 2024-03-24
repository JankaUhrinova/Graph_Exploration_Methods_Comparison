from maze import Maze, Position
from base_solver import BaseSolver
from typing import List, Any



class DFSSolver(BaseSolver):
    
    stack: List[Position] = []

    def next_step(self):
        x_pos = self.position.x
        y_pos = self.position.y
        # to choose which node should be visited first, the base algorithm chooses the least visited neighbor
        # the ties are broken in following order: down, left, right, up
        # the neighbors are represented by a list in a following format:
        # [number of times the neighbor was visited, index representing direction (for breaking ties), coordinates of a neighbor]
        # always check, if the neighbor exists first

        node = Position(x_pos, y_pos + 1) #going down
        if self.maze.grid.has_node(node.to_tuple()): 
            num_visited = self.maze.check_visited(node)
            if(num_visited == 0):
                return node

        node = Position(x_pos - 1, y_pos) #going left
        if self.maze.grid.has_node(node.to_tuple()): 
            num_visited = self.maze.check_visited(node)
            if(num_visited == 0):
                return node
        
        node = Position(x_pos + 1, y_pos) #going right
        if self.maze.grid.has_node(node.to_tuple()): 
            num_visited = self.maze.check_visited(node)
            if(num_visited == 0):
                return node

        node = Position(x_pos, y_pos - 1) #going up
        if self.maze.grid.has_node(node.to_tuple()): 
            num_visited = self.maze.check_visited(node)
            if(num_visited == 0):
                return node

        
        return self.stack.pop()
    
    def solve(self):
        while self.position != self.maze.end_position:
            self.stack.append(self.position)
            self.maze.update_visit(self.position)
            self.position = self.next_step()
            self.trace.append(self.position)
        return self.trace
