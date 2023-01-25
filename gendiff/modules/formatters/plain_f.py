def plain(diff):
    result = ''
    for i in list(diff.keys()):
        if i[0] == '+' and diff[i] is dict:
            result += f'Property {i[2:]} was added with value: [complex value]\n'
        elif i[0] == '+' and diff[i] is not dict:
            result += f'Property {i[2:]} was added with value: {diff[i]}\n'
        elif i[0] == '-':
            result += f'Property {i[2:]} was removed\n'
        else:
            if type(diff[i]) is dict:
                result += plain(diff[i])
            else:
                pass
    return result
