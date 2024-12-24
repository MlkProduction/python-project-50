from gendiff.scripts.two_dicts import two_dicts_json, two_dicts_yaml
import pytest


@pytest.mark.parametrize(
    "file1, file2, expected_file",
    [
        ("fixtures/file1.json", "fixtures/file2.json", "correct_result.txt"),
    ]
)
def test_generate_diff_json(file1, file2, expected_file):
    with open(expected_file, 'r') as f:
        expected = f.read().strip()

    result = two_dicts_json(file1, file2)

    # Сравнение
    assert result == expected

@pytest.mark.parametrize(
    "file1, file2, expected_file",
    [
        ("fixtures/file1path.yml", "fixtures/file2path.yml", "correct_result.txt"),
    ]
)
def test_generate_diff_yaml(file1, file2, expected_file):
    with open(expected_file, 'r') as f:
        expected = f.read().strip()

    result = two_dicts_yaml(file1, file2)

    # Сравнение
    assert result == expected