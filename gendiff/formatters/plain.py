def format_value(value):
 
    if isinstance(value, dict):
        return '[complex value]'

    elif isinstance(value, bool):
        return str(value).lower()
    
    elif value is None:
        return 'null'

    elif isinstance(value, str):
        return f"'{value}'"


    return value


def formatter_plain(all_dict, path=''):
    result = []
    for key, (flag, value) in all_dict.items():
        full_path = f"{path}.{key}" if path else key

        if flag == 'removed':
            result.append(f"Property '{full_path}' was removed")
        elif flag == 'added':
            result.append(f"Property '{full_path}' was added with value: {format_value(value)}")
        elif flag == 'changed':
            old_value, new_value = value
            result.append(f"Property '{full_path}' was updated. From {format_value(old_value)} to {format_value(new_value)}")
        elif flag == 'nested':
            result.append(formatter_plain(value, full_path)) 

    formatted_result = '\n'.join(result)
    return formatted_result

