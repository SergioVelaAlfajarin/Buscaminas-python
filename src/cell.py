from tkinter import Button
import random

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
            text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>', self.left_click_action) # left click
        btn.bind('<Button-3>', self.right_click_action) # right click
        self.cell_btn = btn;

    def left_click_action(self, event):
        print(event)
        print("left clicked")

    def right_click_action(self, event):
        print(event)
        print("right clicked")

    @staticmethod
    def randomize_mines():
        mines_list = random.sample(Cell.all, 9)
        for i in mines_list:
            i.is_mine = True
        pass

    def __repr__(self):
        return f"Cell(x:{self.x}, y:{self.y}, is_mine:{self.is_mine})"