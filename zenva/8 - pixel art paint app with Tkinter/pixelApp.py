from tkinter import *
import tkinter.colorchooser

class PixelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art Paint")

        # parameters
        self.current_color = "black"
        cell_length = 20
        grid_width = 32
        grid_height = 18
        self.is_pen_selected = False
        self.is_eraser_selected = False

        # structure setup
        self.canvas = Canvas(self.root, bg="white")
        self.canvas.grid(row=0, column=0, sticky=(N,S,E,W))

        # structure: canvas
        self.cells = []
        for i in range(grid_width):
            row = []
            for j in range(grid_height):
                cell = Frame(self.canvas, width=cell_length, height=cell_length, bg="white")
                cell.grid(column=i, row=j)
                cell.bind("<Button-1>", self.tap_cell)
                row.append(cell)
            self.cells.append(row)

        # structure: controls
        control_frame = Frame(self.root, height=cell_length)
        control_frame.grid(row=1, column=0, sticky=(N,S,E,W))

        button_new = Button(control_frame, text="New", command=self.new_canvas)
        button_new.grid(row=0, column=0, columnspan=2, sticky=(N, S, E, W), padx=5, pady=5)

        button_save = Button(control_frame, text="Save", command=self.save_canvas)
        button_save.grid(row=0, column=2, columnspan=2, sticky=(N, S, E, W), padx=5, pady=5)

        self.image_pen = PhotoImage(file="images/pencil.png").subsample(4,4)
        button_pen = Button(control_frame, image=self.image_pen, command=self.press_prencil_button)
        button_pen.grid(row=0, column=6, columnspan=2, sticky=(N, S, E, W), padx=5, pady=5)

        self.image_eraser = PhotoImage(file="images/eraser.png").subsample(4,4)
        button_eraser = Button(control_frame, image=self.image_eraser, command=self.press_eraser_button)
        button_eraser.grid(row=0, column=8, columnspan=2, sticky=(N, S, E, W), padx=5, pady=5)

        self.colour_chooser = tkinter.colorchooser.Chooser(self.root)
        self.selected_colour_box = Frame(control_frame, borderwidth=1, bg=self.current_color, relief="groove")
        self.selected_colour_box.grid(row=0, column=12, sticky=(N, S, E, W), padx=5, pady=5)

        button_pick_color = Button(control_frame, text="Pick Color", command=self.pick_color)
        button_pick_color.grid(row=0, column=14, columnspan=3, sticky=(N, S, E, W), padx=5, pady=5)

        # structure configuration
        cols, rows = control_frame.grid_size()
        for col in range(cols):
            control_frame.grid_columnconfigure(col, minsize=cell_length)
        for row in range(rows):
            control_frame.grid_rowconfigure(row, minsize=cell_length)

    def tap_cell(self, event):
        x = event.x
        y = event.y
        cell_x = x // 50
        cell_y = y // 50
        print("Tapped at", event.x, event.y, "-> cell", cell_x, cell_y)
        self.cells[cell_x][cell_y].config(bg=self.current_color)

    def paint(self, event):
        x = event.x
        y = event.y
        self.canvas.create_rectangle(x, y, x+10, y+10, fill=self.current_color)

    def define_color(self, color):
        self.current_color = color
        self.selected_colour_box["bg"] = self.current_color

    def new_canvas(self):
        print("New canvas...")

    def save_canvas(self):
        print("Saving canvas...")
        
    def press_prencil_button(self):
        self.is_pen_selected = True
        self.is_eraser_selected = False

    def press_eraser_button(self):
        self.is_pen_selected = False
        self.is_eraser_selected = True

    def pick_color(self):
        chosen_color = self.colour_chooser.show()[1]
        if chosen_color != None:
            self.define_color(chosen_color)