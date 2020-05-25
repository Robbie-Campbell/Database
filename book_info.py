def read_a_quote(title):
    i = 0
    quotes = open("famousquotes.txt", "r")
    print(title + " Quotes: ")
    for line in quotes:
        if line.lower().__contains__(title.lower()):
            i += 1
            print(line)
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
        the_quote = self.quote
        quotes.write(self.author + ", " + self.title + ":\n" + "'" + the_quote + "'" + "\n")
        print("Your quote has been added!")
        quotes.close()

