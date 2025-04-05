import argparse

from gendiff.diff_builder import build_diff
from gendiff.formatters.stylish import format_diff_stylish
from gendiff.parsers import parse_data_from_file


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_data_from_file(file1)
    data2 = parse_data_from_file(file2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_diff_stylish(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")


def main():
    parser = argparse.ArgumentParser(description="Generate "
                                                 "diff between two files.")
    parser.add_argument("file1", help="Path to the first file")
    parser.add_argument("file2", help="Path to the second file")
    parser.add_argument("-f", "--format", default="stylish",
                        help="Output format (default: stylish)")
    args = parser.parse_args()

    print(generate_diff(args.file1, args.file2, args.format))


if __name__ == "__main__":
    main()