import pytest

from gendiff.scripts.gendiff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, expected", [
    ("file1.json", "file2.json", 'stylish',
     "tests/fixtures/correct_result.txt"),
    ("file1.json", "file2.json", 'json',
     "tests/fixtures/correct_result.json"),
    ("new_file1.json", "new_file2.json", 'stylish',
     "tests/fixtures/stylish_result.txt"),
    ("new_file1.json", "new_file2.json", 'plain',
     "tests/fixtures/result_plain.txt"),
    ("new_file1.json", "new_file2.json", 'json',
     "tests/fixtures/result.json"),
    ("file1path.yml", "file2path.yml", 'stylish',
     "tests/fixtures/stylish_result.txt")
])
def test_generate_diff(file1, file2, formatter, expected):
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(expected)
    assert diff == expected_result


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
