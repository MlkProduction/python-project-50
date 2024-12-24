import json
import yaml

def read_json_file(file_json):
    with open(file_json, 'r') as file:
        return json.load(file)

def read_yaml_file(file_yaml):
    with open(file_yaml, "r") as file:
        return yaml.safe_load(file)