from gendiff.formatters.stylish_f import stylish
from gendiff.formatters.plain_f import plain
from gendiff.formatters.json_f import form_json
from gendiff.parsing import read_file, parse_data


def mod_check(a, b, i, diff):
    if type(a) == dict and type(b) == dict:
        diff['!_' + i] = make_diff(a, b)
    else:
        diff[('!_' + i)] = [a, b]
    return diff


def make_diff(f_1, f_2):
    file1_keys = set(f_1.keys())
    file2_keys = set(f_2.keys())
    all_keys = list(file1_keys.union(file2_keys))
    all_keys.sort()
    sh_keys = file1_keys.intersection(file2_keys)
    added = file2_keys - file1_keys
    removed = file1_keys - file2_keys
    unchanged = {i: (f_1[i], f_2[i]) for i in sh_keys if f_1[i] == f_2[i]}
    diff = {}
    for i in all_keys:
        if i in added:
            diff[('+_' + i)] = f_2[i]
        elif i in removed:
            diff[('-_' + i)] = f_1[i]
        elif i in unchanged:
            diff[i] = f_1[i]
        else:
            diff = mod_check(f_1[i], f_2[i], i, diff)
    return diff


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
