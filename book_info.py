def read_a_quote(title):
    i = 0
    quotes = open("famousquotes.txt", "r")
    print(title.capitalize() + " Quotes: ")
    for line in quotes:
        if line.lower().__contains__(title):
            i += 1
            print(quotes.readline())
    if i == 0:
        print("There were no results")
    quotes.close()


def clear_quotes():
    quotes = open("famousquotes.txt", "w")
    quotes.write("")
    print("Quotes have been cleared")
    quotes.close()


class Book:
    def __init__(self, title, author, quote):
        self.title = title
        self.author = author
        self.quote = quote

    def write_a_quote(self):
        quotes = open("famousquotes.txt", "a")
        quotes.write(self.author + ", " + self.title + "\n" + "'" + self.quote + "'" + "\n\n")
        print("Your quote has been added!")
        quotes.close()

