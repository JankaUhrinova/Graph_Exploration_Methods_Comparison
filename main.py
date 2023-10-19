"""
This module functions as the main call. Generates GUI to wrap around graph generation. Shows the generated graph in tkinter.
"""
import tkinter as tk
from maze import Maze

class Main():
    """
    A main class responsible for creating a GUI window that wraps around our maze, so that it can be shown in tkinter.
    """
    def __init__ (self, window_size_x = "500", window_size_y = "500"):
        """
        Constructor for main.
        """
        # Set up some variables
        self.window_size_x = window_size_x
        self.window_size_y = window_size_y
        self.maze = Maze()
        # Set up root
        self.root = tk.Tk()
        self.root.geometry (f"{self.window_size_x}x{self.window_size_y}")
        self.root.title("Mousemaze")

        # Creating frames
        self.frame_input = tk.Frame(self.root, width = window_size_x)
        self.frame_input.pack()
        self.frame_maze = tk.Frame(self.root, width = window_size_x)
        self.frame_maze.pack()
        # Input frame element creation
        self.label_entry = tk.Label(self.frame_input, text="Input a list of tuples in the format x1 y2,x2 y2,... to set nodes to be removed from maze.")
        self.label_entry.pack()
        self.entry_tuple_list = tk.Entry(self.frame_input)
        self.entry_tuple_list.pack(side = tk.LEFT)
        self.button_submit = tk.Button(self.frame_input, text = "submit tuples", command=self.submit_tuples)
        self.button_submit.pack(side = tk.LEFT)
        self.label_warning = tk.Label(self.frame_input, text = "test")
        # Run the root
        self.root.mainloop()

    def submit_tuples(self) -> bool:
        """Takes single string input from entry, calls helper func, sets obstacles for maze if success and removes those nodes, else just warns user. Returns success/fail bool."""
        tuples_string = self.entry_tuple_list.get()
        success, tuple_list = self.cs_tuples(tuples_string)
        if(success):
            self.label_warning["text"] = "Submitting tuples was succesful!"
            self.maze.set_obstacles(tuple_list)
            self.maze.remove_nodes()
        else:
            self.label_warning["text"] = "Failure to submit tuples. Check format and try again."
        self.label_warning.pack(side = tk.BOTTOM)
        return success
    
    def cs_tuples(self,cs_tuple_string) -> (bool,[()]):
        """Helper function, takes a string in the comma separated format with tuples x1 y1,x2 y2... and returns a tuple list."""
        if(cs_tuple_string == ""):
            return (False, [()])
        tuple_list =[]
        tuples_string_list = cs_tuple_string.split(',')
        print(f"TUPLES STRING LIST :: {tuples_string_list}")
        for t in tuples_string_list:
            x, y = t.split(' ')
            new_t = (int(x), int(y))
            tuple_list.append(new_t)
        return (True,tuple_list)


if __name__ == "__main__":
    main = Main()