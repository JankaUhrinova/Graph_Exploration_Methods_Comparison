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
from tkinter import filedialog
from tkinter import messagebox

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
        self.maze_dict = {}
        self.curr_graph = 0
        # Set up root
        self.root = tk.Tk()
        self.root.geometry (f"{self.window_size_x}x{self.window_size_y}")
        self.root.title("Mousemaze")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.radio_value = tk.IntVar()

        """Creating frames"""
        self.frame_radio = tk.Frame(self.root, width= window_size_x)
        self.frame_radio.grid(row = 0)
        self.frame_input_manual = tk.Frame(self.root, width = window_size_x)
        self.frame_input_csv = tk.Frame(self.root, width=window_size_x)
        self.frame_maze = tk.Frame(self.root, width = window_size_x)
        self.frame_maze.grid(row=2)
        # Radio frame element creation
        self.label_radio = tk.Label(self.frame_radio, text="Please pick an input method:")
        self.label_radio.pack(side=tk.TOP)
        self.radio_input1 = tk.Radiobutton(self.frame_radio, anchor=tk.CENTER, text="Manual obsacle input.", variable=self.radio_value, value=1, command=self.switch_input_frame)
        self.radio_input1.pack(side=tk.LEFT)
        self.radio_input2 = tk.Radiobutton(self.frame_radio, anchor=tk.CENTER, text="Input(possibly multiple) from CSV.", variable=self.radio_value, value=2, command=self.switch_input_frame)
        self.radio_input2.pack(side=tk.LEFT)
        # Manual input frame element creation
        self.label_entry = tk.Label(self.frame_input_manual, text="Input a list of tuples in the format x1 y2,x2 y2,... to set nodes to be removed from maze.")
        self.label_entry.pack(side = tk.TOP)
        self.entry_tuple_list = tk.Entry(self.frame_input_manual)
        self.entry_tuple_list.pack(side = tk.LEFT)
        self.button_submit = tk.Button(self.frame_input_manual, text = "Submit tuples.", command=self.submit_tuples)
        self.button_submit.pack(side = tk.LEFT)
        self.label_warning = tk.Label(self.frame_input_manual, text = "")
        # CSV input frame element creation
        self.button_inputcsv = tk.Button(self.frame_input_csv, text = "Input graph from CSV.", command=self.open_csv_input)
        self.button_inputcsv.pack(side = tk.LEFT)
        self.button_next = tk.Button(self.frame_input_csv, text="<-", command=None)
        self.button_next = tk.Button(self.frame_input_csv, text="->", command=None)
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
        if(not self.maze):
           self.maze = Maze()
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
    
    def open_csv_input(self) -> None:
        """Opens a windows filename dialog, and tries to get csv input. Credit for lines 3-9 to 2022/23 SH-16 COMPSCI4015 group, as per CCA4.0 License. Code used was originally written by me."""
        while True:
            filename = filedialog.askopenfilename() # Ask for csv to take slice from
            if not(filename.endswith(".csv")) or filename is None:
                messagebox.showerror("Wrong File Type!", "Wrong File Type! \
                                        Please choose a csv file.")
            else:
                break
        with open(filename, encoding='utf-8-sig') as f:
            lines = f.readlines()
            offset = len(self.maze_dict)
            print(lines)
            for i in range(len(lines)):
                line = lines[i].strip().split(',')
                new_line = list(map(lambda a : tuple(map(lambda b : int(b), a.split(" "))), line))
                self.maze_dict[i+offset] = new_line
        # Draw the initial graph at key 0
        self.maze.set_obstacles(self.maze_dict[0])
        self.maze.remove_nodes()
        self.draw_graph()


    def cs_tuples(self,cs_tuple_string) -> (bool,[()]):
        """Helper function, takes a string in the comma separated format with tuples x1 y1,x2 y2... and returns a tuple list."""
        if(cs_tuple_string == ""):
            return (False, [()])
        if(cs_tuple_string.endswith(",")):
            cs_tuple_string = cs_tuple_string[:-1]
        tuple_list =[]
        tuples_string_list = cs_tuple_string.split(',')
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
    
    def switch_input_frame(self):
        if(self.radio_value.get() == 1):
            self.frame_input_csv.grid_forget()
            self.frame_input_manual.grid(row=1)
        else:
            self.frame_input_manual.grid_forget()
            self.frame_input_csv.grid(row=1)
    
    def next_graph(self):
        return None

    def new_graph(self):
        self.maze = Maze()
        self.draw_graph()

    def close(self):
        self.root.destroy()
        sys.exit()


if __name__ == "__main__":
    main = Main()