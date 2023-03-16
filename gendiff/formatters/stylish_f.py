from gendiff.converter import repr_el


def repr_value(elem, indent=1):
    result = ["{"]
    if type(elem) is dict:
        for key, val in elem.items():
            val = repr_el(val)
            result.append(f"{'  ' * indent}  {key}: "
                          f"{repr_value(val, indent + 2)}")
        result.append(f"{'  ' * (indent - 1)}}}")
    else:
        return repr_el(elem)
    return '\n'.join(result)


def select_char(el_type):
    if el_type == 'added':
        char = '+'
    elif el_type == 'deleted':
        char = '-'
    else:
        char = ' '
    return char


def build_stylish(diff, indent=1):
    result = []
    for elem in diff:
        el_type = elem['type']
        key = elem['key']
        if el_type == 'nested':
            result.append(f"{'  ' * indent}  {key}: {{\n"
                          f"{build_stylish(elem['children'], indent + 2)}")
            result.append(f"{'  ' * (indent + 1)}}}\n")
        elif el_type == 'changed':
            result.append(f"{'  ' * indent}- {key}: "
                          f"{repr_value(elem['old_value'], indent + 2)}\n")
            result.append(f"{'  ' * indent}+ {key}: "
                          f"{repr_value(elem['new_value'], indent + 2)}\n")
        else:
            char = select_char(el_type)
            result.append(f"{'  ' * indent}{char} {key}: "
                          f"{repr_value(elem['value'], indent + 2)}\n")
    result = ''.join(result)
    return result


def stylish(diff):
    stylish_built = build_stylish(diff)
    result = str('{\n' + stylish_built + '}')
    return result
