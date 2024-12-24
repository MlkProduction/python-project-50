def gendiff_diff(dict1, dict2):

    result = []
    for key in dict1:
        if key not in dict2:
            result.append(f'- {key}: {dict1[key]}')
        elif key in dict2 and dict1[key] != dict2[key]:
            result.append(f'- {key}: {dict1[key]}')
            result.append(f'+ {key}: {dict2[key]}')
        elif key in dict2 and dict1[key] == dict2[key]:
            result.append(f'{key}: {dict1[key]}')
    for key in dict2:
        if key not in dict1:
            result.append(f'+ {key}: {dict2[key]}')
    return '\n'.join(result)



