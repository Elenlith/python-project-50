from gendiff.converter import repr_el


def repr(elem):
    if type(elem) is dict:
        val = '[complex value]'
    elif type(elem) is not bool and elem is not None and elem != 0:
        val = f"'{str(repr_el(elem))}'"
    else:
        val = repr_el(elem)
    return val


def compose_name(name, elem):
    if len(name) > 1:
        f_name = name + '.' + elem['key']
    else:
        f_name = elem['key']
    return f_name


def plain(diff, name=''):
    res = []
    for elem in diff:
        status = elem['type']
        f_name = compose_name(name, elem)
        if status == 'nested':
            res.extend(plain(elem['children'], f_name))
        elif status == 'changed':
            old_value = repr(elem['old_value'])
            new_value = repr(elem['new_value'])
            res.append(
                f"Property '{f_name}' was updated. "
                f"From {old_value} to {new_value}\n")
        elif status == 'added':
            value = repr(elem['value'])
            res.append(f"Property '{f_name}' was added with value: {value}\n")
        elif status == 'deleted':
            res.append(f"Property '{f_name}' was removed\n")
    res = ''.join(res)
    return res
