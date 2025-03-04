import os
import json
import yaml


BASE_DIR = "tests/fixtures"  


def read_file(file):
    if not os.path.isabs(file):  
        file = os.path.join(BASE_DIR, file)

    if not os.path.exists(file):  
        raise FileNotFoundError(f"File '{file}' not found.")

    extension = os.path.splitext(file)[1].lower()
    parser = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }

    if extension not in parser:
        raise ValueError(f"Unsupported file format: {extension}")

    with open(file) as f:
        return parser[extension](f)
