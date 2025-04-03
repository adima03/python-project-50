import argparse


def generate_diff(file1, file2):
    """
    Функция для сравнения двух файлов и вывода их различий.
    В реальной реализации здесь будет логика сравнения файлов.
    """
    return f"Comparing {file1} and {file2}\nDifferences:\n(Placeholder for actual diff logic)"


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file)

    print(result)


if __name__ == "__main__":
    main()