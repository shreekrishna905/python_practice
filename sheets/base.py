from sheets import options
from collections import OrderedDict


class RowMeta(type):

    def __init__(cls, name, bases, attrs):

        if 'Dialect' in attrs:
            items = attrs.pop('Dialect').__dict__.items()
            items = {k:v for k, v in items if not k.startswith('__')}
        else:
            items = {}
        cls._dialect = options.Dialect(**items)
        for key, attr in attrs.items():
            if hasattr(attr, 'attach_to_class'):
                attr.attach_to_class(cls,key, cls._dialect)

    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()


class Row(metaclass=RowMeta):
    pass