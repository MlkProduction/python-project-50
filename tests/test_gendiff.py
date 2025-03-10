import pytest

from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, expected", [
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'stylish',
     "tests/fixtures/correct_result.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'json',
     "tests/fixtures/correct_result.json"),
    ("tests/fixtures/new_file1.json", "tests/fixtures/new_file2.json", 
     'stylish', "tests/fixtures/stylish_result.txt"),
    ("tests/fixtures/new_file1.json", "tests/fixtures/new_file2.json", 'plain',
     "tests/fixtures/result_plain.txt"),
    ("tests/fixtures/new_file1.json", "tests/fixtures/new_file2.json", 'json',
     "tests/fixtures/result.json"),
    ("tests/fixtures/file1path.yml", "tests/fixtures/file2path.yml", 'stylish',
     "tests/fixtures/stylish_result.txt")
])
def test_generate_diff(file1, file2, formatter, expected):
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(expected)
    assert diff == expected_result


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
