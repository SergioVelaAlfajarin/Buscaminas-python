from tkinter import Button

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn = None

    def create_button(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text="Text"
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
