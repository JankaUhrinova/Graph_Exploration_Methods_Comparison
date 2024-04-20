from maze import Maze, Position
from base_solver import BaseSolver
from typing import List, Any



class DFSSolver(BaseSolver):
    
    stack: List[Position] = [(Position(0,0))]

    def next_step(self):
        x_pos = self.position.x
        y_pos = self.position.y
        # to choose which node should be visited first, the base algorithm chooses the least visited neighbor
        # the ties are broken in following order: down, left, right, up
        # the neighbors are represented by a list in a following format:
        # [number of times the neighbor was visited, index representing direction (for breaking ties), coordinates of a neighbor]
        # always check, if the neighbor exists first

        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        for i in range(len(directions)):
            node = Position(x_pos + directions[i][0], y_pos + directions[i][1])
            if self.maze.grid.has_node(node.to_tuple()): 
                num_visited = self.maze.check_visited(node)
                if(num_visited == 0):
                    return node
        
        return -1
    
    def solve(self):
        while self.position != self.maze.end_position:
            self.maze.update_visit(self.position)
            # print(self.position.x, self.position.y)
            new_position = self.next_step()
            if new_position == -1:
                self.stack.pop()
                self.position = self.stack[-1]
            else:
                self.stack.append(new_position)
                self.position = new_position
            
            self.trace.append(self.position)
        return self.trace
