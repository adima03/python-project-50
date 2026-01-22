import json
import os

import yaml


def get_file_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:]


def read_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read()


def parse_data(data, file_format):
    if file_format == 'json':
        return json.loads(data)
    if file_format == 'yaml' or file_format == 'yml':
        return yaml.safe_load(data)
    raise ValueError(f'Unsupported file format: {file_format}')


def parse_data_from_file(file_path):
    data = read_file(file_path)
    file_format = get_file_format(file_path)
    return parse_data(data, file_format)
