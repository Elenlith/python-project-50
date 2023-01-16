import argparse
import os
from gendiff.modules.get_difference import generate_diff
from gendiff.modules.parsing import parse_json, parse_yaml


def main():
    text = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    ext1 = os.path.splitext(args.first_file)[-1].lower()
    ext2 = os.path.splitext(args.first_file)[-1].lower()
    if ext1 == '.json' and ext2 == '.json':
        file1 = parse_json(args.first_file)
        file2 = parse_json(args.second_file)
        print(generate_diff(file1, file2))
    elif ext1 == '.yml' or '.yaml' and ext2 == '.yml' or '.yaml':
        file1 = parse_yaml(args.first_file)
        file2 = parse_yaml(args.second_file)
        print(generate_diff(file1, file2))
    else:
        print('Wrong files format')


if __name__ == '__main__':
    main()
