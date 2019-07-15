class Column:

    def __init__(self, title=None, required=True):
        self.title = title
        self.required = required

    def attach_to_class(self,cls,name,dialect):
        self.cls = cls
        self.name = name
        self.dialect = dialect
        if self.title is None:
            self.title = name.replace('_',' ')
        dialect.add_column(self)
