from gendiff.converter import normalize_elem


def normalize_value(elem, indent=1):
    result = ["{"]
    if type(elem) is dict:
        for key, val in elem.items():
            val = normalize_elem(val)
            result.append(f"{'  ' * indent}  {key}: "
                          f"{normalize_value(val, indent + 2)}")
        result.append(f"{'  ' * (indent - 1)}}}")
    else:
        return normalize_elem(elem)
    return '\n'.join(result)


def select_char(elem_type):
    if elem_type == 'added':
        char = '+'
    elif elem_type == 'deleted':
        char = '-'
    else:
        char = ' '
    return char


def build_stylish(diff, indent=1):
    result = []
    for elem in diff:
        elem_type = elem['type']
        key = elem['key']
        if elem_type == 'nested':
            result.append(f"{'  ' * indent}  {key}: {{\n"
                          f"{build_stylish(elem['children'], indent + 2)}")
            result.append(f"{'  ' * (indent + 1)}}}\n")
        elif elem_type == 'changed':
            result.append(f"{'  ' * indent}- {key}: "
                          f"{normalize_value(elem['old_value'], indent + 2)}\n")
            result.append(f"{'  ' * indent}+ {key}: "
                          f"{normalize_value(elem['new_value'], indent + 2)}\n")
        else:
            char = select_char(elem_type)
            result.append(f"{'  ' * indent}{char} {key}: "
                          f"{normalize_value(elem['value'], indent + 2)}\n")
    result = ''.join(result)
    return result


def stylish(diff):
    stylish_built = build_stylish(diff)
    result = str('{\n' + stylish_built + '}')
    return result
