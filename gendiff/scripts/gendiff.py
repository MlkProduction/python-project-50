import argparse
import json

def read_json_file(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


def gendiff_diff(dict1, dict2):

    for key in dict1:
        if key not in dict2:
            print(f'- {key}: {dict1[key]}')
        elif key in dict2 and dict1[key] != dict2[key]:
            print(f'-{key}: {dict1[key]}')
            print(f'+{key}: {dict2[key]}')
        elif key in dict2 and dict1[key] == dict2[key]:
            print(f'{key}: {dict1[key]}')
    for key in dict2:
        if key not in dict1:
            print(f'+ {key}: {dict2[key]}')

def two_dicts(file1, file2):
    first_dicts = read_json_file(file1)
    second_dicts = read_json_file(file2)

    print("Comparing files...\n")
    gendiff_diff(first_dicts, second_dicts)

def main():

    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference')

    parser.add_argument('first_file')           # positional argument
    parser.add_argument('second_file')           # positional argument
    parser.add_argument('-f', '--format', help="Set format of output")
    args = parser.parse_args()

    two_dicts(args.first_file, args.second_file)

if __name__ == "__main__":
    main()
