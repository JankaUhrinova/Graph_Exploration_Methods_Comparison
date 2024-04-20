import tkinter as tk

X, Y = 0, 1
SIZE = (600, 600) # Width, Height

class GridGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Grid GUI")

        self.grid_size = (10, 10)  # Default grid size
        self.grid = [[0 for _ in range(self.grid_size[X])] for _ in range(self.grid_size[Y])]
        self.walls = []

        self.canvas = tk.Canvas(self.root, width=SIZE[X], height=SIZE[Y], bg="white")
        self.canvas.pack()

        self.textbox = tk.Text(self.root, height=10, width=100)
        self.textbox.pack()

        self.btn_clear = tk.Button(self.root, text="Clear Walls", command=self.clear_walls)
        self.btn_clear.pack()

        self.btn_fill = tk.Button(self.root, text="Fill Walls", command=self.fill_walls)
        self.btn_fill.pack()

        self.entry_cols = tk.Entry(self.root, width=5)
        self.entry_cols.pack()
        self.entry_cols.insert(0, str(self.grid_size[X]))

        self.entry_rows = tk.Entry(self.root, width=5)
        self.entry_rows.pack()
        self.entry_rows.insert(0, str(self.grid_size[Y]))

        self.btn_update = tk.Button(self.root, text="Init Grid", command=self.init_grid)
        self.btn_update.pack()

        self.marks = {}

        self.draw_grid()

        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.canvas.bind("<Button-3>", self.toggle_mark)
    
    def init_grid(self):
        rows = int(self.entry_rows.get())
        cols = int(self.entry_cols.get())

        self.grid_size = (rows, cols)
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        wall_text = self.textbox.get(1.0, tk.END)
        walls = []
        if wall_text:
            walls = eval(wall_text)
            for x, y in walls:
                self.grid[y][x] = 1

        self.update_output()

    def draw_grid(self):
        cell_width = SIZE[X] / self.grid_size[X]
        cell_height = SIZE[Y] / self.grid_size[Y]

        for y in range(self.grid_size[Y]):
            for x in range(self.grid_size[X]):
                x0 = x * cell_width
                y0 = y * cell_height
                x1 = x0 + cell_width
                y1 = y0 + cell_height

                color = "white" if self.grid[y][x] == 0 else "gray"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                self.canvas.create_text(x0 + 10, y0 + 10, text=f"{x}, {y}")
        
        marg_w, marg_h = cell_width * 0.2, cell_height * 0.2
        for mark, color in self.marks.items():
            x0 = mark[X] * cell_width
            y0 = mark[Y] * cell_height
            x1 = x0 + cell_width
            y1 = y0 + cell_height

            self.canvas.create_oval(x0 + marg_w, y0 + marg_h, x1 - marg_w, y1 - marg_h, fill=color)

    def toggle_cell(self, event):
        cell_width = SIZE[X] / self.grid_size[X]
        cell_height = SIZE[Y] / self.grid_size[Y]

        col = int(event.x / cell_width)
        row = int(event.y / cell_height)

        if self.grid[row][col] == 0:
            self.grid[row][col] = 1
            self.canvas.create_rectangle(col * cell_width, row * cell_height,
                                         (col + 1) * cell_width, (row + 1) * cell_height, fill="black")
        else:
            self.grid[row][col] = 0
            self.canvas.create_rectangle(col * cell_width, row * cell_height,
                                         (col + 1) * cell_width, (row + 1) * cell_height, fill="white")
        self.update_output()
    
    def toggle_mark(self, event):
        cell_width = SIZE[X] / self.grid_size[X]
        cell_height = SIZE[Y] / self.grid_size[Y]

        col = int(event.x / cell_width)
        row = int(event.y / cell_height)

        colors = ["empty", "red", "blue", "green"]
        pos = (col, row)
        if pos not in self.marks:
            self.marks[pos] = colors[0]
        color = self.marks[pos]
        idx = colors.index(color)
        idx = (idx + 1) % len(colors)
        self.marks[pos] = colors[idx]
        if self.marks[pos] == "empty":
            del self.marks[pos]
        self.update_output()

    def set_wall(self):
        self.walls = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[Y])):
                if self.grid[y][x] == 1:
                    self.walls.append((x, y))
        self.walls.sort()

    def clear_walls(self):
        self.walls = []
        self.grid = [[0 for _ in range(self.grid_size[X])] for _ in range(self.grid_size[Y])]
        self.update_output()
    
    def fill_walls(self):
        self.walls = []
        self.grid = [[1 for _ in range(self.grid_size[X])] for _ in range(self.grid_size[Y])]
        self.update_output()

    def print_walls(self):
        self.textbox.delete(1.0, tk.END)
        text = "[{}]".format(", ".join(map(str, self.walls)))
        self.textbox.insert(tk.END, text)
    
    def update_output(self):
        self.set_wall()
        self.canvas.delete("all")
        self.draw_grid()
        self.print_walls()

if __name__ == "__main__":
    root = tk.Tk()
    app = GridGUI(root)
    root.mainloop()