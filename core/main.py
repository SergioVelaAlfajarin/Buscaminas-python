from tkinter import *
import settings
import utils 

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

    # lanza la ventana
    root.mainloop()

if __name__ == '__main__':
    main()