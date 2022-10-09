from tkinter import *


root = Tk()

# establece parametros de root
root.configure(bg="black")
root.geometry('1280x720') #WIDTH X HEIGHT
root.title("Buscaminas")
root.resizable(False, False)


top_frame = Frame(root,bg="red",width=1280,height=180)
top_frame.place(x=0,y=0)


# lanza la ventana
root.mainloop()