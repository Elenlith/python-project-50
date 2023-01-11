def generate_diff(first_file, second_file):
    file1_keys = set(first_file.keys())
    file2_keys = set(second_file.keys())
    all_keys = list(file1_keys.union(file2_keys))
    all_keys.sort()
    shared_keys = file1_keys.intersection(file2_keys)
    added = file2_keys - file1_keys
    removed = file1_keys - file2_keys
    modified = {i: (first_file[i], second_file[i]) for i in shared_keys if first_file[i] != second_file[i]}
    difference = '{'
    for i in all_keys:
        if i in added:
            difference += str(f'\n+ {i}: {second_file[i]}')
        elif i in removed:
            difference += str(f'\n- {i}: {first_file[i]}')
        elif i in modified:
            difference += str(f'\n- {i}: {first_file[i]}\n+ {i}: {second_file[i]}')
        else:
            difference += str(f'\n  {i}: {first_file[i]}')
    difference += '\n}'
    return difference
