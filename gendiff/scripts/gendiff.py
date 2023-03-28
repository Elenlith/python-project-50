from gendiff.gendiff_with_formatter import generate_diff
from gendiff.argparser import get_args


def main():
    args = get_args()
    filepath_1 = args.first_file
    filepath_2 = args.second_file
    out_format = args.format
    print(generate_diff(filepath_1, filepath_2, out_format))


if __name__ == '__main__':
    main()
