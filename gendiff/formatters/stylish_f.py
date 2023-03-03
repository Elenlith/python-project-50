from gendiff.converter import repr_el


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


def stylish_if_list(result, elem, j, indent):
    for (i, _) in enumerate(elem):
        if type(elem[i]) is dict:
            result += j[i] + ': ' + stylish(repr_el(elem[i]), indent + 1) + '\n'
        else:
            result += j[i] + ': ' + str(repr_el(elem[i])) + '\n'
    return result


def stylish_finish(result, indent):
    if result[-1] == '}':
        result += '\n' + (indent - 1) * '    ' + '}'
    else:
        result += (indent - 1) * '    ' + '}'
    return result


def stylish(diff, indent=1):
    r = '{' + '\n'
    for i in list(diff.keys()):
        j = stylish_start(diff, i, indent)
        if type(diff[i]) is dict:
            r += j + ': ' + stylish(repr_el(diff[i]), indent + 1) + '\n'
        elif type(diff[i]) is list:
            r = stylish_if_list(r, diff[i], j, indent)
        else:
            r += j + ': ' + str(repr_el(diff[i])) + '\n'
    r = stylish_finish(r, indent)
    return r
