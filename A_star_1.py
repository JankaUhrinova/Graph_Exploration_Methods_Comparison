from maze import Maze, Position
from base_solver import BaseSolver
from queue import PriorityQueue
from collections import deque
from typing import Tuple, ClassVar



class A_solver_1(BaseSolver):
    
    heap: ClassVar[Tuple[int, Position]] = PriorityQueue() #holds unvisited nodes that are neighboring visited nodes and keeps them sorted by closeness to the finish node

    def next_step(self):
        x_pos = self.position.x
        y_pos = self.position.y

        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        for i in range(len(directions)):
            node = Position(x_pos + directions[i][0], y_pos + directions[i][1])
            if self.maze.grid.has_node(node.to_tuple()): 
                num_visited = self.maze.check_visited(node)
                if(num_visited == 0):
                    return node

        #Find the unvisited node that is closest to the finishing node and go there
        
        goal = self.heap.get()[1]
        #Since it's possible that node has been visited in the meantime, check it after poping from the heap
        while(self.maze.check_visited(goal) != 0):
            goal = self.heap.get()[1]

        self.trace.append(self.transport(goal))
        return goal

    
    def transport(self, goal: Position):

        # Visited set to keep track of visited nodes
        visited = set()
        visited.add(self.position.to_tuple())
        
        # Queue for BFS
        queue = deque([(self.position, [])])  # (node, path to this node from the og position)
        
        # Perform BFS
        while queue:
            cell, path = queue.popleft()
            if cell == goal:
                path = path[:-1]
                return path
            
            x_pos = cell.x
            y_pos = cell.y

            directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

            for i in range(len(directions)):
                node = Position(x_pos + directions[i][0], y_pos + directions[i][1])
                if self.maze.grid.has_node(node.to_tuple()): 
                    num_visited = self.maze.check_visited(node)
                    if(num_visited != 0 and node.to_tuple() not in visited):
                        new_path = path + [node]
                        queue.append(node, new_path)
                        visited.add(node.to_tuple())

    
    def put_neighbors_in_heap(self, cell: Position):
        x_pos = cell.x
        y_pos = cell.y

        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        for i in range(len(directions)):
            node = Position(x_pos + directions[i][0], y_pos + directions[i][1])
            if self.maze.grid.has_node(node.to_tuple()): 
                num_visited = self.maze.check_visited(node)
                distance_from_finish = abs(self.maze.end_position.x - node.x) + abs(self.maze.end_position.y - node.y) 
                if(num_visited == 0):
                    self.heap.put(distance_from_finish, cell)

    
    def solve(self):
        while self.position != self.maze.end_position:
            self.maze.update_visit(self.position)
            self.put_neighbors_in_heap(self.position)
            self.position = self.next_step()
            self.trace.append(self.position)
        return self.trace