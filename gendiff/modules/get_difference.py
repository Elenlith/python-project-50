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


def make_diff(f_1, f_2):
    file1_keys = set(f_1.keys())
    file2_keys = set(f_2.keys())
    all_keys = list(file1_keys.union(file2_keys))
    all_keys.sort()
    sh_keys = file1_keys.intersection(file2_keys)
    added = file2_keys - file1_keys
    removed = file1_keys - file2_keys
    modified = {i: (f_1[i], f_2[i]) for i in sh_keys if f_1[i] != f_2[i]}
    unchanged = {i: (f_1[i], f_2[i]) for i in sh_keys if f_1[i] == f_2[i]}
    diff = {}
    for i in all_keys:
        if i in added:
            diff[('+ ' + i)] = f_2[i]
        elif i in removed:
            diff[('- ' + i)] = f_1[i]
        elif i in unchanged:
            diff[i] = f_1[i]
        elif i in modified:
            if type(f_1[i]) == dict and type(f_2[i]) == dict:
                diff[i] = make_diff(f_1[i], f_2[i])
            else:
                diff[('- ' + i)] = f_1[i]
                diff[('+ ' + i)] = f_2[i]
    return diff


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


def generate_diff(f_1, f_2):
    return stylish(make_diff(f_1, f_2))
