def represent_item(item, depth=1):
    result = ["{"]
    if isinstance(item, bool):
        return str(item).lower()
    elif item is None:
        return 'null'
    elif isinstance(item, dict):
        for key, val in item.items():
            result.append(f"{make_indent(depth + 1)}{key}: "
                          f"{represent_item(val, depth + 1)}")
        result.append(f"{make_indent(depth)}}}")
    else:
        return item
    return '\n'.join(result)


def make_indent(depth, char=''):
    if char:
        return ' ' * (4 * depth - 2)
    else:
        return '    ' * depth


def build_stylish(diff, depth=1):
    result = []
    for item in diff:
        status = item['type']
        key = item['key']
        if status == 'nested':
            result.append(f"{make_indent(depth)}{key}: {{\n"
                          f"{build_stylish(item['children'], depth + 1)}")
            result.append(f"{make_indent(depth)}}}\n")
        elif status == 'changed':
            result.append(f"{make_indent(depth, '-')}- {key}: "
                          f"{represent_item(item['old_value'], depth)}\n")
            result.append(f"{make_indent(depth, '+')}+ {key}: "
                          f"{represent_item(item['new_value'], depth)}\n")
        elif status == 'added':
            result.append(f"{make_indent(depth, '+')}+ {key}: "
                          f"{represent_item(item['value'], depth)}\n")
        elif status == 'deleted':
            result.append(f"{make_indent(depth, '-')}- {key}: "
                          f"{represent_item(item['value'], depth)}\n")
        else:
            result.append(f"{make_indent(depth)}{key}: "
                          f"{represent_item(item['value'], depth)}\n")
    result = ''.join(result)
    return result


def stylish(diff):
    stylish_built = build_stylish(diff)
    result = str('{\n' + stylish_built + '}')
    return result
