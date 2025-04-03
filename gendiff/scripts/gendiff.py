import argparse
import json


def generate_diff(file1, file2):
    data1 = read_json_file(file1)
    data2 = read_json_file(file2)
    all_keys = sorted(set(data1.keys()).union(data2.keys()))
    result = ["{"]
    for key in all_keys:
        value1 = data1.get(key, None)
        value2 = data2.get(key, None)
        
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

def read_json_file(path_to_file):
    with open(path_to_file, 'r') as file:
        data = json.load(file)
    return data
    


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    # позиционные
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # опциональные
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file)

    print(result)


if __name__ == "__main__":
    main()