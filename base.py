from tkinter import *
from book_info import read_a_quote, clear_quotes, Book

# Set GUI items for all functions used.
root = Tk()
root.title("Quotes storage")
frame = Frame(root, background="bisque")
frame.pack(fill=None, expand=False)
query = Entry(frame)
frame.grid_columnconfigure(0, weight=2)
query.grid(row=0, column=0, ipadx=260, ipady=10)
text_area = Frame(frame, width=20, height=30)


# Function to return results for a given search
def search_query():
    selector = read_a_quote(query.get())
    if query.get() == "":
        results("Please input a value")
    else:
        results(selector)


# Sets the results of the query onto a label object
def results(packer):
    answer = str(packer)
    label = Label(frame, text=answer)
    label.grid(row=1, column=0)
    refresh = Button(frame, width=12, height=2, text="Refresh results", command=lambda: refresh_search())
    refresh.grid(row=0, column=1)
    clearer.grid_forget()
    writer.grid_forget()
    searcher.grid_forget()

    # Resets the search bar
    def refresh_search():
        label.grid_forget()
        refresh.grid_forget()
        query.delete(0, END)
        add_buttons()


# Writes a quote to the document
def write():
    # Remove initial buttons
    searcher.grid_forget()
    clearer.grid_forget()
    writer.grid_forget()

    # Create and place label prompts for input
    label_author = Label(frame, text="Input author.")
    label_title = Label(frame, text="Input title")
    label_quote = Label(frame, text="Input quote")
    label_author.grid(row=0, column=1)
    label_title.grid(row=1, column=1)
    label_quote.grid(row=2, column=1)

    # Create a button to input quote values
    add_quote = Button(frame, width=12, height=2, text="Add your quote", command=lambda: write_quote("Congratulations, "
                                                                                                     "your quote has "
                                                                                                     "been added!"))
    add_quote.grid(row=0, column=2)

    # Return option if the user doesn't want to enter a quote
    return_home = Button(frame, width=12, height=2, text="Return", command=lambda: write_quote(""))
    return_home.grid(row=2, column=2)

    # Create text fields to take in information
    title = Entry(frame)
    title.grid(row=1, column=0, ipadx=260, ipady=10)
    text_area.grid(row=2, column=0, sticky="nsew")
    quote = Text(text_area)
    quote.pack()

    def write_quote(value):
        # Get the values in the text fields
        author = query.get()
        title_value = title.get()
        quote_value = quote.get("1.0", END)

        # Write the values to the file
        file = Book(title_value, author, quote_value)

        # Remove all added buttons and return to base state.
        file.write_a_quote()
        label_quote.grid_forget()
        label_author.grid_forget()
        label_title.grid_forget()
        confirmation = Label(frame, text=value)
        confirmation.grid(row=1, column=0)
        title.grid_forget()
        text_area.grid_forget()
        add_quote.grid_forget()
        return_home.grid_forget()
        query.delete(0, END)
        add_buttons()


# The three standard buttons for the quotes functions
searcher = Button(frame, width=12, height=2, text="Search for a book", command=lambda: search_query())
clearer = Button(frame, width=12, height=2, text="Clear all quotes", command=lambda: clear_quotes())
writer = Button(frame, width=12, height=2, text="Write a quote", command=lambda: write())


# A function to place the buttons both on the main screen and after writing a quote
def add_buttons():
    searcher.grid(row=0, column=1)
    clearer.grid(row=1, column=1)
    writer.grid(row=2, column=1)


add_buttons()
