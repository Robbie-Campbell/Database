from tkinter import *
from book_info import read_a_quote, clear_quotes


def search_query():
    selector = read_a_quote(query.get())
    results(selector)


def results(packer):
    answer = str(packer)
    label = Label(frame, text=answer)
    label.grid(row=1, column=0)


root = Tk()
root.title("Quotes storage")
frame = Frame(root, width=800, height=300, background="bisque")
frame.grid(row=0, column=0)
query = Entry(frame)
query.grid(row=0, column=0, ipadx=12, ipady=10)


searcher = Button(frame, width=12, height=2, text="search for a book", command=lambda: search_query())
clearer = Button(frame, width=12, height=2, text="Clear all quotes", command=lambda: clear_quotes())
clearer.grid(row=1, column=1)
searcher.grid(row=0, column=1)




