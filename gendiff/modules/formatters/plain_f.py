from gendiff.modules.converter import repr_el


def repr(elem):
    if type(elem) is dict:
        val = '[complex value]'
    elif type(elem) is not bool and elem is not None:
        val = f"'{str(repr_el(elem))}'"
    else:
        val = repr_el(elem)
    return val


def plain(diff, name=''):
    r = ''
    for i in list(diff.keys()):
        f_name = name + i[2:]
        if i[0] == '+':
            val = repr(diff[i])
            r += f"Property '{f_name}' was added with value: {val}\n"
        elif i[0] == '-':
            r += f"Property '{f_name}' was removed\n"
        elif i[0] == '!' and type(diff[i]) is list:
            val1 = repr(diff[i][0])
            val2 = repr(diff[i][1])
            r += f"Property '{f_name}' was updated. From {val1} to {val2}\n"
        elif i[0] == '!' and type(diff[i]) is dict:
            new_name = name + str(i[2:] + '.')
            r += plain(diff[i], new_name)
        else:
            pass
    return r
