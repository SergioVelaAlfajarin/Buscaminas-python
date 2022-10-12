import sys
from tkinter import Button, Label
import random
import settings
import ctypes

class Cell:
    all = []
    
    cell_count = settings.CELL_COUNT
    
    cell_count_label = None
    
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x -1, self.y -1),
            self.get_cell_by_axis(self.x -1, self.y),
            self.get_cell_by_axis(self.x -1, self.y +1),
            self.get_cell_by_axis(self.x, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y),
            self.get_cell_by_axis(self.x +1, self.y +1),
            self.get_cell_by_axis(self.x, self.y +1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        
        return counter
    
    # methods ------------------------------------------------------
    
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn = None
        self.is_mine_candidate = False
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_button(self, location):
        btn = Button(
            location,
            width=10,
            height=3,
        )
        btn.bind('<Button-1>', self.left_click_action) # left click
        btn.bind('<Button-3>', self.right_click_action) # right click
        self.cell_btn = btn;

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, "Has Ganado", "Game Over", 0)
        self.cell_btn.unbind("<Button-1>")
        self.cell_btn.unbind("<Button-3>")

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_cell(self):
        if self.is_opened:
            return;
        
        Cell.cell_count -= 1
        self.cell_btn.configure(text=self.surrounded_cells_mines_length)
        self.cell_btn.configure(bg="SystemButtonFace")
        if Cell.cell_count_label:
            Cell.cell_count_label.configure(
                text=f"Cells Left: {Cell.cell_count}"
            )
        self.is_opened = True

    def show_mine(self): # bomb exploded, game lost. 
        self.cell_btn.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "Has hecho click en una bomba.", "Game Over", 0)
        sys.exit()

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn.configure(bg="SystemButtonFace")
            self.is_mine_candidate = False

    # static -------------------------------------------------------

    @staticmethod
    def randomize_mines():
        mines_list = random.sample(Cell.all, settings.MINES_COUNT)
        for i in mines_list:
            i.is_mine = True

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            font=("", 30),
            text=f"Cells Left: {Cell.cell_count}",
        )
        Cell.cell_count_label = lbl

    def __repr__(self):
        return f"Cell(x:{self.x}, y:{self.y}, is_mine:{self.is_mine})"