def normalize_elem(item):
    if type(item) is bool and item is True:
        result = 'true'
    elif type(item) is bool and item is False:
        result = 'false'
    elif item is None:
        result = 'null'
    else:
        result = item
    return result


def normalize_value(item, indent=1):
    result = ["{"]
    if type(item) is dict:
        for key, val in item.items():
            val = normalize_elem(val)
            result.append(f"{'  ' * indent}  {key}: "
                          f"{normalize_value(val, indent + 2)}")
        result.append(f"{'  ' * (indent - 1)}}}")
    else:
        return normalize_elem(item)
    return '\n'.join(result)


def build_stylish(diff, indent=1):
    result = []
    for item in diff:
        status = item['type']
        key = item['key']
        if status == 'nested':
            result.append(f"{'  ' * indent}  {key}: {{\n"
                          f"{build_stylish(item['children'], indent + 2)}")
            result.append(f"{'  ' * (indent + 1)}}}\n")
        elif status == 'changed':
            result.append(f"{'  ' * indent}- {key}: "
                          f"{normalize_value(item['old_value'], indent + 2)}\n")
            result.append(f"{'  ' * indent}+ {key}: "
                          f"{normalize_value(item['new_value'], indent + 2)}\n")
        elif status == 'added':
            result.append(f"{'  ' * indent}+ {key}: "
                          f"{normalize_value(item['value'], indent + 2)}\n")
        elif status == 'deleted':
            result.append(f"{'  ' * indent}- {key}: "
                          f"{normalize_value(item['value'], indent + 2)}\n")
        else:
            result.append(f"{'  ' * indent}  {key}: "
                          f"{normalize_value(item['value'], indent + 2)}\n")
    result = ''.join(result)
    return result


def stylish(diff):
    stylish_built = build_stylish(diff)
    result = str('{\n' + stylish_built + '}')
    return result
