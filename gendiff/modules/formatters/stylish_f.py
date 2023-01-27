from gendiff.modules.converter import repr_el


def stylish_start(diff, key, indent):
    if key[0] == '+':
        j = (indent - 1) * '    ' + '  + ' + key[2:]
    elif key[0] == '-':
        j = (indent - 1) * '    ' + '  - ' + key[2:]
    elif key[0] == '!' and type(diff[key]) is list:
        j = []
        j.append((indent - 1) * '    ' + '  - ' + key[2:])
        j.append((indent - 1) * '    ' + '  + ' + key[2:])
    elif key[0] == '!' and type(diff[key]) is dict:
        j = indent * '    ' + key[2:]
    else:
        j = indent * '    ' + key
    return j


def stylish_if_list(result, elem, j1, j2, indent):
    if type(elem[0]) is dict:
        result += j1 + ': ' + stylish(repr_el(elem[0]), indent + 1) + '\n'
    else:
        result += j1 + ': ' + str(repr_el(elem[0])) + '\n'
    if type(elem[1]) is dict:
        result += j2 + ': ' + stylish(repr_el(elem[1]), indent + 1) + '\n'
    else:
        result += j2 + ': ' + str(repr_el(elem[1])) + '\n'
    return result


def stylish_finish(result, indent):
    if result[-1] == '}':
        result += '\n' + (indent - 1) * '    ' + '}'
    else:
        result += (indent - 1) * '    ' + '}'
    return result


def stylish(diff, indent=1):
    r = '{' + '\n'
    j = ''
    j1 = ''
    j2 = ''
    for i in list(diff.keys()):
        j = stylish_start(diff, i, indent)
        if type(j) is list:
            j1 = j[0]
            j2 = j[1]
        if type(diff[i]) is dict:
            r += j + ': ' + stylish(repr_el(diff[i]), indent + 1) + '\n'
        elif type(diff[i]) is list:
            r = stylish_if_list(r, diff[i], j1, j2, indent)
        else:
            r += j + ': ' + str(repr_el(diff[i])) + '\n'
    r = stylish_finish(r, indent)
    return r
