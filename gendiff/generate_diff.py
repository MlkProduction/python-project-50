#!/usr/bin/env python3
from gendiff.formatters.formatter_json import json_formatter
from gendiff.formatters.plain import formatter_plain
from gendiff.formatters.stylish import format_diff
from gendiff.gendiff_diff import compare_dicts
from gendiff.parser import parse

FORMATTERS = {
    'stylish': format_diff,
    'plain': formatter_plain,
    'json': json_formatter
    }


def generate_diff(file_path1, file_path2, formatter='stylish'):

    dict1 = parse(file_path1)

    dict2 = parse(file_path2)
    diff = compare_dicts(dict1, dict2)

    if formatter == 'stylish':
        return format_diff(diff)
    elif formatter == 'plain':
        return formatter_plain(diff)
    elif formatter == 'json':
        return json_formatter(diff)


