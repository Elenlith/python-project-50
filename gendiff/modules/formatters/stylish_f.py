def repr_el(elem):
    if type(elem) is bool and elem is True:
        result = 'true'
    elif type(elem) is bool and elem is False:
        result = 'false'
    elif elem is None:
        result = 'null'
    else:
        result = elem
    return result


def stylish(diff, indent=1):
    result = '{' + '\n'
    for i in list(diff.keys()):
        if i[0] == '+':
            j = (indent - 1) * '    ' + '  + ' + i[2:]
        elif i[0] == '-':
            j = (indent - 1) * '    ' + '  - ' + i[2:]
        else:
            j = indent * '    ' + i
        if type(diff[i]) is dict:
            result += j + ': ' + stylish(repr_el(diff[i]), indent + 1) + '\n'
        else:
            result += j + ': ' + str(repr_el(diff[i])) + '\n'
    if result[-1] == '}':
        result += '\n' + (indent - 1) * '    ' + '}'
    else:
        result += (indent - 1) * '    ' + '}'
    return result
