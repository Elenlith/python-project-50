import argparse
import json
from gendiff.modules.get_difference import generate_diff


def main():
    text = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
