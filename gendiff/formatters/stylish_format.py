def normalize_elem(elem):
    if type(elem) is bool and elem is True:
        result = 'true'
    elif type(elem) is bool and elem is False:
        result = 'false'
    elif elem is None:
        result = 'null'
    else:
        result = elem
    return result


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


def build_stylish(diff, indent=1):
    result = []
    for elem in diff:
        status = elem['type']
        key = elem['key']
        if status == 'nested':
            result.append(f"{'  ' * indent}  {key}: {{\n"
                          f"{build_stylish(elem['children'], indent + 2)}")
            result.append(f"{'  ' * (indent + 1)}}}\n")
        elif status == 'changed':
            result.append(f"{'  ' * indent}- {key}: "
                          f"{normalize_value(elem['old_value'], indent + 2)}\n")
            result.append(f"{'  ' * indent}+ {key}: "
                          f"{normalize_value(elem['new_value'], indent + 2)}\n")
        elif status == 'added':
            result.append(f"{'  ' * indent}+ {key}: "
                          f"{normalize_value(elem['value'], indent + 2)}\n")
        elif status == 'deleted':
            result.append(f"{'  ' * indent}- {key}: "
                          f"{normalize_value(elem['value'], indent + 2)}\n")
        else:
            result.append(f"{'  ' * indent}  {key}: "
                          f"{normalize_value(elem['value'], indent + 2)}\n")
    result = ''.join(result)
    return result


def stylish(diff):
    stylish_built = build_stylish(diff)
    result = str('{\n' + stylish_built + '}')
    return result
