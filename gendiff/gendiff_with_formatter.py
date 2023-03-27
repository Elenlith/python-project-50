from gendiff.formatters.stylish_format import stylish
from gendiff.formatters.plain_format import plain
from gendiff.formatters.json_format import form_json
from gendiff.parsing import read_file, parse_data
from gendiff.get_difference import make_diff


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
