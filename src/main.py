from tkinter import *
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
    ).place(x=0,y=0)

    left_frame = Frame(
        root, 
        bg="blue", 
        width=utils.width_prct(20), 
        height=utils.height_prct(80)
    ).place(x=0,y=utils.height_prct(20))

    center_frame = Frame(
        root,
        bg="green",
        width=utils.width_prct(80),
        height=utils.height_prct(80)
    ).place(x=utils.width_prct(20), y=utils.height_prct(20))
    
    btn1 = Button(
        center_frame,
        bg="white",
        text="button1"
    ).place(x=0,y=0)
    
    c1 = Cell()
    
    # lanza la ventana
    root.mainloop()

if __name__ == '__main__':
    main()