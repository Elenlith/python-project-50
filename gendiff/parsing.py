import json
import yaml
import os


def parse_json(filepath):
    return json.load(open(filepath))


def parse_yaml(filepath):
    with open(filepath, 'r') as file:
        value = yaml.safe_load(file)
    return value


def parse_data(filepath):
    ext = os.path.splitext(filepath)[-1].lower()
    if ext == '.json':
        file = parse_json(filepath)
    elif ext == '.yml' or '.yaml':
        file = parse_yaml(filepath)
    return file
