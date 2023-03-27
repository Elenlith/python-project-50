from gendiff.gendiff_with_formatter import generate_diff
from gendiff.argparsing import get_args


def main():
    args = get_args()
    file1 = args.first_file
    file2 = args.second_file
    out_format = args.format
    print(generate_diff(file1, file2, out_format))


if __name__ == '__main__':
    main()
