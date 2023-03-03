import argparse
from gendiff.get_difference import generate_diff
from gendiff.parsing import parse_data


def main():
    text = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', help='set format of output',
        default='stylish'
    )
    args = parser.parse_args()
    out_format = args.format
    file1 = parse_data(args.first_file)
    file2 = parse_data(args.second_file)
    print(generate_diff(file1, file2, out_format))


if __name__ == '__main__':
    main()
