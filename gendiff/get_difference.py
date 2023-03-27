def make_diff(file_1, file_2):
    file1_keys = set(file_1.keys())
    file2_keys = set(file_2.keys())
    all_keys = list(file1_keys.union(file2_keys))
    all_keys.sort()
    diff_dict = []
    for key in all_keys:
        if key not in file_2:
            diff_dict.append({'key': key, 'type': 'deleted',
                              'value': file_1[key]})
        elif key not in file_1:
            diff_dict.append({'key': key, 'type': 'added',
                              'value': file_2[key]})
        elif isinstance(file_1[key], dict) and isinstance(file_2[key], dict):
            children = make_diff(file_1[key], file_2[key])
            diff_dict.append({'key': key, 'type': 'nested',
                              'children': children})
        elif file_1[key] == file_2[key]:
            diff_dict.append({'key': key, 'type': 'unchanged',
                              'value': file_1[key]})
        else:
            diff_dict.append({'key': key, 'type': 'changed',
                              'old_value': file_1[key],
                              'new_value': file_2[key]})
    return diff_dict
