"""
This is an application which allows the user to enter book quotes into a file and find them later using author or
title to find all quotes of that sort at a later date.
"""

from book_info import Book, read_a_quote, clear_quotes
from base import *

read_or_write = input("Do you want to clear all quotes, read or write a quote?: ")
global adder
if read_or_write == "write":
    title = input("What is the title of the book?: ")
    author = input("What is the name of the author?: ")
    quote = input("Please write the desired quote: ")
    adder = Book(title, author, quote)
    adder.write_a_quote()

elif read_or_write == "read":
    search = input("What is: the name of the author or the name of the book: ")
    gui(read_a_quote(search))

elif read_or_write == "clear":
    sure = input("Are you sure you want to delete all messages?: ")
    if sure == "yes":
        clear_quotes()
    else:
        print("Thankyou for using the application")

mainloop()
