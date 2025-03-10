import json
import os

import yaml

from gendiff.read_files import read_file


def format_extensions(file):
    
    extension = os.path.splitext(file)[1].lower()
    return extension[1:]


def parse_format(data, format):
    
    if format == "json":
        return json.loads(data)
    if format in ("yaml", "yml"):
        return yaml.safe_load(data)
    raise ValueError(f"Unsupported format: {format}")


def parse(file_path):
    
    format = format_extensions(file_path)
    read = read_file(file_path)
    return parse_format(read, format)
