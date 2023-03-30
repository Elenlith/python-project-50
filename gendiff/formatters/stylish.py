def represent_item(item, indent=1):
    result = ["{"]
    if isinstance(item, bool):
        return str(item).lower()
    elif item is None:
        return 'null'
    elif isinstance(item, dict):
        for key, val in item.items():
            result.append(f"{'  ' * indent}  {key}: "
                          f"{represent_item(val, indent + 2)}")
        result.append(f"{'  ' * (indent - 1)}}}")
    else:
        return item
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
                          f"{represent_item(item['old_value'], indent + 2)}\n")
            result.append(f"{'  ' * indent}+ {key}: "
                          f"{represent_item(item['new_value'], indent + 2)}\n")
        elif status == 'added':
            result.append(f"{'  ' * indent}+ {key}: "
                          f"{represent_item(item['value'], indent + 2)}\n")
        elif status == 'deleted':
            result.append(f"{'  ' * indent}- {key}: "
                          f"{represent_item(item['value'], indent + 2)}\n")
        else:
            result.append(f"{'  ' * indent}  {key}: "
                          f"{represent_item(item['value'], indent + 2)}\n")
    result = ''.join(result)
    return result


def stylish(diff):
    stylish_built = build_stylish(diff)
    result = str('{\n' + stylish_built + '}')
    return result
