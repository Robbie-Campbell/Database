from tkinter import *

root = Tk()

root.title("Quotes storage")


def gui(packer):
    top = Toplevel()
    label = Label(top, text=packer)
    label.pack()
    top.title("These are the quotes")
