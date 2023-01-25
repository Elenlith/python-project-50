from gendiff.modules.converter import repr_el


def stylish(diff, indent=1):
    r = '{' + '\n'
    j = ''
    j1 = ''
    j2 = ''
    for i in list(diff.keys()):
        if i[0] == '+':
            j = (indent - 1) * '    ' + '  + ' + i[2:]
        elif i[0] == '-':
            j = (indent - 1) * '    ' + '  - ' + i[2:]
        elif i[0] == '!' and type(diff[i]) is list:
            j1 = (indent - 1) * '    ' + '  - ' + i[2:]
            j2 = (indent - 1) * '    ' + '  + ' + i[2:]
        elif i[0] == '!' and type(diff[i]) is dict:
            j = indent * '    ' + i[2:]
        else:
            j = indent * '    ' + i
        if type(diff[i]) is dict:
            r += j + ': ' + stylish(repr_el(diff[i]), indent + 1) + '\n'
        elif type(diff[i]) is list:
            if type(diff[i][0]) is dict:
                r += j1 + ': ' + stylish(repr_el(diff[i][0]), indent + 1) + '\n'
            else:
                r += j1 + ': ' + str(repr_el(diff[i][0])) + '\n'
            if type(diff[i][1]) is dict:
                r += j2 + ': ' + stylish(repr_el(diff[i][1]), indent + 1) + '\n'
            else:
                r += j2 + ': ' + str(repr_el(diff[i][1])) + '\n'
        else:
            r += j + ': ' + str(repr_el(diff[i])) + '\n'
    if r[-1] == '}':
        r += '\n' + (indent - 1) * '    ' + '}'
    else:
        r += (indent - 1) * '    ' + '}'
    return r
