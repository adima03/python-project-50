### Hexlet tests and linter status:
[![Actions Status](https://github.com/adima03/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/adima03/python-project-50/actions)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=adima03_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=adima03_python-project-50)

https://asciinema.org/a/dgePPUSNZKQ6sYiPhz5Jj8DHu

https://asciinema.org/a/ssihpQEy4HsvHcMBKPQRbBnFw

https://asciinema.org/a/CfL3j023XrW7artFuHEvXybsG

https://asciinema.org/a/vlRiDbi3XmbImWbBXzHkjjSbX

https://asciinema.org/a/U76hYZG0770yyqGVe0iE8gor0

# Difference Calculator (gendiff)

- gendiff is a command-line tool for finding differences between files. This is the second project developed as part of
  the Hexlet course.

***

## Requirements:

[Python 3.13 +] - (https://www.python.org/downloads/)

[UV 0.5.11 +] - (https://astral.sh)
***

## Installation:

``` 
git clone git@github.com:adima03/python-project-50.git
```

````
cd python-project-50
````

`````
uv build
``````

````````
uv tool install dist/*.whl
````````

***

## Supported File Formats

#### - JSON (.json)

#### - YAML (.yaml, .yml)

***

## Usage

1. Place the files you want to compare inside the tests/test_data directory.
2. Run the following command, replacing file1 and file2 with your actual file names:

````
uv run gendiff tests/test_data/<file1> tests/test_data/<file2>
````

3. By default, the output is formatted using the stylish formatter.

- To use a different format (json or plain), specify it with the -f flag:

***

## Development and Testing
### Linting
Run ruff to check for linting issues:
```
make check
```
Running Tests
```
make tests
```