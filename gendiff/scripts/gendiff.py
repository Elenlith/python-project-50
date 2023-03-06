import argparse
from gendiff.get_difference import generate_diff


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
    file1 = args.first_file
    file2 = args.second_file
    out_format = args.format
    print(generate_diff(file1, file2, out_format))


if __name__ == '__main__':
    main()
