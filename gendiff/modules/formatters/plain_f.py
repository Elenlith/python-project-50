from gendiff.modules.converter import repr_el


def repr(elem):
    if type(elem) is dict:
        val = '[complex value]'
    elif type(elem) is not bool and elem is not None:
        val = f"'{str(repr_el(elem))}'"
    else:
        val = repr_el(elem)
    return val


def plain_if_modified(r, i, elem, name):
    if type(elem) is list:
        val1 = repr(elem[0])
        val2 = repr(elem[1])
        r += f"Property '{name + i[2:]}' was updated. From {val1} to {val2}\n"
    else:
        new_name = name + str(i[2:] + '.')
        r += str(plain(elem, new_name))
    return r


def plain_handle_elem(r, name, diff, i):
    f_name = name + i[2:]
    if i[0] == '+':
        val = repr(diff[i])
        r += f"Property '{f_name}' was added with value: {val}\n"
    elif i[0] == '-':
        r += f"Property '{f_name}' was removed\n"
    elif i[0] == '!':
        r = plain_if_modified(r, i, diff[i], name)
    else:
        pass
    return r


def plain(diff, name=''):
    r = ''
    for i in list(diff.keys()):
        r = plain_handle_elem(r, name, diff, i)
    return r
