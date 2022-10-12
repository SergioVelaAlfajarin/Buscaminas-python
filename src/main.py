from tkinter import *
from tkinter.tix import COLUMN
import settings
import utils 
from cell import Cell

def main():
    root = Tk()

    # establece parametros de root
    root.configure(bg="black")
    root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
    root.title("Buscaminas")
    root.resizable(False, False)

    top_frame = Frame(
        root,
        bg="red",
        width=utils.width_prct(100),
        height=utils.height_prct(20)
    )
    top_frame.place(x=0,y=0)

    left_frame = Frame(
        root, 
        bg="blue", 
        width=utils.width_prct(20), 
        height=utils.height_prct(80)
    )
    left_frame.place(x=0,y=utils.height_prct(20))

    center_frame = Frame(
        root,
        bg="green",
        width=utils.width_prct(80),
        height=utils.height_prct(80)
    )
    center_frame.place(x=utils.width_prct(20), y=utils.height_prct(20))

    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            c = Cell(x,y)
            c.create_button(center_frame)
            c.cell_btn.grid(column=c.y,row=c.x)
    
    Cell.randomize_mines()

    print(Cell.all)
    
    
    # lanza la ventana
    root.mainloop()

if __name__ == '__main__':
    main()