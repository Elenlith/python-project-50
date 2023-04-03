from gendiff.formatters import apply_format
from gendiff.parser import read_file, parse_data
from gendiff.difference_evaluation import make_diff


def generate_diff(path_1, path_2, format='stylish'):
    first_file_string = read_file(path_1)
    second_file_string = read_file(path_2)
    file_1 = parse_data(path_1, first_file_string)
    file_2 = parse_data(path_2, second_file_string)
    difference = make_diff(file_1, file_2)
    result = apply_format(difference, format)
    return result
