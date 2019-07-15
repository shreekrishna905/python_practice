class Dialect:
    """
    A container for dialect options that control how a CSV file should be handled when
    converting it to a set of objects.
    has_header_row
        A Boolean indication whether the file has row containing header values.
    """

    def __init__(self, has_header_row=False, **kwargs):
        self.has_header_row = has_header_row
        self.csv_dialect = kwargs
        self.columns = []

    def add_column(self, column):
        self.columns.append(column)
