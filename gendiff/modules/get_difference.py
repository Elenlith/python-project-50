def repr_el(elem):
    if type(elem) is bool and elem is True:
        result = 'true'
    elif type(elem) is bool and elem is False:
        result = 'false'
    else:
        result = elem
    return result


def generate_diff(f_1, f_2):
    file1_keys = set(f_1.keys())
    file2_keys = set(f_2.keys())
    all_keys = list(file1_keys.union(file2_keys))
    all_keys.sort()
    sh_keys = file1_keys.intersection(file2_keys)
    added = file2_keys - file1_keys
    removed = file1_keys - file2_keys
    modified = {i: (f_1[i], f_2[i]) for i in sh_keys if f_1[i] != f_2[i]}
    diff = '{'
    for i in all_keys:
        if i in added:
            diff += str(f'\n+ {i}: {repr_el(f_2[i])}')
        elif i in removed:
            diff += str(f'\n- {i}: {repr_el(f_1[i])}')
        elif i in modified:
            diff += str(f'\n- {i}: {repr_el(f_1[i])}\n+ {i}: {repr_el(f_2[i])}')
        else:
            diff += str(f'\n  {i}: {repr_el(f_1[i])}')
    diff += '\n}'
    return diff
