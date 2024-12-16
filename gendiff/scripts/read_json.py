import json

def read_json_file():
   return json.load(open('file1.json')), json.load(open('file2.json'))
print(read_json_file())

def gendiff_diff(dict1, dict2):

    for key in dict1:
        if key not in dict2:
            print(f'{'-'} {key}: {dict1[key]}')
        elif key in dict2 and dict1[key] != dict2[key]:
            print(f'-{key}: {dict1[key]}')
            print(f'+{key}: {dict2[key]}')
        elif key in dict2 and dict1[key] == dict2[key]:
            print(f'{key}: {dict1[key]}')
    for key in dict2:
        if key not in dict1:
            print(f'{'+'} {key}: {dict2[key]}')

