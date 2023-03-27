from gendiff.converter import normalize_elem


def represent_elem(elem):
    if type(elem) is dict:
        val = '[complex value]'
    elif type(elem) is not bool and elem is not None and elem != 0:
        val = f"'{str(normalize_elem(elem))}'"
    else:
        val = normalize_elem(elem)
    return val


def compose_name(name, elem):
    if len(name) > 1:
        full_name = name + '.' + elem['key']
    else:
        full_name = elem['key']
    return full_name


def plain(diff, name=''):
    result = []
    for elem in diff:
        status = elem['type']
        full_name = compose_name(name, elem)
        if status == 'nested':
            result.extend(plain(elem['children'], full_name))
        elif status == 'changed':
            old_value = represent_elem(elem['old_value'])
            new_value = represent_elem(elem['new_value'])
            result.append(
                f"Property '{full_name}' was updated. "
                f"From {old_value} to {new_value}\n")
        elif status == 'added':
            value = represent_elem(elem['value'])
            result.append(f"Property '{full_name}' was added "
                          f"with value: {value}\n")
        elif status == 'deleted':
            result.append(f"Property '{full_name}' was removed\n")
    result = ''.join(result)
    return result
