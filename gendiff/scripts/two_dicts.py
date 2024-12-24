from gendiff.scripts.gendiff import gendiff_diff
from gendiff.scripts.read_files import read_yaml_file, read_json_file


def two_dicts_json(file1, file2):
    first = read_json_file(file1)
    second = read_json_file(file2)

    result = gendiff_diff(first, second)
    return result

def two_dicts_yaml(file1, file2):
    first = read_yaml_file(file1)
    second = read_yaml_file(file2)

    result = gendiff_diff(first, second)
    return result