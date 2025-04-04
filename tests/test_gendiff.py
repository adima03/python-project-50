import json
import tempfile
from gendiff.scripts.gendiff import generate_diff


def create_temp_json_file(data):
    file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    json.dump(data, file)
    file.close()
    return file.name


def test_generate_diff_identical_files():
    data = {"host": "hexlet.io", "timeout": 50}
    file1 = create_temp_json_file(data)
    file2 = create_temp_json_file(data)

    expected_output = """{
    host: "hexlet.io"
    timeout: 50
}"""
    assert generate_diff(file1, file2) == expected_output


def test_generate_diff_different_keys():
    data1 = {"host": "hexlet.io", "timeout": 50}
    data2 = {"timeout": 20, "verbose": True}

    file1 = create_temp_json_file(data1)
    file2 = create_temp_json_file(data2)

    expected_output = """{
  - host: "hexlet.io"
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(file1, file2) == expected_output


def test_generate_diff_changed_values():
    data1 = {"host": "hexlet.io", "timeout": 50}
    data2 = {"host": "hexlet.io", "timeout": 20}

    file1 = create_temp_json_file(data1)
    file2 = create_temp_json_file(data2)

    expected_output = """{
    host: "hexlet.io"
  - timeout: 50
  + timeout: 20
}"""
    assert generate_diff(file1, file2) == expected_output


def test_generate_diff_empty_files():
    data1 = {}
    data2 = {}

    file1 = create_temp_json_file(data1)
    file2 = create_temp_json_file(data2)

    expected_output = """{
}"""
    assert generate_diff(file1, file2) == expected_output


def test_generate_diff_one_empty_file():
    data1 = {}
    data2 = {"host": "hexlet.io", "timeout": 50}

    file1 = create_temp_json_file(data1)
    file2 = create_temp_json_file(data2)

    expected_output = """{
  + host: "hexlet.io"
  + timeout: 50
}"""
    assert generate_diff(file1, file2) == expected_output

