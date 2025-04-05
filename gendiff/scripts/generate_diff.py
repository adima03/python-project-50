from pprint import pprint

from gendiff.diff_builder import build_diff
from gendiff.parsers import parse_data_from_file


def generate_diff(file_path1, file_path2, formatter='stylish'):
    first_file = parse_data_from_file(file_path1)
    second_file = parse_data_from_file(file_path2)
    diff = build_diff(first_file, second_file)
    # return format_identifier(diff, formatter)
    pprint(diff)
    return diff

