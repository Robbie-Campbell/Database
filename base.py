from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Quotes storage")

top = Toplevel()
image = ImageTk.PhotoImage(Image.open("C:/img/loader.gif"))
label = Label(top, image=image)
label.pack()
top.title("Hello")

mainloop()
