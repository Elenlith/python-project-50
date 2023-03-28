def represent_item_plain(item):
    if type(item) is bool:
        return str(item).lower()
    elif item is None:
        return 'null'
    elif type(item) is dict:
        return '[complex value]'
    elif type(item) is int:
        return item
    else:
        return f"'{item}'"


def compose_name(name, item):
    if name:
        full_name = name + '.' + item['key']
    else:
        full_name = item['key']
    return full_name


def plain(diff, name=''):
    result = []
    for item in diff:
        status = item['type']
        full_name = compose_name(name, item)
        if status == 'nested':
            result.append(plain(item['children'], full_name))
        elif status == 'changed':
            old_value = represent_item_plain(item['old_value'])
            new_value = represent_item_plain(item['new_value'])
            result.append(
                f"Property '{full_name}' was updated. "
                f"From {old_value} to {new_value}")
        elif status == 'added':
            value = represent_item_plain(item['value'])
            result.append(f"Property '{full_name}' was added "
                          f"with value: {value}")
        elif status == 'deleted':
            result.append(f"Property '{full_name}' was removed")
    result = '\n'.join(result)
    return result
