from gendiff.formatters.stylish_format import stylish
from gendiff.formatters.plain_format import plain
from gendiff.formatters.json_format import form_json
from gendiff.parsing import read_file, parse_data


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


def generate_diff(path_1, path_2, format='stylish'):
    first_file_string = read_file(path_1)
    second_file_string = read_file(path_2)
    file_1 = parse_data(path_1, first_file_string)
    file_2 = parse_data(path_2, second_file_string)
    if format == 'stylish':
        return stylish(make_diff(file_1, file_2))
    elif format == 'plain':
        return plain(make_diff(file_1, file_2))[:-1]
    elif format == 'json':
        return form_json(make_diff(file_1, file_2))
