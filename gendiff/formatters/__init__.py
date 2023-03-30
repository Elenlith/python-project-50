from .stylish import stylish
from .plain import plain
from .json import form_json


def apply_format(difference, format):
    if format == 'stylish':
        return stylish(difference)
    elif format == 'plain':
        return plain(difference)
    elif format == 'json':
        return form_json(difference)
    else:
        raise NameError('Wrong format name')
