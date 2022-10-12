from tkinter import Button
import random
import settings
class Cell:
    all = []
    
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn = None
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

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

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

    def show_cell(self):
        
        self.cell_btn.configure(text=self.surrounded_cells_mines_length)

    def show_mine(self): # bomb exploded, game lost. 
        self.cell_btn.configure(bg="red")

    def right_click_action(self, event):
        print(event)
        print("right clicked")

    @staticmethod
    def randomize_mines():
        mines_list = random.sample(Cell.all, settings.MINES_COUNT)
        for i in mines_list:
            i.is_mine = True

    def __repr__(self):
        return f"Cell(x:{self.x}, y:{self.y}, is_mine:{self.is_mine})"