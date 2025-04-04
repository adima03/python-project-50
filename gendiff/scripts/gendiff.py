import argparse
import json

import yaml

from gendiff import parsing


def generate_diff(file1, file2):
    try:
        data1 = parsing.read_json_file(file1)
        data2 = parsing.read_json_file(file2)
    except:
        try:
            data1 = parsing.read_yaml_file(file1)
            data2 = parsing.read_yaml_file(file2)
        except yaml.YAMLError as e:
            raise ValueError(f"Файл не является JSON или YAML: {e}")

    # data1 = read_json_file(file1)
    # data2 = read_json_file(file2)
    all_keys = sorted(set(data1.keys()) | (data2.keys()))
    result = ["{"]

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in data1 and key not in data2:
            result.append(f"  - {key}: {json.dumps(value1)}")
        elif key in data2 and key not in data1:
            result.append(f"  + {key}: {json.dumps(value2)}")
        elif value1 != value2:
            result.append(f"  - {key}: {json.dumps(value1)}")
            result.append(f"  + {key}: {json.dumps(value2)}")
        else:
            result.append(f"    {key}: {json.dumps(value1)}")

    result.append("}")

    return "\n".join(result)


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='Set format of output')

    args = parser.parse_args()

    try:
        result = generate_diff(args.first_file, args.second_file)
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


