def represent_item_plain(item):
    if type(item) is bool and item is True:
        item_value = 'true'
    elif type(item) is bool and item is False:
        item_value = 'false'
    elif item is None:
        item_value = 'null'
    else:
        item_value = item
    if type(item) is dict:
        plain_value = '[complex value]'
    elif type(item) is not bool and item is not None and item != 0:
        plain_value = f"'{str(item_value)}'"
    else:
        plain_value = item_value
    return plain_value


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
            result.extend(plain(item['children'], full_name))
        elif status == 'changed':
            old_value = represent_item_plain(item['old_value'])
            new_value = represent_item_plain(item['new_value'])
            result.append(
                f"Property '{full_name}' was updated. "
                f"From {old_value} to {new_value}\n")
        elif status == 'added':
            value = represent_item_plain(item['value'])
            result.append(f"Property '{full_name}' was added "
                          f"with value: {value}\n")
        elif status == 'deleted':
            result.append(f"Property '{full_name}' was removed\n")
    result = ''.join(result)
    return result
