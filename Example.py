import sheets


class Example(sheets.Row):
    title = sheets.Column()
    description = sheets.Column()


if __name__ == '__main__':
    print(Example.title)
