import json
import os

import yaml


def read_json_file(path_to_file):
    if not os.path.isfile(path_to_file):
        raise FileNotFoundError(f"The file {path_to_file} does not exist.")
    with open(path_to_file) as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding \
            JSON from file {path_to_file}: {e}")


def read_yaml_file(path_to_file):
    if not os.path.isfile(path_to_file):
        raise FileNotFoundError(f"The file {path_to_file} does not exist.")
    with open(path_to_file, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error decoding YAML from file {path_to_file}: {e}")
