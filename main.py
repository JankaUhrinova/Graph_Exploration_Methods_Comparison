"""
This module functions as the main call. Generates GUI to wrap around graph generation. Shows the generated graph in tkinter.
"""
import sys
import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from maze import Maze

class Main():
    """
    A main class responsible for creating a GUI window that wraps around our maze, so that it can be shown in tkinter.
    """
    def __init__ (self, window_size_x = "650", window_size_y = "650"):
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
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        # Creating frames
        self.frame_input = tk.Frame(self.root, width = window_size_x)
        self.frame_input.pack()
        self.frame_maze = tk.Frame(self.root, width = window_size_x)
        self.frame_maze.pack()
        # Input frame element creation
        self.label_entry = tk.Label(self.frame_input, text="Input a list of tuples in the format x1 y2,x2 y2,... to set nodes to be removed from maze.")
        self.label_entry.pack(side = tk.TOP)
        self.entry_tuple_list = tk.Entry(self.frame_input)
        self.entry_tuple_list.pack(side = tk.LEFT)
        self.button_submit = tk.Button(self.frame_input, text = "Submit tuples.", command=self.submit_tuples)
        self.button_submit.pack(side = tk.LEFT)
        self.label_warning = tk.Label(self.frame_input, text = "")
        # Maze frame element creation
        self.label_maze = tk.Label(self.frame_maze, text="Mousemaze graph.")
        self.label_maze.pack()
        self.button_draw = tk.Button(self.frame_maze, text="Draw the graph.", command=self.draw_graph)
        self.button_draw.pack()
        self.maze_canvas = None
        self.button_new_graph = tk.Button(self.frame_maze, text="New graph", command=self.new_graph)
        self.button_new_graph.pack(side=tk.BOTTOM)
        # Run the root
        self.root.mainloop()

    def submit_tuples(self) -> None:
        """On button click: Takes single string input from entry, calls helper func, sets obstacles for maze if success and removes those nodes, else just warns user."""
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
        if(cs_tuple_string.endswith(",")):
            cs_tuple_string = cs_tuple_string[:-1]
        tuple_list =[]
        tuples_string_list = cs_tuple_string.split(',')
        print(f"TUPLES STRING LIST :: {tuples_string_list}")
        for t in tuples_string_list:
            x, y = t.split(' ')
            new_t = (int(x), int(y))
            tuple_list.append(new_t)
        return (True,tuple_list)
    
    def draw_graph(self):
        """On button click: draws the mousemaze graph onto the tkinter frame."""
        if(self.maze_canvas is not None):
            self.maze_canvas.get_tk_widget().pack_forget()
        figure = plt.figure(figsize=(5,5))
        a = figure.add_subplot(111)
        plt.axis('off')
        nx.draw(self.maze.get_graph(), self.maze.positions, ax=a)
        self.maze_canvas = FigureCanvasTkAgg(figure, master = self.frame_maze)
        self.maze_canvas.draw()
        self.maze_canvas.get_tk_widget().pack()
    
    def new_graph(self):
        self.maze = Maze()
        self.draw_graph()

    def close(self):
        self.root.destroy()
        sys.exit()


if __name__ == "__main__":
    main = Main()