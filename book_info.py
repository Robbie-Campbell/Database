from tkinter import messagebox


# The search query is run from here
def read_a_quote(title):
    i = 0
    current = 0
    result = ""
    quotes = open("famousquotes.txt", "r")
    quote = quotes.readlines()
    print(title + " Quotes: ")
    for line in quote:
        current += 1
        if current == len(quote):
            break
        elif line.lower().__contains__(title.lower()):
            i += 1
            result += line
            result += quote[current]
            print(i)
    quotes.close()
    return result


# This offers the user the option to remove all quotes from the database (will be updated shortly)
def clear_quotes():
    are_you_sure = messagebox.askyesno(title="Are you sure?", message="Are you sure you want to clear all quotes?")
    if are_you_sure:
        quotes = open("famousquotes.txt", "w")
        quotes.write("")
        print("Quotes have been cleared")
        quotes.close()


# The book class allows the user to assign a variable as a book object to be put into the famousquotes document
class Book:
    def __init__(self, title, author, quote):
        self.title = title
        self.author = author
        self.quote = quote

    def write_a_quote(self):
        quotes = open("famousquotes.txt", "a")
        the_quote = self.quote
        quotes.write(self.author + ", " + self.title + ":\n" + "'" + the_quote + "'" + "\n")
        print("Your quote has been added!")
        quotes.close()

