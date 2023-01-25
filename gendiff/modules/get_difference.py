from gendiff.modules.formatters.stylish_f import stylish
from gendiff.modules.formatters.plain_f import plain


def make_diff(f_1, f_2):
    file1_keys = set(f_1.keys())
    file2_keys = set(f_2.keys())
    all_keys = list(file1_keys.union(file2_keys))
    all_keys.sort()
    sh_keys = file1_keys.intersection(file2_keys)
    added = file2_keys - file1_keys
    removed = file1_keys - file2_keys
    modified = {i: (f_1[i], f_2[i]) for i in sh_keys if f_1[i] != f_2[i]}
    unchanged = {i: (f_1[i], f_2[i]) for i in sh_keys if f_1[i] == f_2[i]}
    diff = {}
    for i in all_keys:
        if i in added:
            diff[('+ ' + i)] = f_2[i]
        elif i in removed:
            diff[('- ' + i)] = f_1[i]
        elif i in unchanged:
            diff[i] = f_1[i]
        elif i in modified:
            if type(f_1[i]) == dict and type(f_2[i]) == dict:
                diff[i] = make_diff(f_1[i], f_2[i])
            else:
                diff[('- ' + i)] = f_1[i]
                diff[('+ ' + i)] = f_2[i]
    return diff


def generate_diff(f_1, f_2, format='stylish'):
    if format == 'stylish':
        return stylish(make_diff(f_1, f_2))
    elif format == 'plain':
        return plain(make_diff(f_1, f_2))
