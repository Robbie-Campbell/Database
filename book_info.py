def read_a_quote(title):
    i = 0
    current = 0
    result = ""
    quotes = open("famousquotes.txt", "r")
    quote = quotes.readlines()
    print(title + " Quotes: ")
    for line in quote:
        current += 1
        if line.lower().__contains__(title.lower()):
            i += 1
            print(line)
            print(quote)
            result += line
            result += quote[current]
    if i == 0:
        print("There were no results")
    quotes.close()
    return result


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

