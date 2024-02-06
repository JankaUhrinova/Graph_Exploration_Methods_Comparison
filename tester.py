class Tester():
    def __init__(self, maze, algorithm) -> None:
        self.maze = maze
        self.algorithm = algorithm
        self.position = (0, 0)
        self.turns = 0

    def get_results(self) -> 0:
        self.run_test()
        return self.turns
    
    def update_position(self) -> False:
        self.position = self.algorithm.next_step(self.maze, self.position)
        self.turns += 1
        if self.position == (12, 0):
            return True
        
    def run_test(self) -> None:
        done = False
        while not done:
            done = self.update_position()
        