import argparse
import sys
from pathlib import Path

# Fix import path when running script directly
# Remove the script's directory from sys.path to avoid conflicts
script_dir = Path(__file__).resolve().parent
script_dir_str = str(script_dir)
if script_dir_str in sys.path:
    sys.path.remove(script_dir_str)

# Add project root to Python path (two levels up from this script)
project_root = script_dir.parent.parent
project_root_str = str(project_root)
if project_root_str not in sys.path:
    sys.path.insert(0, project_root_str)

from gendiff.formatters.json import format_diff_json  # noqa: E402
from gendiff.formatters.plain import format_diff_plain  # noqa: E402
from gendiff.formatters.stylish import format_diff_stylish  # noqa: E402
from gendiff.scripts.diff_builder import build_diff  # noqa: E402
from gendiff.scripts.parsers import parse_data_from_file  # noqa: E402


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_data_from_file(file1)
    data2 = parse_data_from_file(file2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_diff_stylish(diff)
    if format_name == 'plain':
        return format_diff_plain(diff)
    if format_name == 'json':
        return format_diff_json(diff)
    else:
        raise ValueError(f"Unsupported formatter: {format_name}")


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