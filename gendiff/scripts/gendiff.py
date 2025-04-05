import argparse
import json

from gendiff.parsing import read_file


def generate_diff(file1, file2):
    try:
        data1 = read_file(file1)
        data2 = read_file(file2)

        if not isinstance(data1, dict) or not isinstance(data2, dict):
            raise ValueError("Данные в файлах должны быть словарями.")

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Ошибка при чтении файла: {e}")
    except ValueError as e:
        raise ValueError(f"Ошибка при обработке данных: {e}")

    all_keys = sorted(set(data1.keys()).union(data2.keys()))
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


