from maze import Maze, Position
from base_solver import BaseSolver
from queue import PriorityQueue
from collections import deque
from typing import Tuple, ClassVar, List


class A_solver_2(BaseSolver):
    
    to_explore: List[Position] = [] 

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

        #Find the unvisited node that has smallest combined distance from the finish and the current position
        heap = PriorityQueue()
        
        for node in self.to_explore:
            if self.maze.check_visited(node) != 0:
                continue
            weigth = 0
            path_from_current = self.transport(node)
            weigth += len(path_from_current)
            weigth += abs(self.maze.end_position.x - node.x) + abs(self.maze.end_position.y - node.y) 
            heap.put((weigth, node))

        
        goal = heap.get()[1]
        self.trace += self.transport(goal)
        return goal

    def check_distances(self):
        # Visited set to keep track of visited nodes
        visited = set()
        visited.add(self.position.to_tuple())
        
        # Queue for BFS
        queue = deque([(self.position, 0)])  # (node, num of steps to get there)
        
        distances = {}

        # Perform BFS
        while queue:
            cell, distance = queue.popleft()
            x_pos = cell.x
            y_pos = cell.y
            directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

            distances[cell] = distance

            for i in range(len(directions)):
                node = Position(x_pos + directions[i][0], y_pos + directions[i][1])
                if self.maze.grid.has_node(node.to_tuple()): 
                    num_visited = self.maze.check_visited(node)
                    if num_visited != 0 and node.to_tuple() not in visited:
                        new_distance = distance + 1
                        queue.append(node, new_distance)
                        visited.add(node.to_tuple())
                    elif num_visited == 0:
                        distances[node] = distance + 1

        return distances


    def transport(self, goal: Position):

        # Visited set to keep track of visited nodes
        visited = set()
        visited.add(self.position.to_tuple())
        
        # Queue for BFS
        queue = deque([(self.position, [])])  # (node, path to this node from the og position)
        
        # Perform BFS
        while queue:
            cell, path = queue.popleft()
            x_pos = cell.x
            y_pos = cell.y
            #go through all neighbors of the cell to see if there is goal node
            directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
            for i in range(len(directions)):
                node = Position(x_pos + directions[i][0], y_pos + directions[i][1])
                if node == goal:
                    return path

            for i in range(len(directions)):
                node = Position(x_pos + directions[i][0], y_pos + directions[i][1])
                if self.maze.grid.has_node(node.to_tuple()): 
                    num_visited = self.maze.check_visited(node)
                    if(num_visited != 0 and node.to_tuple() not in visited):
                        new_path = path + [node]
                        queue.append((node, new_path))
                        visited.add(node.to_tuple())

    def put_neighbors_in_list(self):
        x_pos = self.position.x
        y_pos = self.position.y

        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        for i in range(len(directions)):
            node = Position(x_pos + directions[i][0], y_pos + directions[i][1])
            if self.maze.grid.has_node(node.to_tuple()): 
                num_visited = self.maze.check_visited(node)
                if(num_visited == 0 and node not in self.to_explore):
                    self.to_explore.append(node)

    def solve(self):
        while self.position != self.maze.end_position:
            print(self.position.x, self.position.y)
            self.maze.update_visit(self.position)
            self.put_neighbors_in_list()
            self.position = self.next_step()
            self.trace.append(self.position)
        return self.trace
