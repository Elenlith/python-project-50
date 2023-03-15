from gendiff.formatters.stylish_f import stylish
from gendiff.formatters.plain_f import plain
from gendiff.formatters.json_f import form_json
from gendiff.parsing import read_file, parse_data


def make_diff(f_1, f_2):
    file1_keys = set(f_1.keys())
    file2_keys = set(f_2.keys())
    all_keys = list(file1_keys.union(file2_keys))
    all_keys.sort()
    diff_dict = []
    for key in all_keys:
        if key not in f_2:
            diff_dict.append({'key': key, 'type': 'deleted', 'value': f_1[key]})
        elif key not in f_1:
            diff_dict.append({'key': key, 'type': 'added', 'value': f_2[key]})
        elif isinstance(f_1[key], dict) and isinstance(f_2[key], dict):
            children = make_diff(f_1[key], f_2[key])
            diff_dict.append({'key': key, 'type': 'nested',
                              'children': children})
        elif f_1[key] == f_2[key]:
            diff_dict.append({'key': key, 'type': 'unchanged',
                              'value': f_1[key]})
        else:
            diff_dict.append({'key': key, 'type': 'changed',
                              'old_value': f_1[key], 'new_value': f_2[key]})
    return diff_dict


def generate_diff(path_1, path_2, format='stylish'):
    f_1_str = read_file(path_1)
    f_2_str = read_file(path_2)
    f_1 = parse_data(path_1, f_1_str)
    f_2 = parse_data(path_2, f_2_str)
    if format == 'stylish':
        return stylish(make_diff(f_1, f_2))
    elif format == 'plain':
        return plain(make_diff(f_1, f_2))[:-1]
    elif format == 'json':
        return form_json(make_diff(f_1, f_2))
