class Book:

    def __init__(self, title, publisher, pages):
        self.title= title
        self.publisher = publisher
        self.pages = pages

    def __len__(self):
        return self.pages


class Ebook(Book):

    def __init__(self, title, publisher, pages, format_):
        self.format_ = format_
        super().__init__(title,publisher,pages)


if __name__ == "__main__":
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    print()
    for s in sorted([name for name, score in students if score==sorted([g for n, g in students])[1]]):
        print(s)



